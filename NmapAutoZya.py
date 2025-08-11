#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import re
import json
import time
from datetime import datetime
import argparse

class Colors:
    """Colores para la interfaz"""
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

class NmapAutomator:
    def __init__(self):
        self.target = ""
        self.output_dir = "nmap_results"
        self.history = []
        self.create_output_directory()
        
    def create_output_directory(self):
        """Crear directorio para resultados"""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def clear_screen(self):
        """Limpiar pantalla"""
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def print_banner(self):
        """Mostrar banner principal"""
        banner = f"""
{Colors.CYAN}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════════════════════╗
║                          NMAP AUTOMATION TOOL                                ║
║                             by Zyanetralys                                   ║
║                            Para Kali Linux                                   ║
╚══════════════════════════════════════════════════════════════════════════════╝
{Colors.END}
{Colors.YELLOW}Target actual: {Colors.WHITE}{self.target if self.target else "No establecido"}{Colors.END}
{Colors.YELLOW}Directorio resultados: {Colors.WHITE}{self.output_dir}{Colors.END}
"""
        print(banner)
    
    def validate_target(self, target):
        """Validar formato de IP o dominio"""
        # Patrón para IP
        ip_pattern = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
        # Patrón para rango CIDR
        cidr_pattern = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\/(?:[0-9]|[1-2][0-9]|3[0-2])$'
        # Patrón básico para dominio
        domain_pattern = r'^[a-zA-Z0-9][a-zA-Z0-9-]{1,61}[a-zA-Z0-9]?\.[a-zA-Z]{2,}$'
        
        return bool(re.match(ip_pattern, target) or 
                   re.match(cidr_pattern, target) or 
                   re.match(domain_pattern, target) or
                   target.count('.') >= 2)
    
    def execute_nmap(self, command, scan_type):
        """Ejecutar comando nmap y guardar resultados"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"{self.output_dir}/{scan_type}_{timestamp}"
        
        # Agregar parámetros de salida
        full_command = f"{command} -oA {output_file}"
        
        print(f"{Colors.GREEN}[INFO]{Colors.END} Ejecutando: {full_command}")
        print(f"{Colors.YELLOW}[INFO]{Colors.END} Guardando resultados en: {output_file}")
        print(f"{Colors.CYAN}{'='*60}{Colors.END}")
        
        try:
            # Ejecutar comando
            process = subprocess.Popen(full_command, shell=True, 
                                     stdout=subprocess.PIPE, 
                                     stderr=subprocess.PIPE,
                                     universal_newlines=True)
            
            # Mostrar progreso en tiempo real
            for line in process.stdout:
                print(line.rstrip())
            
            process.wait()
            
            if process.returncode == 0:
                print(f"{Colors.GREEN}[ÉXITO]{Colors.END} Escaneo completado exitosamente")
                self.history.append({
                    'timestamp': timestamp,
                    'command': full_command,
                    'scan_type': scan_type,
                    'target': self.target,
                    'output_files': [f"{output_file}.nmap", f"{output_file}.xml", f"{output_file}.gnmap"]
                })
            else:
                print(f"{Colors.RED}[ERROR]{Colors.END} Error en el escaneo")
                stderr_output = process.stderr.read()
                if stderr_output:
                    print(f"{Colors.RED}Error details:{Colors.END} {stderr_output}")
                    
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}[INFO]{Colors.END} Escaneo interrumpido por el usuario")
        except Exception as e:
            print(f"{Colors.RED}[ERROR]{Colors.END} Error ejecutando comando: {str(e)}")
        
        input(f"\n{Colors.CYAN}Presiona Enter para continuar...{Colors.END}")
    
    def host_discovery_menu(self):
        """Menú de descubrimiento de hosts"""
        while True:
            self.clear_screen()
            self.print_banner()
            
            menu = f"""
{Colors.BOLD}{Colors.BLUE}╔═══════════════════════════════════════╗
║          DESCUBRIMIENTO DE HOSTS      ║
╚═══════════════════════════════════════╝{Colors.END}

{Colors.GREEN}1.{Colors.END} Ping Scan (descubrir hosts activos)
{Colors.GREEN}2.{Colors.END} Descubrimiento sin ping (-Pn)
{Colors.GREEN}3.{Colors.END} Descubrimiento TCP SYN (-PS)
{Colors.GREEN}4.{Colors.END} Descubrimiento TCP ACK (-PA)
{Colors.GREEN}5.{Colors.END} Descubrimiento UDP (-PU)
{Colors.GREEN}6.{Colors.END} Descubrimiento ARP (-PR)
{Colors.GREEN}7.{Colors.END} Lista de hosts sin escanear (-sL)
{Colors.GREEN}8.{Colors.END} Descubrimiento personalizado

{Colors.RED}0.{Colors.END} Volver al menú principal
"""
            print(menu)
            
            choice = input(f"{Colors.CYAN}Selecciona una opción: {Colors.END}")
            
            if choice == '0':
                break
            elif choice == '1':
                command = f"nmap -sn {self.target}"
                self.execute_nmap(command, "ping_scan")
            elif choice == '2':
                command = f"nmap -sn -Pn {self.target}"
                self.execute_nmap(command, "no_ping_discovery")
            elif choice == '3':
                ports = input(f"{Colors.YELLOW}Puertos para TCP SYN (default 80): {Colors.END}") or "80"
                command = f"nmap -sn -PS{ports} {self.target}"
                self.execute_nmap(command, "tcp_syn_discovery")
            elif choice == '4':
                ports = input(f"{Colors.YELLOW}Puertos para TCP ACK (default 80): {Colors.END}") or "80"
                command = f"nmap -sn -PA{ports} {self.target}"
                self.execute_nmap(command, "tcp_ack_discovery")
            elif choice == '5':
                ports = input(f"{Colors.YELLOW}Puertos para UDP (default 53): {Colors.END}") or "53"
                command = f"nmap -sn -PU{ports} {self.target}"
                self.execute_nmap(command, "udp_discovery")
            elif choice == '6':
                command = f"nmap -sn -PR {self.target}"
                self.execute_nmap(command, "arp_discovery")
            elif choice == '7':
                command = f"nmap -sL {self.target}"
                self.execute_nmap(command, "list_scan")
            elif choice == '8':
                custom_flags = input(f"{Colors.YELLOW}Parámetros personalizados: {Colors.END}")
                command = f"nmap -sn {custom_flags} {self.target}"
                self.execute_nmap(command, "custom_discovery")
    
    def port_scan_menu(self):
        """Menú de escaneo de puertos"""
        while True:
            self.clear_screen()
            self.print_banner()
            
            menu = f"""
{Colors.BOLD}{Colors.BLUE}╔═══════════════════════════════════════╗
║           ESCANEO DE PUERTOS          ║
╚═══════════════════════════════════════╝{Colors.END}

