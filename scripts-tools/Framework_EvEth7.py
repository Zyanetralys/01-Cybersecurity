#!/usr/bin/env python3
"""
Evaluación ética
"""

import socket
import threading
import subprocess
import requests
import json
import sys
import argparse
import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
import ipaddress
import dns.resolver
import ssl
import urllib3
from urllib.parse import urljoin, urlparse
import re
import hashlib
import base64

# Suprimir warnings SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Colors:
    """Códigos de colores para output mejorado"""
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class Logger:
    """Sistema de logging profesional"""
    
    def __init__(self, filename=None):
        self.filename = filename
        if filename:
            with open(filename, 'w') as f:
                f.write(f"=== PENTEST REPORT - {datetime.now()} ===\n\n")
    
    def log(self, message, level="INFO", color=Colors.WHITE):
        timestamp = datetime.now().strftime("%H:%M:%S")
        formatted_msg = f"[{timestamp}] [{level}] {message}"
        print(f"{color}{formatted_msg}{Colors.END}")
        
        if self.filename:
            with open(self.filename, 'a') as f:
                f.write(formatted_msg + "\n")

class NetworkScanner:
    """Escáner de red avanzado"""
    
    def __init__(self, logger):
        self.logger = logger
        self.open_ports = {}
        self.services = {}
    
    def ping_sweep(self, network):
        """Ping sweep para descubrir hosts activos"""
        self.logger.log(f"Iniciando ping sweep en {network}", "SCAN", Colors.CYAN)
        active_hosts = []
        
        try:
            net = ipaddress.IPv4Network(network, strict=False)
            with ThreadPoolExecutor(max_workers=50) as executor:
                futures = {executor.submit(self._ping_host, str(ip)): ip for ip in net.hosts()}
                
                for future in as_completed(futures):
                    if future.result():
                        active_hosts.append(str(futures[future]))
        except Exception as e:
            self.logger.log(f"Error en ping sweep: {e}", "ERROR", Colors.RED)
        
        self.logger.log(f"Hosts activos encontrados: {len(active_hosts)}", "SUCCESS", Colors.GREEN)
        return active_hosts
    
    def _ping_host(self, ip):
        """Ping individual a un host"""
        try:
            result = subprocess.run(['ping', '-c', '1', '-W', '1', ip], 
                                  capture_output=True, text=True, timeout=2)
            return result.returncode == 0
        except:
            return False
    
    def port_scan(self, target, ports=None, scan_type="SYN"):
        """Escáner de puertos avanzado"""
        if ports is None:
            ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 993, 995, 1433, 3306, 3389, 5432, 8080, 8443]
        
        self.logger.log(f"Escaneando puertos en {target}", "SCAN", Colors.CYAN)
        open_ports = []
        
        with ThreadPoolExecutor(max_workers=100) as executor:
            futures = {executor.submit(self._scan_port, target, port): port for port in ports}
            
            for future in as_completed(futures):
                port = futures[future]
                if future.result():
                    open_ports.append(port)
                    self.logger.log(f"Puerto abierto: {port}", "FOUND", Colors.GREEN)
        
        self.open_ports[target] = open_ports
        return open_ports
    
    def _scan_port(self, target, port):
        """Escaneo individual de puerto"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            sock.close()
            return result == 0
        except:
            return False
    
    def service_detection(self, target, ports):
        """Detección de servicios en puertos abiertos"""
        self.logger.log(f"Detectando servicios en {target}", "SCAN", Colors.CYAN)
        services = {}
        
        for port in ports:
            try:
                service = self._detect_service(target, port)
                if service:
                    services[port] = service
                    self.logger.log(f"Puerto {port}: {service}", "SERVICE", Colors.YELLOW)
            except Exception as e:
                continue
        
        self.services[target] = services
        return services
    
    def _detect_service(self, target, port):
        """Detección individual de servicio"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            sock.connect((target, port))
            
            # Enviar banner grab
            sock.send(b"GET / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n")
            banner = sock.recv(1024).decode('utf-8', errors='ignore')
            sock.close()
            
            # Identificar servicio basado en banner
            if "HTTP" in banner:
                return f"HTTP - {banner.split()[0] if banner.split() else 'Unknown'}"
            elif port == 22:
                return "SSH"
            elif port == 21:
                return "FTP"
            elif port == 25:
                return "SMTP"
            elif port == 53:
                return "DNS"
            else:
                return f"Unknown - Port {port}"
        except:
            return None

