#!/usr/bin/env python3
"""
SOC Utilities & Complementary Tools Script
Script de utilidades complementarias para SOC
"""

import os
import subprocess
import sys
import time
import json
import requests
from pathlib import Path
from datetime import datetime

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

class SOCUtilities:
    def __init__(self):
        self.utilities_dir = "/opt/soc/utilities"
        self.scripts_dir = "/opt/soc/scripts"
        self.tools_dir = "/opt/soc/tools"
        self.backup_dir = "/opt/soc/backup"
        
    def print_banner(self):
        banner = f"""
{Colors.BLUE}
╔══════════════════════════════════════════════════════════════╗
║              SOC UTILITIES & COMPLEMENTARY TOOLS             ║
║                    Script Secundario                         ║
║                Advanced Security Arsenal                     ║
╚══════════════════════════════════════════════════════════════╝
{Colors.ENDC}
        """
        print(banner)
    
    def show_menu(self):
        menu = f"""
{Colors.CYAN}[MENÚ PRINCIPAL]{Colors.ENDC}
1.  Instalar herramientas avanzadas de pentesting
2.  Configurar automatización y orquestación
3.  Instalar herramientas de threat hunting
4.  Configurar análisis de malware
5.  Instalar herramientas de criptografía y steganografía
6.  Configurar herramientas de red y comunicaciones
7.  Instalar utilidades de desarrollo y scripting
8.  Configurar herramientas de backup y recuperación
9.  Instalar herramientas de compliance y auditoría
10. Configurar monitoreo avanzado
11. Instalar herramientas de dark web monitoring
12. Configurar integración con APIs externas
13. Crear scripts personalizados
14. Instalar todas las utilidades
15. Salir

{Colors.WARNING}Selecciona una opción:{Colors.ENDC} """
        return input(menu)
    
    def run_command(self, command, check=True):
        """Ejecuta comandos del sistema con manejo de errores"""
        try:
            print(f"{Colors.CYAN}[INFO]{Colors.ENDC} Ejecutando: {command}")
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if check and result.returncode != 0:
                print(f"{Colors.FAIL}[ERROR]{Colors.ENDC} Error en comando: {command}")
                print(f"STDERR: {result.stderr}")
                return False
            return True
        except Exception as e:
            print(f"{Colors.FAIL}[ERROR]{Colors.ENDC} Excepción: {e}")
            return False
    
    def create_directories(self):
        """Crea directorios para utilidades"""
        directories = [
            self.utilities_dir,
            f"{self.utilities_dir}/pentesting",
            f"{self.utilities_dir}/automation",
            f"{self.utilities_dir}/threat_hunting",
            f"{self.utilities_dir}/malware_analysis",
            f"{self.utilities_dir}/crypto",
            f"{self.utilities_dir}/network",
            f"{self.utilities_dir}/development",
            self.backup_dir,
            f"{self.utilities_dir}/compliance",
            f"{self.utilities_dir}/monitoring",
            f"{self.utilities_dir}/darkweb",
            f"{self.utilities_dir}/apis"
        ]
        
        for directory in directories:
            Path(directory).mkdir(parents=True, exist_ok=True)
            print(f"{Colors.GREEN}[✓]{Colors.ENDC} Creado: {directory}")
    
    def install_advanced_pentesting(self):
        """Instala herramientas avanzadas de pentesting"""
        print(f"\n{Colors.HEADER}[PENTESTING AVANZADO]{Colors.ENDC}")
        
        # Herramientas de reconocimiento avanzado
        recon_tools = [
            "amass",
            "subfinder",
            "assetfinder",
            "httpx",
            "dnsx",
            "katana",
            "gau",
            "waybackurls"
        ]
        
        # Instalar herramientas Go
        go_tools = {
            "amass": "github.com/OWASP/Amass/v3/...@master",
            "subfinder": "github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest",
            "httpx": "github.com/projectdiscovery/httpx/cmd/httpx@latest",
            "dnsx": "github.com/projectdiscovery/dnsx/cmd/dnsx@latest",
            "katana": "github.com/projectdiscovery/katana/cmd/katana@latest",
            "nuclei": "github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest"
        }
        
        # Instalar Go si no está instalado
        self.run_command("apt install golang-go -y")
        
        for tool, package in go_tools.items():
            self.run_command(f"go install {package}", check=False)
        
        # Herramientas web avanzadas
        web_tools = [
            "burpsuite",
            "zaproxy",
            "sqlmap",
            "commix",
            "xsstrike"
        ]
        
        for tool in web_tools:
            self.run_command(f"apt install {tool} -y", check=False)
        
        # Instalar herramientas desde GitHub
        github_tools = [
            ("https://github.com/OJ/gobuster.git", "gobuster"),
            ("https://github.com/ffuf/ffuf.git", "ffuf"),
            ("https://github.com/tomnomnom/gf.git", "gf"),
            ("https://github.com/1ndianl33t/Gf-Patterns.git", "gf-patterns")
        ]
        
        for repo, name in github_tools:
            self.run_command(f"cd {self.utilities_dir}/pentesting && git clone {repo}", check=False)
    
    def install_automation_orchestration(self):
        """Configura automatización y orquestación"""
        print(f"\n{Colors.HEADER}[AUTOMATIZACIÓN Y ORQUESTACIÓN]{Colors.ENDC}")
        
        # Instalar Ansible
        ansible_commands = [
            "apt install ansible -y",
            "pip3 install ansible-runner",
            "pip3 install molecule"
        ]
        
        for cmd in ansible_commands:
            self.run_command(cmd)
        
        # Instalar Terraform
        terraform_commands = [
            "wget -O- https://apt.releases.hashicorp.com/gpg | gpg --dearmor | tee /usr/share/keyrings/hashicorp-archive-keyring.gpg",
            "echo 'deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com jammy main' | tee /etc/apt/sources.list.d/hashicorp.list",
            "apt update && apt install terraform -y"
        ]
        
        for cmd in terraform_commands:
            self.run_command(cmd, check=False)
        
        # Instalar Docker y Docker Compose
        docker_commands = [
            "apt install docker.io docker-compose -y",
            "systemctl enable docker",
            "systemctl start docker",
            "usermod -aG docker $USER"
        ]
        
        for cmd in docker_commands:
            self.run_command(cmd)
        
        # Crear playbooks de Ansible básicos
        self.create_ansible_playbooks()
    
    def install_threat_hunting_tools(self):
        """Instala herramientas de threat hunting"""
        print(f"\n{Colors.HEADER}[THREAT HUNTING]{Colors.ENDC}")
        
        # Sigma rules
        sigma_commands = [
            f"cd {self.utilities_dir}/threat_hunting",
            "git clone https://github.com/SigmaHQ/sigma.git",
            "pip3 install sigmatools"
        ]
        
        for cmd in sigma_commands:
            self.run_command(cmd, check=False)
        
        # YARA rules
        yara_commands = [
            "apt install yara -y",
            f"cd {self.utilities_dir}/threat_hunting",
            "git clone https://github.com/Yara-Rules/rules.git yara-rules"
        ]
        
        for cmd in yara_commands:
            self.run_command(cmd)
        
        # Instalar Hayabusa (Windows event log analyzer)
        hayabusa_commands = [
            f"cd {self.utilities_dir}/threat_hunting",
            "wget https://github.com/Yamato-Security/hayabusa/releases/latest/download/hayabusa-2.11.0-linux-x64.zip",
            "unzip hayabusa-2.11.0-linux-x64.zip",
            "chmod +x hayabusa"
        ]
        
        for cmd in hayabusa_commands:
            self.run_command(cmd, check=False)
        
        # Chainsaw para Windows event logs
        chainsaw_commands = [
            f"cd {self.utilities_dir}/threat_hunting",
            "wget https://github.com/WithSecureLabs/chainsaw/releases/latest/download/chainsaw_x86_64-unknown-linux-gnu.tar.gz",
            "tar -xzf chainsaw_x86_64-unknown-linux-gnu.tar.gz"
        ]
        
        for cmd in chainsaw_commands:
            self.run_command(cmd, check=False)
    
    def install_malware_analysis_tools(self):
        """Instala herramientas de análisis de malware"""
        print(f"\n{Colors.HEADER}[ANÁLISIS DE MALWARE]{Colors.ENDC}")
        
        malware_tools = [
            "radare2",
            "ghidra",
            "cutter",
            "rizin",
            "remnux-tools",
            "flare-floss",
            "peframe",
            "pefile"
        ]
        
        for tool in malware_tools:
            self.run_command(f"apt install {tool} -y", check=False)
        
        # Instalar REMnux tools
        remnux_commands = [
            "wget -O remnux-cli https://REMnux.org/remnux-cli",
            "mv remnux-cli /usr/local/bin/",
            "chmod +x /usr/local/bin/remnux-cli",
            "remnux-cli install --mode=addon"
        ]
        
        for cmd in remnux_commands:
            self.run_command(cmd, check=False)
        
        # Instalar herramientas Python para malware
        python_malware_tools = [
            "pycryptodome",
            "yara-python",
            "pefile",
            "oletools",
            "exifread",
            "python-magic",
            "requests",
            "beautifulsoup4"
        ]
        
        for tool in python_malware_tools:
            self.run_command(f"pip3 install {tool}")
    
    def install_crypto_stego_tools(self):
        """Instala herramientas de criptografía y steganografía"""
        print(f"\n{Colors.HEADER}[CRIPTOGRAFÍA Y STEGANOGRAFÍA]{Colors.ENDC}")
        
        crypto_tools = [
            "steghide",
            "stegosuite",
            "outguess",
            "binwalk",
            "foremost",
            "exiftool",
            "hashcat",
            "john",
            "hydra"
        ]
        
        for tool in crypto_tools:
            self.run_command(f"apt install {tool} -y", check=False)
        
        # Herramientas adicionales de GitHub
        stego_github_tools = [
            ("https://github.com/DominicBreuker/stego-toolkit.git", "stego-toolkit"),
            ("https://github.com/bannsec/steganography.git", "steganography")
        ]
        
        for repo, name in stego_github_tools:
            self.run_command(f"cd {self.utilities_dir}/crypto && git clone {repo}", check=False)
    
    def install_network_communication_tools(self):
        """Instala herramientas de red y comunicaciones"""
        print(f"\n{Colors.HEADER}[RED Y COMUNICACIONES]{Colors.ENDC}")
        
        network_tools = [
            "ncat",
            "socat",
            "proxychains4",
            "tor",
            "i2p",
            "openvpn",
            "wireguard",
            "stunnel4"
        ]
        
        for tool in network_tools:
            self.run_command(f"apt install {tool} -y", check=False)
        
        # Configurar Proxychains
        proxychains_config = """
strict_chain
proxy_dns
remote_dns_subnet 224
tcp_read_time_out 15000
tcp_connect_time_out 8000

[ProxyList]
socks4  127.0.0.1 9050
        """
        
        with open("/etc/proxychains4.conf", "w") as f:
            f.write(proxychains_config)
    
    def install_development_scripting(self):
        """Instala herramientas de desarrollo y scripting"""
        print(f"\n{Colors.HEADER}[DESARROLLO Y SCRIPTING]{Colors.ENDC}")
        
        dev_tools = [
            "git",
            "vim",
            "nano",
            "code",
            "python3-pip",
            "nodejs",
            "npm",
            "ruby",
            "golang-go",
            "php",
            "curl",
            "wget",
            "jq",
            "xmlstarlet"
        ]
        
        for tool in dev_tools:
            self.run_command(f"apt install {tool} -y", check=False)
        
        # Instalar herramientas Python útiles
        python_tools = [
            "requests",
            "beautifulsoup4",
            "selenium",
            "scrapy",
            "pandas",
            "numpy",
            "matplotlib",
            "scapy",
            "paramiko",
            "fabric"
        ]
        
        for tool in python_tools:
            self.run_command(f"pip3 install {tool}")
    
    def configure_backup_recovery(self):
        """Configura herramientas de backup y recuperación"""
        print(f"\n{Colors.HEADER}[BACKUP Y RECUPERACIÓN]{Colors.ENDC}")
        
        backup_tools = [
            "rsync",
            "duplicity",
            "borgbackup",
            "restic"
        ]
        
        for tool in backup_tools:
            self.run_command(f"apt install {tool} -y", check=False)
        
        # Crear script de backup automatizado
        backup_script = f"""#!/bin/bash
# Script de backup automatizado para SOC
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="{self.backup_dir}"
SOC_DIR="/opt/soc"

echo "Iniciando backup del SOC - $DATE"

# Crear backup comprimido
tar -czf $BACKUP_DIR/soc_backup_$DATE.tar.gz $SOC_DIR

# Mantener solo los últimos 7 backups
find $BACKUP_DIR -name "soc_backup_*.tar.gz" -mtime +7 -delete

echo "Backup completado: $BACKUP_DIR/soc_backup_$DATE.tar.gz"
        """
        
        with open(f"{self.scripts_dir}/backup_soc.sh", "w") as f:
            f.write(backup_script)
        
        self.run_command(f"chmod +x {self.scripts_dir}/backup_soc.sh")
    
    def install_compliance_audit_tools(self):
        """Instala herramientas de compliance y auditoría"""
        print(f"\n{Colors.HEADER}[COMPLIANCE Y AUDITORÍA]{Colors.ENDC}")
        
        audit_tools = [
            "lynis",
            "rkhunter",
            "chkrootkit",
            "aide",
            "auditd",
            "tiger"
        ]
        
        for tool in audit_tools:
            self.run_command(f"apt install {tool} -y", check=False)
        
        # Configurar auditd
        auditd_rules = """
# SOC Audit Rules
-w /etc/passwd -p wa -k identity
-w /etc/group -p wa -k identity
-w /etc/shadow -p wa -k identity
-w /etc/sudoers -p wa -k identity
-w /var/log/auth.log -p wa -k authentication
-w /var/log/secure -p wa -k authentication
-w /bin/su -p x -k privileged
-w /usr/bin/sudo -p x -k privileged
-w /etc/ssh/sshd_config -p wa -k sshd
        """
        
        with open("/etc/audit/rules.d/soc.rules", "w") as f:
            f.write(auditd_rules)
    
    def configure_advanced_monitoring(self):
        """Configura monitoreo avanzado"""
        print(f"\n{Colors.HEADER}[MONITOREO AVANZADO]{Colors.ENDC}")
        
        # Instalar Beats (Elastic Stack)
        beats_commands = [
            "wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key add -",
            "apt install filebeat metricbeat packetbeat auditbeat heartbeat-elastic -y"
        ]
        
        for cmd in beats_commands:
            self.run_command(cmd, check=False)
        
        # Instalar OSSEC HIDS
        ossec_commands = [
            f"cd {self.utilities_dir}/monitoring",
            "wget https://github.com/ossec/ossec-hids/archive/3.7.0.tar.gz",
            "tar -xzf 3.7.0.tar.gz",
            "cd ossec-hids-3.7.0",
            "./install.sh"
        ]
        
        for cmd in ossec_commands:
            self.run_command(cmd, check=False)
    
    def install_darkweb_monitoring(self):
        """Instala herramientas de monitoreo de dark web"""
        print(f"\n{Colors.HEADER}[DARK WEB MONITORING]{Colors.ENDC}")
        
        # Instalar Tor y herramientas relacionadas
        tor_commands = [
            "apt install tor torsocks -y",
            "systemctl enable tor",
            "systemctl start tor"
        ]
        
        for cmd in tor_commands:
            self.run_command(cmd)
        
        # OnionScan
        onionscan_commands = [
            f"cd {self.utilities_dir}/darkweb",
            "go install github.com/s-rah/onionscan@latest"
        ]
        
        for cmd in onionscan_commands:
            self.run_command(cmd, check=False)
    
    def configure_api_integrations(self):
        """Configura integraciones con APIs externas"""
        print(f"\n{Colors.HEADER}[INTEGRACIÓN CON APIS]{Colors.ENDC}")
        
        # Crear script de integración con VirusTotal
        vt_script = """#!/usr/bin/env python3
import requests
import sys
import json

class VirusTotalAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://www.virustotal.com/api/v3"
    
    def scan_file_hash(self, file_hash):
        headers = {"x-apikey": self.api_key}
        response = requests.get(f"{self.base_url}/files/{file_hash}", headers=headers)
        return response.json()
    
    def scan_url(self, url):
        headers = {"x-apikey": self.api_key}
        data = {"url": url}
        response = requests.post(f"{self.base_url}/urls", headers=headers, data=data)
        return response.json()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python3 vt_scanner.py <API_KEY> <HASH_OR_URL>")
        sys.exit(1)
    
    api_key = sys.argv[1]
    target = sys.argv[2]
    
    vt = VirusTotalAPI(api_key)
    
    if len(target) in [32, 40, 64]:  # MD5, SHA1, SHA256
        result = vt.scan_file_hash(target)
    else:
        result = vt.scan_url(target)
    
    print(json.dumps(result, indent=2))
        """
        
        with open(f"{self.utilities_dir}/apis/vt_scanner.py", "w") as f:
            f.write(vt_script)
        
        self.run_command(f"chmod +x {self.utilities_dir}/apis/vt_scanner.py")
    
    def create_custom_scripts(self):
        """Crea scripts personalizados"""
        print(f"\n{Colors.HEADER}[SCRIPTS PERSONALIZADOS]{Colors.ENDC}")
        
        # Script de health check del SOC
        health_check_script = f"""#!/bin/bash
# SOC Health Check Script
echo "=== SOC HEALTH CHECK ==="
echo "Fecha: $(date)"
echo

# Verificar servicios críticos
services=("elasticsearch" "kibana" "logstash" "suricata" "nginx")
for service in "${{services[@]}}"; do
    if systemctl is-active --quiet $service; then
        echo "✅ $service: RUNNING"
    else
        echo "❌ $service: STOPPED"
    fi
done

# Verificar espacio en disco
echo
echo "=== ESPACIO EN DISCO ==="
df -h | grep -E "/$|/opt|/var"

# Verificar memoria
echo
echo "=== MEMORIA ==="
free -h

# Verificar carga del sistema
echo
echo "=== CARGA DEL SISTEMA ==="
uptime

# Verificar conectividad
echo
echo "=== CONECTIVIDAD ==="
ping -c 3 8.8.8.8 > /dev/null && echo "✅ Internet: OK" || echo "❌ Internet: FAIL"
        """
        
        with open(f"{self.scripts_dir}/health_check.sh", "w") as f:
            f.write(health_check_script)
        
        # Script de log analyzer
        log_analyzer_script = """#!/usr/bin/env python3
import re
import sys
from collections import Counter
from datetime import datetime

def analyze_apache_logs(log_file):
    with open(log_file, 'r') as f:
        logs = f.readlines()
    
    ips = []
    status_codes = []
    user_agents = []
    
    for log in logs:
        # Regex para Apache Combined Log Format
        pattern = r'(\d+\.\d+\.\d+\.\d+).*?".*?" (\d{3}) \d+ ".*?" "(.*?)"'
        match = re.search(pattern, log)
        
        if match:
            ip, status, user_agent = match.groups()
            ips.append(ip)
            status_codes.append(status)
            user_agents.append(user_agent)
    
    print("=== TOP 10 IPs ===")
    for ip, count in Counter(ips).most_common(10):
        print(f"{ip}: {count}")
    
    print("\\n=== STATUS CODES ===")
    for code, count in Counter(status_codes).most_common():
        print(f"{code}: {count}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 log_analyzer.py <log_file>")
        sys.exit(1)
    
    analyze_apache_logs(sys.argv[1])
        """
        
        with open(f"{self.scripts_dir}/log_analyzer.py", "w") as f:
            f.write(log_analyzer_script)
        
        # Hacer ejecutables
        scripts = [
            f"{self.scripts_dir}/health_check.sh",
            f"{self.scripts_dir}/log_analyzer.py"
        ]
        
        for script in scripts:
            self.run_command(f"chmod +x {script}")
    
    def create_ansible_playbooks(self):
        """Crea playbooks de Ansible para automatización"""
        playbook_dir = f"{self.utilities_dir}/automation/playbooks"
        Path(playbook_dir).mkdir(parents=True, exist_ok=True)
        
        # Playbook para hardening básico
        hardening_playbook = """---
- name: SOC Basic Hardening
  hosts: localhost
  become: yes
  
  tasks:
    - name: Update system packages
      apt:
        update_cache: yes
        upgrade: dist
    
    - name: Install fail2ban
      apt:
        name: fail2ban
        state: present
    
    - name: Configure SSH hardening
      lineinfile:
        path: /etc/ssh/sshd_config
        regexp: "{{ item.regexp }}"
        line: "{{ item.line }}"
      with_items:
        - { regexp: '^PermitRootLogin', line: 'PermitRootLogin no' }
        - { regexp: '^PasswordAuthentication', line: 'PasswordAuthentication no' }
        - { regexp: '^Protocol', line: 'Protocol 2' }
    
    - name: Restart SSH service
      service:
        name: ssh
        state: restarted
        """
        
        with open(f"{playbook_dir}/hardening.yml", "w") as f:
            f.write(hardening_playbook)
    
    def install_all_utilities(self):
        """Instala todas las utilidades"""
        print(f"\n{Colors.BOLD}[INSTALACIÓN COMPLETA DE UTILIDADES]{Colors.ENDC}")
        
        self.create_directories()
        self.install_advanced_pentesting()
        self.install_automation_orchestration()
        self.install_threat_hunting_tools()
        self.install_malware_analysis_tools()
        self.install_crypto_stego_tools()
        self.install_network_communication_tools()
        self.install_development_scripting()
        self.configure_backup_recovery()
        self.install_compliance_audit_tools()
        self.configure_advanced_monitoring()
        self.install_darkweb_monitoring()
        self.configure_api_integrations()
        self.create_custom_scripts()
        
        print(f"\n{Colors.GREEN}[COMPLETADO]{Colors.ENDC} Todas las utilidades han sido instaladas.")
        print(f"{Colors.CYAN}Directorio principal:{Colors.ENDC} {self.utilities_dir}")
        print(f"{Colors.CYAN}Scripts personalizados:{Colors.ENDC} {self.scripts_dir}")
    
    def run(self):
        """Función principal"""
        if os.geteuid() != 0:
            print(f"{Colors.FAIL}[ERROR]{Colors.ENDC} Este script debe ejecutarse como root")
            sys.exit(1)
        
        self.print_banner()
        
        while True:
            choice = self.show_menu()
            
            try:
                if choice == "1":
                    self.install_advanced_pentesting()
                elif choice == "2":
                    self.install_automation_orchestration()
                elif choice == "3":
                    self.install_threat_hunting_tools()
                elif choice == "4":
                    self.install_malware_analysis_tools()
                elif choice == "5":
                    self.install_crypto_stego_tools()
                elif choice == "6":
                    self.install_network_communication_tools()
                elif choice == "7":
                    self.install_development_scripting()
                elif choice == "8":
                    self.configure_backup_recovery()
                elif choice == "9":
                    self.install_compliance_audit_tools()
                elif choice == "10":
                    self.configure_advanced_monitoring()
                elif choice == "11":
                    self.install_darkweb_monitoring()
                elif choice == "12":
                    self.configure_api_integrations()
                elif choice == "13":
                    self.create_custom_scripts()
                elif choice == "14":
                    self.install_all_utilities()
                elif choice == "15":
                    print(f"{Colors.CYAN}¡Hasta luego!{Colors.ENDC}")
                    break
                else:
                    print(f"{Colors.WARNING}Opción no válida{Colors.ENDC}")
                
                input(f"\n{Colors.CYAN}Presiona Enter para continuar...{Colors.ENDC}")
                
            except KeyboardInterrupt:
                print(f"\n{Colors.WARNING}Operación cancelada por el usuario{Colors.ENDC}")
                break
            except Exception as e:
                print(f"{Colors.FAIL}Error inesperado: {e}{Colors.ENDC}")

if __name__ == "__main__":
    soc_utils = SOCUtilities()
    soc_utils.run()