{Colors.GREEN}1.{Colors.END} TCP SYN Scan (stealth)
{Colors.GREEN}2.{Colors.END} TCP Connect Scan
{Colors.GREEN}3.{Colors.END} UDP Scan
{Colors.GREEN}4.{Colors.END} TCP ACK Scan
{Colors.GREEN}5.{Colors.END} TCP Window Scan
{Colors.GREEN}6.{Colors.END} TCP Maimon Scan
{Colors.GREEN}7.{Colors.END} TCP FIN Scan
{Colors.GREEN}8.{Colors.END} TCP XMAS Scan
{Colors.GREEN}9.{Colors.END} TCP Null Scan
{Colors.GREEN}10.{Colors.END} Escaneo de puertos top
{Colors.GREEN}11.{Colors.END} Escaneo personalizado

{Colors.RED}0.{Colors.END} Volver al menú principal
"""
            print(menu)
            
            choice = input(f"{Colors.CYAN}Selecciona una opción: {Colors.END}")
            
            if choice == '0':
                break
            elif choice == '1':
                ports = input(f"{Colors.YELLOW}Rango de puertos (default: top 1000): {Colors.END}") or ""
                port_param = f"-p {ports}" if ports else ""
                command = f"nmap -sS {port_param} {self.target}"
                self.execute_nmap(command, "tcp_syn_scan")
            elif choice == '2':
                ports = input(f"{Colors.YELLOW}Rango de puertos (default: top 1000): {Colors.END}") or ""
                port_param = f"-p {ports}" if ports else ""
                command = f"nmap -sT {port_param} {self.target}"
                self.execute_nmap(command, "tcp_connect_scan")
            elif choice == '3':
                ports = input(f"{Colors.YELLOW}Rango de puertos UDP (default: top 1000): {Colors.END}") or ""
                port_param = f"-p {ports}" if ports else ""
                command = f"nmap -sU {port_param} {self.target}"
                self.execute_nmap(command, "udp_scan")
            elif choice == '4':
                ports = input(f"{Colors.YELLOW}Rango de puertos (default: top 1000): {Colors.END}") or ""
                port_param = f"-p {ports}" if ports else ""
                command = f"nmap -sA {port_param} {self.target}"
                self.execute_nmap(command, "tcp_ack_scan")
            elif choice == '5':
                ports = input(f"{Colors.YELLOW}Rango de puertos (default: top 1000): {Colors.END}") or ""
                port_param = f"-p {ports}" if ports else ""
                command = f"nmap -sW {port_param} {self.target}"
                self.execute_nmap(command, "tcp_window_scan")
            elif choice == '6':
                ports = input(f"{Colors.YELLOW}Rango de puertos (default: top 1000): {Colors.END}") or ""
                port_param = f"-p {ports}" if ports else ""
                command = f"nmap -sM {port_param} {self.target}"
                self.execute_nmap(command, "tcp_maimon_scan")
            elif choice == '7':
                ports = input(f"{Colors.YELLOW}Rango de puertos (default: top 1000): {Colors.END}") or ""
                port_param = f"-p {ports}" if ports else ""
                command = f"nmap -sF {port_param} {self.target}"
                self.execute_nmap(command, "tcp_fin_scan")
            elif choice == '8':
                ports = input(f"{Colors.YELLOW}Rango de puertos (default: top 1000): {Colors.END}") or ""
                port_param = f"-p {ports}" if ports else ""
                command = f"nmap -sX {port_param} {self.target}"
                self.execute_nmap(command, "tcp_xmas_scan")
            elif choice == '9':
                ports = input(f"{Colors.YELLOW}Rango de puertos (default: top 1000): {Colors.END}") or ""
                port_param = f"-p {ports}" if ports else ""
                command = f"nmap -sN {port_param} {self.target}"
                self.execute_nmap(command, "tcp_null_scan")
            elif choice == '10':
                top_num = input(f"{Colors.YELLOW}Número de puertos top (default: 1000): {Colors.END}") or "1000"
                command = f"nmap --top-ports {top_num} {self.target}"
                self.execute_nmap(command, f"top_{top_num}_ports")
            elif choice == '11':
                custom_flags = input(f"{Colors.YELLOW}Parámetros personalizados: {Colors.END}")
                command = f"nmap {custom_flags} {self.target}"
                self.execute_nmap(command, "custom_port_scan")
    
    def service_detection_menu(self):
        """Menú de detección de servicios y OS"""
        while True:
            self.clear_screen()
            self.print_banner()
            
            menu = f"""
{Colors.BOLD}{Colors.BLUE}╔═══════════════════════════════════════╗
║      DETECCIÓN DE SERVICIOS Y OS      ║
╚═══════════════════════════════════════╝{Colors.END}

{Colors.GREEN}1.{Colors.END} Detección de versiones (-sV)
{Colors.GREEN}2.{Colors.END} Detección de OS (-O)
{Colors.GREEN}3.{Colors.END} Detección agresiva (-A)
{Colors.GREEN}4.{Colors.END} Scripts por defecto (-sC)
{Colors.GREEN}5.{Colors.END} Scripts específicos
{Colors.GREEN}6.{Colors.END} Scripts de vulnerabilidades
{Colors.GREEN}7.{Colors.END} Detección de servicios UDP
{Colors.GREEN}8.{Colors.END} Escaneo completo (TCP + UDP + Scripts)