class WebScanner:
    """Escáner web especializado"""
    
    def __init__(self, logger):
        self.logger = logger
        self.session = requests.Session()
        self.session.verify = False
        self.session.timeout = 5
        self.vulnerabilities = []
    
    def scan_website(self, url):
        """Escaneo completo de sitio web"""
        self.logger.log(f"Iniciando escaneo web de {url}", "WEB", Colors.PURPLE)
        
        results = {
            'url': url,
            'headers': self._analyze_headers(url),
            'directories': self._directory_bruteforce(url),
            'forms': self._analyze_forms(url),
            'ssl': self._analyze_ssl(url),
            'vulnerabilities': []
        }
        
        # Pruebas de vulnerabilidades comunes
        self._test_sql_injection(url, results)
        self._test_xss(url, results)
        self._test_directory_traversal(url, results)
        
        return results
    
    def _analyze_headers(self, url):
        """Análisis de headers de seguridad"""
        try:
            response = self.session.get(url)
            headers = dict(response.headers)
            
            security_headers = [
                'X-Frame-Options', 'X-XSS-Protection', 'X-Content-Type-Options',
                'Strict-Transport-Security', 'Content-Security-Policy'
            ]
            
            missing_headers = [h for h in security_headers if h not in headers]
            if missing_headers:
                self.logger.log(f"Headers de seguridad faltantes: {missing_headers}", "VULN", Colors.RED)
            
            return headers
        except Exception as e:
            self.logger.log(f"Error analizando headers: {e}", "ERROR", Colors.RED)
            return {}
    
    def _directory_bruteforce(self, url):
        """Fuerza bruta de directorios"""
        common_dirs = [
            'admin', 'administrator', 'login', 'dashboard', 'panel',
            'backup', 'test', 'dev', 'api', 'config', 'uploads',
            'files', 'docs', 'phpmyadmin', 'wp-admin', 'wp-content'
        ]
        
        found_dirs = []
        for directory in common_dirs:
            test_url = urljoin(url, directory)
            try:
                response = self.session.get(test_url)
                if response.status_code == 200:
                    found_dirs.append(directory)
                    self.logger.log(f"Directorio encontrado: /{directory}", "FOUND", Colors.GREEN)
            except:
                continue
        
        return found_dirs
    
    def _analyze_forms(self, url):
        """Análisis de formularios web"""
        try:
            response = self.session.get(url)
            forms = re.findall(r'<form[^>]*>(.*?)</form>', response.text, re.DOTALL | re.IGNORECASE)
            
            form_info = []
            for form in forms:
                inputs = re.findall(r'<input[^>]*>', form, re.IGNORECASE)
                form_info.append({
                    'inputs': len(inputs),
                    'has_password': 'type="password"' in form.lower(),
                    'method': 'POST' if 'method="post"' in form.lower() else 'GET'
                })
            
            return form_info
        except:
            return []
    
    def _analyze_ssl(self, url):
        """Análisis de configuración SSL"""
        if not url.startswith('https://'):
            return {'ssl_enabled': False}
        
        try:
            hostname = urlparse(url).hostname
            context = ssl.create_default_context()
            with socket.create_connection((hostname, 443), timeout=5) as sock:
                with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                    cert = ssock.getpeercert()
                    
                    return {
                        'ssl_enabled': True,
                        'version': ssock.version(),
                        'cipher': ssock.cipher(),
                        'cert_expires': cert.get('notAfter'),
                        'cert_subject': dict(x[0] for x in cert.get('subject', []))
                    }
        except Exception as e:
            return {'ssl_enabled': True, 'error': str(e)}
    
    def _test_sql_injection(self, url, results):
        """Prueba básica de inyección SQL"""
        payloads = ["'", "1' OR '1'='1", "'; DROP TABLE users; --"]
        
        for payload in payloads:
            test_url = f"{url}?id={payload}"
            try:
                response = self.session.get(test_url)
                if any(error in response.text.lower() for error in 
                      ['mysql', 'sql syntax', 'ora-', 'postgresql']):
                    vuln = f"Posible SQLi detectada con payload: {payload}"
                    results['vulnerabilities'].append(vuln)
                    self.logger.log(vuln, "VULN", Colors.RED)
                    break
            except:
                continue
    
    def _test_xss(self, url, results):
        """Prueba básica de XSS"""
        xss_payload = "<script>alert('XSS')</script>"
        test_url = f"{url}?search={xss_payload}"
        
        try:
            response = self.session.get(test_url)
            if xss_payload in response.text:
                vuln = "Posible XSS reflejado detectado"
                results['vulnerabilities'].append(vuln)
                self.logger.log(vuln, "VULN", Colors.RED)
        except:
            pass
    
    def _test_directory_traversal(self, url, results):
        """Prueba de directory traversal"""
        payload = "../../../etc/passwd"
        test_url = f"{url}?file={payload}"
        
        try:
            response = self.session.get(test_url)
            if "root:" in response.text and "/bin/" in response.text:
                vuln = "Posible Directory Traversal detectado"
                results['vulnerabilities'].append(vuln)
                self.logger.log(vuln, "VULN", Colors.RED)
        except:
            pass