{Colors.RED}0.{Colors.END} Volver al menú principal
"""
            print(menu)
            
            choice = input(f"{Colors.CYAN}Selecciona una opción: {Colors.END}")
            
            if choice == '0':
                break
            elif choice == '1':
                intensity = input(f"{Colors.YELLOW}Intensidad (0-9, default: 1): {Colors.END}") or "1"
                command = f"nmap -sV --version-intensity {intensity} {self.target}"
                self.execute_nmap(command, "version_detection")
            elif choice == '2':
                command = f"nmap -O {self.target}"
                self.execute_nmap(command, "os_detection")
            elif choice == '3':
                command = f"nmap -A {self.target}"
                self.execute_nmap(command, "aggressive_scan")
            elif choice == '4':
                command = f"nmap -sC {self.target}"
                self.execute_nmap(command, "default_scripts")
            elif choice == '5':
                scripts = input(f"{Colors.YELLOW}Scripts específicos (ej: http-enum,ftp-anon): {Colors.END}")
                if scripts:
                    command = f"nmap --script {scripts} {self.target}"
                    self.execute_nmap(command, "custom_scripts")
            elif choice == '6':
                command = f"nmap --script vuln {self.target}"
                self.execute_nmap(command, "vulnerability_scripts")
            elif choice == '7':
                command = f"nmap -sUV --top-ports 100 {self.target}"
                self.execute_nmap(command, "udp_service_detection")
            elif choice == '8':
                ports = input(f"{Colors.YELLOW}Puertos TCP (default: top 1000): {Colors.END}") or "1000"
                udp_ports = input(f"{Colors.YELLOW}Puertos UDP (default: top 100): {Colors.END}") or "100"
                
                if ports == "1000":
                    tcp_param = "--top-ports 1000"
                else:
                    tcp_param = f"-p {ports}"
                    
                command = f"nmap -sS -sU {tcp_param} --top-ports {udp_ports} -sV -sC -O {self.target}"
                self.execute_nmap(command, "complete_scan")
    
    def stealth_evasion_menu(self):
        """Menú de técnicas sigilosas y evasión"""
        while True:
            self.clear_screen()
            self.print_banner()
            
            menu = f"""
{Colors.BOLD}{Colors.BLUE}╔═══════════════════════════════════════╗
║        TÉCNICAS SIGILOSAS Y EVASIÓN   ║
╚═══════════════════════════════════════╝{Colors.END}

{Colors.GREEN}1.{Colors.END} Fragmentación de paquetes
{Colors.GREEN}2.{Colors.END} Decoy scan (señuelos)
{Colors.GREEN}3.{Colors.END} Idle zombie scan
{Colors.GREEN}4.{Colors.END} Source port spoofing
{Colors.GREEN}5.{Colors.END} Data length manipulation
{Colors.GREEN}6.{Colors.END} Timing templates
{Colors.GREEN}7.{Colors.END} MAC address spoofing
{Colors.GREEN}8.{Colors.END} Combinación personalizada

{Colors.RED}0.{Colors.END} Volver al menú principal
"""
            print(menu)
            
            choice = input(f"{Colors.CYAN}Selecciona una opción: {Colors.END}")
            
            if choice == '0':
                break
            elif choice == '1':
                frag_type = input(f"{Colors.YELLOW}Tipo fragmentación (f=simple, ff=tiny): {Colors.END}") or "f"
                command = f"nmap -{frag_type} -sS {self.target}"
                self.execute_nmap(command, "fragmentation_scan")
            elif choice == '2':
                decoys = input(f"{Colors.YELLOW}IPs señuelo (ej: 192.168.1.1,192.168.1.2,ME): {Colors.END}")
                if decoys:
                    command = f"nmap -D {decoys} -sS {self.target}"
                    self.execute_nmap(command, "decoy_scan")
            elif choice == '3':
                zombie_ip = input(f"{Colors.YELLOW}IP del zombie: {Colors.END}")
                if zombie_ip:
                    command = f"nmap -sI {zombie_ip} {self.target}"
                    self.execute_nmap(command, "zombie_scan")
            elif choice == '4':
                source_port = input(f"{Colors.YELLOW}Puerto origen (ej: 53, 80): {Colors.END}")
                if source_port:
                    command = f"nmap --source-port {source_port} -sS {self.target}"
                    self.execute_nmap(command, "source_port_scan")
            elif choice == '5':
                data_length = input(f"{Colors.YELLOW}Longitud de datos adicionales: {Colors.END}")
                if data_length:
                    command = f"nmap --data-length {data_length} -sS {self.target}"
                    self.execute_nmap(command, "data_length_scan")
            elif choice == '6':
                timing_menu = f"""
{Colors.YELLOW}Timing Templates:{Colors.END}
0 - Paranoid (muy lento, para evitar IDS)
1 - Sneaky (lento)
2 - Polite (educado, reduce ancho de banda)
3 - Normal (default)
4 - Aggressive (asume red rápida)
5 - Insane (muy rápido, puede perder precisión)
"""
                print(timing_menu)
                timing = input(f"{Colors.YELLOW}Selecciona timing (0-5): {Colors.END}") or "3"
                command = f"nmap -T{timing} -sS {self.target}"
                self.execute_nmap(command, f"timing_{timing}_scan")
            elif choice == '7':
                mac_addr = input(f"{Colors.YELLOW}MAC address (ej: 00:11:22:33:44:55): {Colors.END}")
                if mac_addr:
                    command = f"nmap --spoof-mac {mac_addr} -sS {self.target}"
                    self.execute_nmap(command, "mac_spoof_scan")
            elif choice == '8':
                print(f"{Colors.YELLOW}Opciones disponibles:{Colors.END}")
                print("- Fragmentación: -f, -ff")
                print("- Decoys: -D IP1,IP2,ME")
                print("- Source port: --source-port PORT")
                print("- Data length: --data-length NUM")
                print("- Timing: -T0 a -T5")
                print("- MAC spoof: --spoof-mac MAC")
                
                custom_evasion = input(f"{Colors.YELLOW}Parámetros de evasión: {Colors.END}")
                if custom_evasion:
                    command = f"nmap {custom_evasion} -sS {self.target}"
                    self.execute_nmap(command, "custom_evasion")
    
    def advanced_techniques_menu(self):
        """Menú de técnicas avanzadas"""
        while True:
            self.clear_screen()
            self.print_banner()
            
            menu = f"""
{Colors.BOLD}{Colors.BLUE}╔═══════════════════════════════════════╗
║         TÉCNICAS AVANZADAS            ║
╚═══════════════════════════════════════╝{Colors.END}