class DNSAnalyzer:
    """Analizador DNS avanzado"""
    
    def __init__(self, logger):
        self.logger = logger
    
    def dns_enumeration(self, domain):
        """Enumeración DNS completa"""
        self.logger.log(f"Iniciando enumeración DNS de {domain}", "DNS", Colors.BLUE)
        
        results = {
            'domain': domain,
            'records': {},
            'subdomains': []
        }
        
        record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA', 'CNAME']
        
        for record_type in record_types:
            try:
                answers = dns.resolver.resolve(domain, record_type)
                results['records'][record_type] = [str(rdata) for rdata in answers]
                self.logger.log(f"{record_type}: {len(answers)} registros encontrados", "INFO", Colors.WHITE)
            except:
                continue
        
        # Búsqueda de subdominios
        results['subdomains'] = self._subdomain_enumeration(domain)
        
        return results
    
    def _subdomain_enumeration(self, domain):
        """Enumeración de subdominios"""
        common_subdomains = [
            'www', 'mail', 'ftp', 'admin', 'test', 'dev', 'staging',
            'api', 'app', 'portal', 'secure', 'vpn', 'remote'
        ]
        
        found_subdomains = []
        for subdomain in common_subdomains:
            full_domain = f"{subdomain}.{domain}"
            try:
                dns.resolver.resolve(full_domain, 'A')
                found_subdomains.append(full_domain)
                self.logger.log(f"Subdominio encontrado: {full_domain}", "FOUND", Colors.GREEN)
            except:
                continue
        
        return found_subdomains