{Colors.GREEN}1.{Colors.END} IPv6 Scanning
{Colors.GREEN}2.{Colors.END} Firewall/IDS Evasion Advanced
{Colors.GREEN}3.{Colors.END} NSE Script Categories
{Colors.GREEN}4.{Colors.END} Custom Protocol Scans
{Colors.GREEN}5.{Colors.END} Performance Optimization
{Colors.GREEN}6.{Colors.END} Output Format Customization
{Colors.GREEN}7.{Colors.END} Target Specification Advanced
{Colors.GREEN}8.{Colors.END} Traceroute Integration

{Colors.RED}0.{Colors.END} Volver al menú principal
"""
            print(menu)
            
            choice = input(f"{Colors.CYAN}Selecciona una opción: {Colors.END}")
            
            if choice == '0':
                break
            elif choice == '1':
                ipv6_target = input(f"{Colors.YELLOW}Target IPv6: {Colors.END}")
                if ipv6_target:
                    command = f"nmap -6 {ipv6_target}"
                    self.execute_nmap(command, "ipv6_scan")
            elif choice == '2':
                print(f"{Colors.YELLOW}Técnicas avanzadas de evasión:{Colors.END}")
                print("1. Bad checksum")
                print("2. Invalid flags")
                print("3. Custom payloads")
                
                evasion_choice = input(f"{Colors.CYAN}Selecciona técnica (1-3): {Colors.END}")
                if evasion_choice == '1':
                    command = f"nmap --badsum -sS {self.target}"
                    self.execute_nmap(command, "badsum_scan")
                elif evasion_choice == '2':
                    command = f"nmap --scanflags URGACKPSHRSTSYNFIN -sS {self.target}"
                    self.execute_nmap(command, "custom_flags_scan")
                elif evasion_choice == '3':
                    payload = input(f"{Colors.YELLOW}Custom payload (hex): {Colors.END}")
                    if payload:
                        command = f"nmap --data {payload} -sS {self.target}"
                        self.execute_nmap(command, "custom_payload_scan")
                        
            elif choice == '3':
                categories = [
                    "auth", "broadcast", "brute", "default", "discovery",
                    "dos", "exploit", "external", "fuzzer", "intrusive",
                    "malware", "safe", "version", "vuln"
                ]
                
                print(f"{Colors.YELLOW}Categorías de scripts NSE:{Colors.END}")
                for i, cat in enumerate(categories, 1):
                    print(f"{i}. {cat}")
                
                cat_choice = input(f"{Colors.YELLOW}Selecciona categoría (nombre): {Colors.END}")
                if cat_choice in categories:
                    command = f"nmap --script {cat_choice} {self.target}"
                    self.execute_nmap(command, f"nse_{cat_choice}_scripts")
                    
            elif choice == '4':
                protocols = ["tcp", "udp", "sctp", "ip"]
                print(f"{Colors.YELLOW}Protocolos disponibles:{Colors.END}")
                for i, proto in enumerate(protocols, 1):
                    print(f"{i}. {proto}")
                    
                proto_choice = input(f"{Colors.YELLOW}Protocolo: {Colors.END}")
                if proto_choice in protocols:
                    if proto_choice == "sctp":
                        command = f"nmap -sY {self.target}"
                    elif proto_choice == "ip":
                        command = f"nmap -sO {self.target}"
                    else:
                        command = f"nmap -s{proto_choice[0].upper()} {self.target}"
                    
                    self.execute_nmap(command, f"{proto_choice}_protocol_scan")
                    
            elif choice == '5':
                print(f"{Colors.YELLOW}Optimizaciones de rendimiento:{Colors.END}")
                print("1. Paralelización de hosts")
                print("2. Control de velocidad de envío")
                print("3. Timeouts personalizados")
                print("4. Número de reintentos")
                
                perf_choice = input(f"{Colors.CYAN}Selecciona opción (1-4): {Colors.END}")
                
                if perf_choice == '1':
                    parallelism = input(f"{Colors.YELLOW}Hosts en paralelo (default: auto): {Colors.END}") or "auto"
                    if parallelism != "auto":
                        command = f"nmap --min-hostgroup {parallelism} --max-hostgroup {parallelism} {self.target}"
                    else:
                        command = f"nmap {self.target}"
                elif perf_choice == '2':
                    rate = input(f"{Colors.YELLOW}Paquetes por segundo: {Colors.END}")
                    if rate:
                        command = f"nmap --max-rate {rate} {self.target}"
                        self.execute_nmap(command, f"rate_limited_{rate}_scan")
                elif perf_choice == '3':
                    timeout = input(f"{Colors.YELLOW}Timeout en ms (default: auto): {Colors.END}")
                    if timeout:
                        command = f"nmap --host-timeout {timeout}ms {self.target}"
                        self.execute_nmap(command, f"timeout_{timeout}ms_scan")
                elif perf_choice == '4':
                    retries = input(f"{Colors.YELLOW}Número de reintentos (default: 1): {Colors.END}") or "1"
                    command = f"nmap --max-retries {retries} {self.target}"
                    self.execute_nmap(command, f"retries_{retries}_scan")
                    
            elif choice == '6':
                print(f"{Colors.YELLOW}Formatos de salida disponibles:{Colors.END}")
                print("1. Normal (-oN)")
                print("2. XML (-oX)")
                print("3. Grepable (-oG)")
                print("4. Todos los formatos (-oA)")
                print("5. Script kiddie (-oS)")
                
                format_choice = input(f"{Colors.CYAN}Formato adicional (1-5): {Colors.END}")
                scan_type = input(f"{Colors.YELLOW}Tipo de escaneo básico (-sS, -sT, etc): {Colors.END}") or "S"
                
                format_map = {"1": "N", "2": "X", "3": "G", "4": "A", "5": "S"}
                if format_choice in format_map:
                    fmt = format_map[format_choice]
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    if fmt == "A":
                        command = f"nmap -s{scan_type} -oA {self.output_dir}/custom_format_{timestamp} {self.target}"
                    else:
                        command = f"nmap -s{scan_type} -o{fmt} {self.output_dir}/custom_format_{timestamp}.{fmt.lower()} {self.target}"
                    
                    print(f"{Colors.GREEN}[INFO]{Colors.END} Ejecutando: {command}")
                    subprocess.run(command, shell=True)
                    
            elif choice == '7':
                print(f"{Colors.YELLOW}Especificaciones avanzadas de target:{Colors.END}")
                print("1. Lista desde archivo")
                print("2. Exclusión de hosts")
                print("3. Randomización de targets")
                print("4. Input desde stdin")
                
                target_choice = input(f"{Colors.CYAN}Selecciona opción (1-4): {Colors.END}")
                
                if target_choice == '1':
                    file_path = input(f"{Colors.YELLOW}Archivo con lista de targets: {Colors.END}")
                    if os.path.exists(file_path):
                        command = f"nmap -iL {file_path}"
                        self.execute_nmap(command, "file_input_scan")
                elif target_choice == '2':
                    exclude = input(f"{Colors.YELLOW}Hosts a excluir: {Colors.END}")
                    if exclude:
                        command = f"nmap --exclude {exclude} {self.target}"
                        self.execute_nmap(command, "exclude_hosts_scan")
                elif target_choice == '3':
                    command = f"nmap --randomize-hosts {self.target}"
                    self.execute_nmap(command, "randomized_scan")
                    
            elif choice == '8':
                print(f"{Colors.YELLOW}Opciones de traceroute:{Colors.END}")
                print("1. Traceroute básico")
                print("2. Traceroute con puertos específicos")
                
                trace_choice = input(f"{Colors.CYAN}Selecciona opción (1-2): {Colors.END}")
                
                if trace_choice == '1':
                    command = f"nmap --traceroute {self.target}"
                    self.execute_nmap(command, "traceroute_scan")
                elif trace_choice == '2':
                    port = input(f"{Colors.YELLOW}Puerto para traceroute: {Colors.END}")
                    if port:
                        command = f"nmap --traceroute -p {port} {self.target}"
                        self.execute_nmap(command, f"traceroute_port_{port}_scan")
    
    def view_history(self):
        """Ver historial de escaneos"""
        self.clear_screen()
        self.print_banner()
        
        if not self.history:
            print(f"{Colors.YELLOW}[INFO]{Colors.END} No hay historial de escaneos")
            input(f"\n{Colors.CYAN}Presiona Enter para continuar...{Colors.END}")
            return
        
        print(f"{Colors.BOLD}{Colors.BLUE}╔═══════════════════════════════════════╗")
        print(f"║            HISTORIAL DE ESCANEOS      ║")
        print(f"╚═══════════════════════════════════════╝{Colors.END}\n")
        
        for i, scan in enumerate(self.history, 1):
            print(f"{Colors.GREEN}{i}.{Colors.END} {Colors.BOLD}{scan['scan_type']}{Colors.END}")
            print(f"   Target: {scan['target']}")
            print(f"   Timestamp: {scan['timestamp']}")
            print(f"   Comando: {scan['command']}")
            print(f"   Archivos: {', '.join(scan['output_files'])}")
            print()
        
        choice = input(f"{Colors.CYAN}Ver detalles de escaneo (número) o Enter para volver: {Colors.END}")
        
        if choice.isdigit() and 1 <= int(choice) <= len(self.history):
            scan = self.history[int(choice) - 1]
            self.view_scan_details(scan)
    
    def view_scan_details(self, scan):
        """Ver detalles de un escaneo específico"""
        self.clear_screen()
        self.print_banner()
        
        print(f"{Colors.BOLD}{Colors.BLUE}╔═══════════════════════════════════════╗")
        print(f"║           DETALLES DEL ESCANEO        ║")
        print(f"╚═══════════════════════════════════════╝{Colors.END}\n")
        
        print(f"{Colors.BOLD}Tipo de escaneo:{Colors.END} {scan['scan_type']}")
        print(f"{Colors.BOLD}Target:{Colors.END} {scan['target']}")
        print(f"{Colors.BOLD}Timestamp:{Colors.END} {scan['timestamp']}")
        print(f"{Colors.BOLD}Comando ejecutado:{Colors.END} {scan['command']}\n")
        
        # Mostrar contenido de archivos si existen
        for file_path in scan['output_files']:
            if os.path.exists(file_path):
                print(f"{Colors.YELLOW}═══ Contenido de {file_path} ═══{Colors.END}")
                try:
                    with open(file_path, 'r') as f:
                        content = f.read()
                        # Mostrar solo las primeras 50 líneas para no saturar
                        lines = content.split('\n')[:50]
                        for line in lines:
                            print(line)
                        
                        if len(content.split('\n')) > 50:
                            print(f"\n{Colors.YELLOW}... (archivo truncado, ver archivo completo en {file_path}){Colors.END}")
                        print()
                except Exception as e:
                    print(f"{Colors.RED}Error leyendo archivo: {str(e)}{Colors.END}")
            else:
                print(f"{Colors.RED}Archivo no encontrado: {file_path}{Colors.END}")
        
        input(f"\n{Colors.CYAN}Presiona Enter para continuar...{Colors.END}")
    
    def manage_targets(self):
        """Gestionar targets y configuración"""
        while True:
            self.clear_screen()
            self.print_banner()
            
            menu = f"""
{Colors.BOLD}{Colors.BLUE}╔═══════════════════════════════════════╗
║         GESTIÓN DE TARGETS            ║
╚═══════════════════════════════════════╝{Colors.END}