class PentestFramework:
    """Framework principal de pentesting"""
    
    def __init__(self, output_file=None):
        self.logger = Logger(output_file)
        self.network_scanner = NetworkScanner(self.logger)
        self.web_scanner = WebScanner(self.logger)
        self.dns_analyzer = DNSAnalyzer(self.logger)
        
        # Banner profesional
        self._print_banner()
    
    def _print_banner(self):
        """Banner del framework"""
        banner = f"""
{Colors.CYAN}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════╗
║                    PENTEST FRAMEWORK v2.0                   ║
║                 Herramienta de Ciberseguridad                ║
║                     Uso Ético Autorizado                    ║
╚══════════════════════════════════════════════════════════════╝
{Colors.END}
        """
        print(banner)
    
    def full_scan(self, target, scan_type="comprehensive"):
        """Escaneo completo del objetivo"""
        self.logger.log(f"Iniciando escaneo completo de {target}", "START", Colors.BOLD)
        
        results = {
            'target': target,
            'timestamp': datetime.now().isoformat(),
            'scan_type': scan_type
        }
        
        # Determinar tipo de objetivo
        if self._is_ip(target):
            results.update(self._scan_ip(target))
        elif self._is_domain(target):
            results.update(self._scan_domain(target))
        elif target.startswith(('http://', 'https://')):
            results.update(self._scan_web(target))
        else:
            self.logger.log(f"Tipo de objetivo no reconocido: {target}", "ERROR", Colors.RED)
            return results
        
        self._generate_report(results)
        return results
    
    def _is_ip(self, target):
        """Verificar si el objetivo es una IP"""
        try:
            ipaddress.ip_address(target)
            return True
        except:
            return False
    
    def _is_domain(self, target):
        """Verificar si el objetivo es un dominio"""
        return '.' in target and not target.startswith(('http://', 'https://'))
    
    def _scan_ip(self, ip):
        """Escaneo específico para IPs"""
        results = {'type': 'ip'}
        
        # Port scan
        open_ports = self.network_scanner.port_scan(ip)
        results['open_ports'] = open_ports
        
        # Service detection
        if open_ports:
            services = self.network_scanner.service_detection(ip, open_ports)
            results['services'] = services
        
        return results
    
    def _scan_domain(self, domain):
        """Escaneo específico para dominios"""
        results = {'type': 'domain'}
        
        # DNS enumeration
        dns_results = self.dns_analyzer.dns_enumeration(domain)
        results['dns'] = dns_results
        
        # Si tiene registro A, escanear la IP
        if 'A' in dns_results.get('records', {}):
            ip = dns_results['records']['A'][0]
            results['ip_scan'] = self._scan_ip(ip)
        
        return results
    
    def _scan_web(self, url):
        """Escaneo específico para sitios web"""
        results = {'type': 'web'}
        
        # Web application scan
        web_results = self.web_scanner.scan_website(url)
        results['web_scan'] = web_results
        
        return results
    
    def _generate_report(self, results):
        """Generar reporte final"""
        self.logger.log("Generando reporte final...", "REPORT", Colors.CYAN)
        
        # Resumen de vulnerabilidades
        vuln_count = 0
        if 'web_scan' in results and 'vulnerabilities' in results['web_scan']:
            vuln_count = len(results['web_scan']['vulnerabilities'])
        
        # Resumen de puertos abiertos
        open_ports_count = 0
        if 'open_ports' in results:
            open_ports_count = len(results['open_ports'])
        elif 'ip_scan' in results and 'open_ports' in results['ip_scan']:
            open_ports_count = len(results['ip_scan']['open_ports'])
        
        self.logger.log(f"RESUMEN DEL ESCANEO:", "SUMMARY", Colors.BOLD)
        self.logger.log(f"- Objetivo: {results['target']}", "INFO", Colors.WHITE)
        self.logger.log(f"- Puertos abiertos: {open_ports_count}", "INFO", Colors.WHITE)
        self.logger.log(f"- Vulnerabilidades detectadas: {vuln_count}", "INFO", Colors.WHITE)
        self.logger.log(f"- Tiempo de escaneo: {datetime.now().isoformat()}", "INFO", Colors.WHITE)

def main():
    """Función principal"""
    parser = argparse.ArgumentParser(
        description="Framework de Pentesting Profesional",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  python pentest.py -t 192.168.1.1          # Escanear IP
  python pentest.py -t google.com            # Escanear dominio
  python pentest.py -t https://example.com   # Escanear web
  python pentest.py -t 192.168.1.0/24 -n    # Ping sweep de red
        """
    )
    
    parser.add_argument('-t', '--target', required=True, help='Objetivo a escanear')
    parser.add_argument('-o', '--output', help='Archivo de salida para el reporte')
    parser.add_argument('-n', '--network', action='store_true', help='Modo network scan')
    parser.add_argument('--threads', type=int, default=50, help='Número de hilos (default: 50)')
    
    args = parser.parse_args()
    
    try:
        # Inicializar framework
        framework = PentestFramework(args.output)
        
        if args.network:
            # Modo network scan
            active_hosts = framework.network_scanner.ping_sweep(args.target)
            for host in active_hosts[:5]:  # Limitar a 5 hosts para demo
                framework.full_scan(host)
        else:
            # Escaneo individual
            framework.full_scan(args.target)
            
        framework.logger.log("Escaneo completado exitosamente", "SUCCESS", Colors.GREEN)
        
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Escaneo interrumpido por el usuario{Colors.END}")
    except Exception as e:
        print(f"{Colors.RED}Error crítico: {e}{Colors.END}")
        sys.exit(1)

if __name__ == "__main__":
    main()