{Colors.GREEN}1.{Colors.END} Establecer nuevo target
{Colors.GREEN}2.{Colors.END} Validar target actual
{Colors.GREEN}3.{Colors.END} Cambiar directorio de salida
{Colors.GREEN}4.{Colors.END} Limpiar historial
{Colors.GREEN}5.{Colors.END} Exportar historial
{Colors.GREEN}6.{Colors.END} Importar lista de targets
{Colors.GREEN}7.{Colors.END} Verificar conectividad
{Colors.GREEN}8.{Colors.END} Información del sistema

{Colors.RED}0.{Colors.END} Volver al menú principal
"""
            print(menu)
            
            choice = input(f"{Colors.CYAN}Selecciona una opción: {Colors.END}")
            
            if choice == '0':
                break
            elif choice == '1':
                new_target = input(f"{Colors.YELLOW}Introduce el nuevo target (IP/dominio/CIDR): {Colors.END}")
                if self.validate_target(new_target):
                    self.target = new_target
                    print(f"{Colors.GREEN}[ÉXITO]{Colors.END} Target establecido: {new_target}")
                else:
                    print(f"{Colors.RED}[ERROR]{Colors.END} Formato de target inválido")
                input(f"\n{Colors.CYAN}Presiona Enter para continuar...{Colors.END}")
                
            elif choice == '2':
                if self.target:
                    print(f"{Colors.YELLOW}[INFO]{Colors.END} Validando target: {self.target}")
                    if self.validate_target(self.target):
                        print(f"{Colors.GREEN}[ÉXITO]{Colors.END} Target válido")
                        
                        # Ping test
                        try:
                            result = subprocess.run(['ping', '-c', '1', self.target], 
                                                  capture_output=True, text=True, timeout=5)
                            if result.returncode == 0:
                                print(f"{Colors.GREEN}[CONECTIVIDAD]{Colors.END} Target responde a ping")
                            else:
                                print(f"{Colors.YELLOW}[ADVERTENCIA]{Colors.END} Target no responde a ping (puede estar filtrado)")
                        except:
                            print(f"{Colors.YELLOW}[ADVERTENCIA]{Colors.END} No se pudo verificar conectividad")
                    else:
                        print(f"{Colors.RED}[ERROR]{Colors.END} Target inválido")
                else:
                    print(f"{Colors.RED}[ERROR]{Colors.END} No hay target establecido")
                input(f"\n{Colors.CYAN}Presiona Enter para continuar...{Colors.END}")
                
            elif choice == '3':
                new_dir = input(f"{Colors.YELLOW}Nuevo directorio de salida: {Colors.END}")
                if new_dir:
                    self.output_dir = new_dir
                    self.create_output_directory()
                    print(f"{Colors.GREEN}[ÉXITO]{Colors.END} Directorio cambiado a: {new_dir}")
                input(f"\n{Colors.CYAN}Presiona Enter para continuar...{Colors.END}")
                
            elif choice == '4':
                confirm = input(f"{Colors.RED}¿Limpiar todo el historial? (s/N): {Colors.END}")
                if confirm.lower() == 's':
                    self.history.clear()
                    print(f"{Colors.GREEN}[ÉXITO]{Colors.END} Historial limpiado")
                input(f"\n{Colors.CYAN}Presiona Enter para continuar...{Colors.END}")
                
            elif choice == '5':
                if self.history:
                    filename = f"nmap_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                    try:
                        with open(filename, 'w') as f:
                            json.dump(self.history, f, indent=2)
                        print(f"{Colors.GREEN}[ÉXITO]{Colors.END} Historial exportado a: {filename}")
                    except Exception as e:
                        print(f"{Colors.RED}[ERROR]{Colors.END} Error exportando: {str(e)}")
                else:
                    print(f"{Colors.YELLOW}[INFO]{Colors.END} No hay historial para exportar")
                input(f"\n{Colors.CYAN}Presiona Enter para continuar...{Colors.END}")
                
            elif choice == '6':
                file_path = input(f"{Colors.YELLOW}Archivo con lista de targets: {Colors.END}")
                if os.path.exists(file_path):
                    try:
                        with open(file_path, 'r') as f:
                            targets = [line.strip() for line in f if line.strip()]
                        print(f"{Colors.GREEN}[ÉXITO]{Colors.END} {len(targets)} targets cargados:")
                        for i, target in enumerate(targets[:10], 1):  # Mostrar solo los primeros 10
                            print(f"  {i}. {target}")
                        
                        if len(targets) > 10:
                            print(f"  ... y {len(targets) - 10} más")
                            
                        # Guardar lista para uso posterior
                        self.target_list = targets
                        print(f"\n{Colors.YELLOW}[INFO]{Colors.END} Lista guardada. Usar en 'Técnicas Avanzadas' -> 'Target Specification Advanced'")
                    except Exception as e:
                        print(f"{Colors.RED}[ERROR]{Colors.END} Error leyendo archivo: {str(e)}")
                else:
                    print(f"{Colors.RED}[ERROR]{Colors.END} Archivo no encontrado")
                input(f"\n{Colors.CYAN}Presiona Enter para continuar...{Colors.END}")
                
            elif choice == '7':
                if self.target:
                    print(f"{Colors.YELLOW}[INFO]{Colors.END} Verificando conectividad con {self.target}...")
                    
                    # Ping test
                    try:
                        print(f"{Colors.CYAN}Ejecutando ping...{Colors.END}")
                        result = subprocess.run(['ping', '-c', '3', self.target], 
                                              capture_output=True, text=True, timeout=10)
                        print(result.stdout)
                        
                        if result.returncode == 0:
                            print(f"{Colors.GREEN}[CONECTIVIDAD]{Colors.END} Ping exitoso")
                        else:
                            print(f"{Colors.YELLOW}[ADVERTENCIA]{Colors.END} Ping falló")
                    except Exception as e:
                        print(f"{Colors.RED}[ERROR]{Colors.END} Error en ping: {str(e)}")
                    
                    # Traceroute
                    try:
                        print(f"\n{Colors.CYAN}Ejecutando traceroute...{Colors.END}")
                        result = subprocess.run(['traceroute', self.target], 
                                              capture_output=True, text=True, timeout=30)
                        print(result.stdout[:1000])  # Limitar salida
                    except:
                        print(f"{Colors.YELLOW}[INFO]{Colors.END} Traceroute no disponible")
                        
                else:
                    print(f"{Colors.RED}[ERROR]{Colors.END} No hay target establecido")
                input(f"\n{Colors.CYAN}Presiona Enter para continuar...{Colors.END}")
                
            elif choice == '8':
                print(f"{Colors.BOLD}{Colors.BLUE}═══ INFORMACIÓN DEL SISTEMA ═══{Colors.END}")
                
                # Verificar nmap
                try:
                    result = subprocess.run(['nmap', '--version'], capture_output=True, text=True)
                    print(f"{Colors.GREEN}✓{Colors.END} Nmap: {result.stdout.split()[1] if result.stdout else 'Instalado'}")
                except:
                    print(f"{Colors.RED}✗{Colors.END} Nmap: No encontrado")
                
                # Sistema operativo
                print(f"{Colors.GREEN}✓{Colors.END} SO: {os.name}")
                
                # Python
                print(f"{Colors.GREEN}✓{Colors.END} Python: {sys.version.split()[0]}")
                
                # Directorio actual
                print(f"{Colors.GREEN}✓{Colors.END} Directorio: {os.getcwd()}")
                
                # Permisos
                if os.geteuid() == 0:
                    print(f"{Colors.GREEN}✓{Colors.END} Permisos: Root (todos los escaneos disponibles)")
                else:
                    print(f"{Colors.YELLOW}⚠{Colors.END} Permisos: Usuario normal (algunos escaneos requieren root)")
                
                input(f"\n{Colors.CYAN}Presiona Enter para continuar...{Colors.END}")
    
    def quick_scan_menu(self):
        """Menú de escaneos rápidos predefinidos"""
        while True:
            self.clear_screen()
            self.print_banner()
            
            menu = f"""
{Colors.BOLD}{Colors.BLUE}╔═══════════════════════════════════════╗
║           ESCANEOS RÁPIDOS            ║
╚═══════════════════════════════════════╝{Colors.END}

{Colors.GREEN}1.{Colors.END} Escaneo básico (top 100 puertos)
{Colors.GREEN}2.{Colors.END} Escaneo rápido con detección de servicios
{Colors.GREEN}3.{Colors.END} Escaneo completo (top 1000 + scripts)
{Colors.GREEN}4.{Colors.END} Escaneo de vulnerabilidades
{Colors.GREEN}5.{Colors.END} Escaneo sigiloso
{Colors.GREEN}6.{Colors.END} Escaneo UDP básico
{Colors.GREEN}7.{Colors.END} Escaneo web (puertos HTTP/HTTPS)
{Colors.GREEN}8.{Colors.END} Escaneo de red local

{Colors.RED}0.{Colors.END} Volver al menú principal
"""
            print(menu)
            
            choice = input(f"{Colors.CYAN}Selecciona una opción: {Colors.END}")
            
            if choice == '0':
                break
            elif choice == '1':
                command = f"nmap --top-ports 100 -T4 {self.target}"
                self.execute_nmap(command, "quick_basic_scan")
            elif choice == '2':
                command = f"nmap --top-ports 1000 -T4 -sV {self.target}"
                self.execute_nmap(command, "quick_service_scan")
            elif choice == '3':
                command = f"nmap --top-ports 1000 -T4 -A {self.target}"
                self.execute_nmap(command, "quick_complete_scan")
            elif choice == '4':
                command = f"nmap --top-ports 1000 -T4 --script vuln {self.target}"
                self.execute_nmap(command, "quick_vuln_scan")
            elif choice == '5':
                command = f"nmap -sS -T2 -f --top-ports 1000 {self.target}"
                self.execute_nmap(command, "quick_stealth_scan")
            elif choice == '6':
                command = f"nmap -sU --top-ports 100 -T4 {self.target}"
                self.execute_nmap(command, "quick_udp_scan")
            elif choice == '7':
                command = f"nmap -p 80,443,8080,8443,8000,8888 -T4 -sV --script http-enum {self.target}"
                self.execute_nmap(command, "quick_web_scan")
            elif choice == '8':
                network = input(f"{Colors.YELLOW}Red local (ej: 192.168.1.0/24): {Colors.END}")
                if network:
                    command = f"nmap -sn -T4 {network}"
                    self.execute_nmap(command, "quick_network_discovery")
    
    def main_menu(self):
        """Menú principal"""
        while True:
            if not self.target:
                self.clear_screen()
                self.print_banner()
                print(f"{Colors.RED}[REQUERIDO]{Colors.END} Primero debes establecer un target")
                target = input(f"{Colors.CYAN}Introduce el target (IP/dominio/CIDR): {Colors.END}")
                
                if not target:
                    print(f"{Colors.RED}[ERROR]{Colors.END} Target requerido para continuar")
                    return
                
                if self.validate_target(target):
                    self.target = target
                    print(f"{Colors.GREEN}[ÉXITO]{Colors.END} Target establecido: {target}")
                    time.sleep(1)
                else:
                    print(f"{Colors.RED}[ERROR]{Colors.END} Formato de target inválido")
                    time.sleep(2)
                    continue
            
            self.clear_screen()
            self.print_banner()
            
            menu = f"""
{Colors.BOLD}{Colors.BLUE}╔═══════════════════════════════════════╗
║              MENÚ PRINCIPAL           ║
╚═══════════════════════════════════════╝{Colors.END}

{Colors.GREEN}1.{Colors.END}  Descubrimiento de Hosts
{Colors.GREEN}2.{Colors.END}  Escaneo de Puertos
{Colors.GREEN}3.{Colors.END}  Detección de Servicios y OS
{Colors.GREEN}4.{Colors.END}  Técnicas Sigilosas y Evasión
{Colors.GREEN}5.{Colors.END}  Técnicas Avanzadas
{Colors.GREEN}6.{Colors.END}  Escaneos Rápidos
{Colors.GREEN}7.{Colors.END}  Ver Historial
{Colors.GREEN}8.{Colors.END}  Gestión de Targets
{Colors.GREEN}9.{Colors.END}  Ayuda y Documentación

{Colors.RED}0.{Colors.END}  Salir
"""
            print(menu)
            
            choice = input(f"{Colors.CYAN}Selecciona una opción: {Colors.END}")
            
            if choice == '0':
                print(f"{Colors.YELLOW}¡Gracias por usar Nmap Automation Tool!{Colors.END}")
                break
            elif choice == '1':
                self.host_discovery_menu()
            elif choice == '2':
                self.port_scan_menu()
            elif choice == '3':
                self.service_detection_menu()
            elif choice == '4':
                self.stealth_evasion_menu()
            elif choice == '5':
                self.advanced_techniques_menu()
            elif choice == '6':
                self.quick_scan_menu()
            elif choice == '7':
                self.view_history()
            elif choice == '8':
                self.manage_targets()
            elif choice == '9':
                self.show_help()
            else:
                print(f"{Colors.RED}[ERROR]{Colors.END} Opción inválida")
                time.sleep(1)
    
    def show_help(self):
        """Mostrar ayuda y documentación"""
        self.clear_screen()
        self.print_banner()
        
        help_text = f"""
{Colors.BOLD}{Colors.BLUE}╔═══════════════════════════════════════╗
║              AYUDA Y DOCUMENTACIÓN    ║
╚═══════════════════════════════════════╝{Colors.END}

{Colors.BOLD}TIPOS DE TARGET:{Colors.END}
• IP única: 192.168.1.1
• Rango CIDR: 192.168.1.0/24
• Dominio: example.com
• Lista: 192.168.1.1,192.168.1.2

{Colors.BOLD}TIPOS DE ESCANEO:{Colors.END}
• {Colors.CYAN}-sS{Colors.END}: TCP SYN (stealth)
• {Colors.CYAN}-sT{Colors.END}: TCP Connect
• {Colors.CYAN}-sU{Colors.END}: UDP
• {Colors.CYAN}-sA{Colors.END}: TCP ACK
• {Colors.CYAN}-sN{Colors.END}: TCP NULL

{Colors.BOLD}DETECCIÓN:{Colors.END}
• {Colors.CYAN}-sV{Colors.END}: Versiones de servicios
• {Colors.CYAN}-O{Colors.END}: Sistema operativo
• {Colors.CYAN}-A{Colors.END}: Agresivo (OS + versión + scripts)
• {Colors.CYAN}-sC{Colors.END}: Scripts por defecto

{Colors.BOLD}EVASIÓN:{Colors.END}
• {Colors.CYAN}-f{Colors.END}: Fragmentar paquetes
• {Colors.CYAN}-D{Colors.END}: Usar señuelos
• {Colors.CYAN}-T0-T5{Colors.END}: Plantillas de tiempo
• {Colors.CYAN}--source-port{Colors.END}: Puerto origen específico

{Colors.BOLD}ARCHIVOS DE SALIDA:{Colors.END}
• {Colors.CYAN}.nmap{Colors.END}: Formato normal
• {Colors.CYAN}.xml{Colors.END}: Formato XML
• {Colors.CYAN}.gnmap{Colors.END}: Formato grepable

{Colors.BOLD}CONSEJOS:{Colors.END}
• Usa sudo para escaneos SYN (-sS)
• -T4 para escaneos rápidos en redes confiables
• -T2 para escaneos sigilosos
• Combina múltiples técnicas para mejores resultados

{Colors.BOLD}EJEMPLOS DE COMANDOS:{Colors.END}
• nmap -sS -T4 --top-ports 1000 -sV target
• nmap -sU --top-ports 100 target
• nmap -A -T4 target
• nmap --script vuln target
"""
        
        print(help_text)
        input(f"\n{Colors.CYAN}Presiona Enter para continuar...{Colors.END}")

def main():
    """Función principal"""
    # Verificar si nmap está instalado
    try:
        subprocess.run(['nmap', '--version'], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print(f"{Colors.RED}[ERROR]{Colors.END} Nmap no está instalado o no está en el PATH")
        print(f"{Colors.YELLOW}[INFO]{Colors.END} En Kali Linux instala con: apt update && apt install nmap")
        return
    
    # Verificar permisos
    if os.geteuid() != 0:
        print(f"{Colors.YELLOW}[ADVERTENCIA]{Colors.END} Ejecutándose sin permisos root")
        print(f"{Colors.YELLOW}[INFO]{Colors.END} Algunos escaneos (como -sS) requieren privilegios root")
        print(f"{Colors.CYAN}[TIP]{Colors.END} Ejecuta con: sudo python3 {sys.argv[0]}")
        print()
        
        confirm = input(f"{Colors.CYAN}¿Continuar de todos modos? (S/n): {Colors.END}")
        if confirm.lower() == 'n':
            return
    
    # Crear y ejecutar la aplicación
    app = NmapAutomator()
    
    try:
        app.main_menu()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}[INFO]{Colors.END} Aplicación terminada por el usuario")
    except Exception as e:
        print(f"\n{Colors.RED}[ERROR CRÍTICO]{Colors.END} {str(e)}")
        print(f"{Colors.YELLOW}[DEBUG]{Colors.END} Contacta al desarrollador si el error persiste")

if __name__ == "__main__":
    # Agregar soporte para argumentos de línea de comandos
    parser = argparse.ArgumentParser(description="Herramienta completa de automatización Nmap")
    parser.add_argument('-t', '--target', help='Target inicial (IP/dominio/CIDR)')
    parser.add_argument('-o', '--output', help='Directorio de salida', default='nmap_results')
    parser.add_argument('--version', action='version', version='Nmap Automation Tool v2.0')
    
    args = parser.parse_args()
    
    # Si se proporciona target por argumentos
    if args.target:
        app = NmapAutomator()
        if app.validate_target(args.target):
            app.target = args.target
        else:
            print(f"{Colors.RED}[ERROR]{Colors.END} Target inválido: {args.target}")
            sys.exit(1)
        
        if args.output:
            app.output_dir = args.output
            app.create_output_directory()
        
        try:
            app.main_menu()
        except KeyboardInterrupt:
            print(f"\n\n{Colors.YELLOW}[INFO]{Colors.END} Aplicación terminada por el usuario")
    else:
        main()
