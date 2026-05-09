#!/usr/bin/env python3
"""
Guía Interactiva CTF - Capture The Flag
Una herramienta educativa para aprender ciberseguridad paso a paso
"""

import os
import sys
import subprocess
import time
import json
import base64
import hashlib
import requests
from urllib.parse import urlparse
import socket

class CTFGuide:
    def __init__(self):
        self.current_step = 0
        self.completed_steps = []
        self.tools_installed = {}
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_header(self):
        print("=" * 60)
        print("🏁 GUÍA INTERACTIVA CTF - CAPTURE THE FLAG 🏁")
        print("=" * 60)
        print()
    
    def print_step(self, step_num, title, description):
        print(f"\n📋 PASO {step_num}: {title}")
        print("-" * 50)
        print(f"📝 {description}")
        print()
    
    def wait_for_user(self):
        input("Presiona Enter para continuar...")
    
    def check_tool_installed(self, tool_name, command):
        """Verifica si una herramienta está instalada"""
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                self.tools_installed[tool_name] = True
                return True
            else:
                self.tools_installed[tool_name] = False
                return False
        except:
            self.tools_installed[tool_name] = False
            return False
    
    def install_tool(self, tool_name, install_command):
        """Instala una herramienta"""
        print(f"🔧 Instalando {tool_name}...")
        print(f"Comando: {install_command}")
        
        choice = input("¿Deseas ejecutar este comando? (s/n): ")
        if choice.lower() == 's':
            try:
                subprocess.run(install_command, shell=True, check=True)
                print(f"✅ {tool_name} instalado correctamente")
                self.tools_installed[tool_name] = True
            except subprocess.CalledProcessError:
                print(f"❌ Error al instalar {tool_name}")
                self.tools_installed[tool_name] = False
        else:
            print(f"⚠️  Instalación de {tool_name} omitida")
    
    def step_1_introduction(self):
        """Introducción a CTF"""
        self.print_step(1, "INTRODUCCIÓN A CTF", 
                       "Los CTF son competencias de ciberseguridad donde resuelves desafíos para encontrar 'flags'")
        
        print("🎯 TIPOS DE CTF:")
        print("• Jeopardy: Categorías independientes (Web, Crypto, Forensics, etc.)")
        print("• Attack/Defense: Equipos atacan y defienden sistemas")
        print("• Mixed: Combinación de ambos tipos")
        print()
        
        print("🏆 CATEGORÍAS PRINCIPALES:")
        categories = {
            "Web": "Vulnerabilidades en aplicaciones web",
            "Cryptography": "Criptografía y cifrado",
            "Forensics": "Análisis forense digital",
            "Binary Exploitation": "Explotación de binarios",
            "Reverse Engineering": "Ingeniería inversa",
            "Steganography": "Información oculta en archivos",
            "Network": "Análisis de tráfico de red",
            "OSINT": "Inteligencia de fuentes abiertas"
        }
        
        for category, description in categories.items():
            print(f"  {category}: {description}")
        
        print()
        self.wait_for_user()
    
    def step_2_environment_setup(self):
        """Configuración del entorno"""
        self.print_step(2, "CONFIGURACIÓN DEL ENTORNO", 
                       "Instalación de herramientas esenciales para CTF")
        
        # Lista de herramientas esenciales
        tools = {
            "nmap": {
                "check": "nmap --version",
                "install": "sudo apt update && sudo apt install nmap",
                "description": "Escáner de puertos y redes"
            },
            "netcat": {
                "check": "nc -h",
                "install": "sudo apt install netcat-traditional",
                "description": "Herramienta de red versátil"
            },
            "curl": {
                "check": "curl --version",
                "install": "sudo apt install curl",
                "description": "Cliente HTTP/HTTPS"
            },
            "wget": {
                "check": "wget --version",
                "install": "sudo apt install wget",
                "description": "Descargador de archivos"
            },
            "john": {
                "check": "john --version",
                "install": "sudo apt install john",
                "description": "Cracker de contraseñas"
            },
            "hashcat": {
                "check": "hashcat --version",
                "install": "sudo apt install hashcat",
                "description": "Cracker de hashes avanzado"
            },
            "binwalk": {
                "check": "binwalk --help",
                "install": "sudo apt install binwalk",
                "description": "Análisis de firmware y archivos"
            },
            "strings": {
                "check": "strings --version",
                "install": "sudo apt install binutils",
                "description": "Extrae strings de archivos binarios"
            },
            "file": {
                "check": "file --version",
                "install": "sudo apt install file",
                "description": "Identifica tipos de archivo"
            },
            "hexdump": {
                "check": "hexdump -C /dev/null",
                "install": "sudo apt install bsdmainutils",
                "description": "Visor hexadecimal"
            }
        }
        
        print("🔍 VERIFICANDO HERRAMIENTAS INSTALADAS:")
        for tool, info in tools.items():
            installed = self.check_tool_installed(tool, info["check"])
            status = "✅" if installed else "❌"
            print(f"{status} {tool}: {info['description']}")
        
        print("\n🛠️  INSTALACIÓN DE HERRAMIENTAS:")
        for tool, info in tools.items():
            if not self.tools_installed.get(tool, False):
                print(f"\n{tool}: {info['description']}")
                choice = input(f"¿Instalar {tool}? (s/n): ")
                if choice.lower() == 's':
                    self.install_tool(tool, info["install"])
        
        print("\n📚 HERRAMIENTAS ADICIONALES RECOMENDADAS:")
        additional_tools = [
            "Burp Suite Community - Proxy web para testing",
            "Wireshark - Análisis de tráfico de red",
            "Ghidra - Ingeniería inversa (NSA)",
            "Volatility - Análisis forense de memoria",
            "Autopsy - Análisis forense digital",
            "Steghide - Esteganografía",
            "Exiftool - Análisis de metadatos"
        ]
        
        for tool in additional_tools:
            print(f"• {tool}")
        
        self.wait_for_user()
    
    def step_3_reconnaissance(self):
        """Técnicas de reconocimiento"""
        self.print_step(3, "RECONOCIMIENTO", 
                       "Técnicas para recopilar información sobre el objetivo")
        
        print("🔍 RECONOCIMIENTO PASIVO:")
        print("• OSINT (Open Source Intelligence)")
        print("• Búsqueda en Google Dorks")
        print("• Análisis de DNS")
        print("• Redes sociales")
        print()
        
        print("🎯 RECONOCIMIENTO ACTIVO:")
        print("• Escaneo de puertos")
        print("• Enumeración de servicios")
        print("• Fingerprinting")
        print()
        
        print("📋 COMANDOS ÚTILES:")
        commands = [
            ("nmap -sS -sV -O target.com", "Escaneo SYN con detección de versiones y OS"),
            ("nmap -sU target.com", "Escaneo UDP"),
            ("nmap --script vuln target.com", "Escaneo de vulnerabilidades"),
            ("dig target.com", "Consulta DNS"),
            ("whois target.com", "Información de dominio"),
            ("curl -I http://target.com", "Headers HTTP"),
            ("nc -nv target.com 80", "Conexión manual con netcat")
        ]
        
        for cmd, desc in commands:
            print(f"  {cmd}")
            print(f"  └─ {desc}")
            print()
        
        # Ejemplo práctico
        print("🧪 EJEMPLO PRÁCTICO:")
        target = input("Ingresa un dominio para analizar (ej: example.com): ")
        if target:
            print(f"\n🔍 Analizando {target}...")
            
            # DNS lookup
            try:
                import socket
                ip = socket.gethostbyname(target)
                print(f"IP: {ip}")
            except:
                print("No se pudo resolver el DNS")
            
            # HTTP headers
            try:
                import requests
                response = requests.head(f"http://{target}", timeout=5)
                print(f"Status: {response.status_code}")
                print("Headers importantes:")
                for header in ['Server', 'X-Powered-By', 'X-Framework']:
                    if header in response.headers:
                        print(f"  {header}: {response.headers[header]}")
            except:
                print("No se pudo conectar via HTTP")
        
        self.wait_for_user()
    
    def step_4_web_challenges(self):
        """Desafíos web"""
        self.print_step(4, "DESAFÍOS WEB", 
                       "Técnicas para explotar vulnerabilidades web")
        
        print("🌐 VULNERABILIDADES WEB COMUNES:")
        vulns = {
            "SQL Injection": "Inyección de código SQL en consultas",
            "XSS": "Cross-Site Scripting",
            "CSRF": "Cross-Site Request Forgery",
            "Directory Traversal": "Acceso a archivos del sistema",
            "Command Injection": "Ejecución de comandos del sistema",
            "File Upload": "Subida de archivos maliciosos",
            "Authentication Bypass": "Saltarse autenticación",
            "Session Hijacking": "Robo de sesiones"
        }
        
        for vuln, desc in vulns.items():
            print(f"• {vuln}: {desc}")
        
        print("\n🛠️  HERRAMIENTAS WEB:")
        print("• curl - Cliente HTTP de línea de comandos")
        print("• Burp Suite - Proxy interceptor")
        print("• sqlmap - Automatización de SQL injection")
        print("• dirb/dirbuster - Búsqueda de directorios")
        print("• nikto - Escáner de vulnerabilidades web")
        print()
        
        print("📋 COMANDOS ÚTILES:")
        web_commands = [
            ("curl -X POST -d 'user=admin&pass=123' http://target.com/login", "POST request"),
            ("curl -H 'Cookie: session=abc123' http://target.com", "Request con cookies"),
            ("curl -A 'Mozilla/5.0' http://target.com", "Cambiar User-Agent"),
            ("sqlmap -u 'http://target.com/page?id=1' --dbs", "SQL injection automatizado"),
            ("dirb http://target.com /usr/share/dirb/wordlists/common.txt", "Búsqueda de directorios"),
            ("nikto -h http://target.com", "Escaneo de vulnerabilidades web")
        ]
        
        for cmd, desc in web_commands:
            print(f"  {cmd}")
            print(f"  └─ {desc}")
            print()
        
        # Ejemplo de SQL injection
        print("🧪 EJEMPLO: SQL INJECTION")
        print("Payload común: ' OR '1'='1' --")
        print("URL: http://target.com/login?user=admin&pass=' OR '1'='1' --")
        print("Resultado: Bypassa la autenticación")
        print()
        
        # Ejemplo de XSS
        print("🧪 EJEMPLO: XSS")
        print("Payload: <script>alert('XSS')</script>")
        print("Contexto: Campo de comentarios o búsqueda")
        print("Resultado: Ejecución de JavaScript")
        
        self.wait_for_user()
    
    def step_5_cryptography(self):
        """Desafíos de criptografía"""
        self.print_step(5, "CRIPTOGRAFÍA", 
                       "Técnicas para resolver desafíos de cifrado")
        
        print("🔐 TIPOS DE CIFRADO:")
        crypto_types = {
            "César": "Rotación de caracteres",
            "Base64": "Codificación de datos",
            "ROT13": "Rotación específica de 13 posiciones",
            "Vigenère": "Cifrado polialfabético",
            "RSA": "Criptografía asimétrica",
            "AES": "Cifrado simétrico avanzado",
            "MD5/SHA": "Funciones hash"
        }
        
        for cipher, desc in crypto_types.items():
            print(f"• {cipher}: {desc}")
        
        print("\n🛠️  HERRAMIENTAS CRYPTO:")
        print("• hashcat - Cracking de hashes")
        print("• john - John the Ripper")
        print("• openssl - Operaciones criptográficas")
        print("• CyberChef - Herramienta web para decodificar")
        print("• hash-identifier - Identificar tipos de hash")
        print()
        
        print("📋 COMANDOS ÚTILES:")
        crypto_commands = [
            ("echo 'dGVzdA==' | base64 -d", "Decodificar Base64"),
            ("echo 'hello' | tr 'a-z' 'n-za-m'", "ROT13 manual"),
            ("hashcat -m 0 hash.txt wordlist.txt", "Crackear MD5"),
            ("john --wordlist=rockyou.txt hash.txt", "Crackear con John"),
            ("openssl enc -aes-256-cbc -d -in file.enc -out file.txt", "Descifrar AES"),
            ("echo -n 'text' | md5sum", "Generar hash MD5"),
            ("echo -n 'text' | sha256sum", "Generar hash SHA256")
        ]
        
        for cmd, desc in crypto_commands:
            print(f"  {cmd}")
            print(f"  └─ {desc}")
            print()
        
        # Ejemplos prácticos
        print("🧪 EJEMPLO PRÁCTICO: CIFRADO CÉSAR")
        text = input("Ingresa texto para cifrar con César (ROT13): ")
        if text:
            # ROT13 implementation
            result = ""
            for char in text:
                if char.isalpha():
                    shift = 13
                    if char.islower():
                        result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                    else:
                        result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                else:
                    result += char
            print(f"Resultado ROT13: {result}")
        
        print("\n🧪 EJEMPLO: BASE64")
        text = input("Ingresa texto para codificar en Base64: ")
        if text:
            import base64
            encoded = base64.b64encode(text.encode()).decode()
            print(f"Base64: {encoded}")
            decoded = base64.b64decode(encoded).decode()
            print(f"Decodificado: {decoded}")
        
        self.wait_for_user()
    
    def step_6_forensics(self):
        """Análisis forense"""
        self.print_step(6, "ANÁLISIS FORENSE", 
                       "Técnicas para analizar archivos y encontrar evidencia")
        
        print("🔍 ANÁLISIS FORENSE:")
        print("• Análisis de archivos")
        print("• Recuperación de datos")
        print("• Análisis de memoria")
        print("• Análisis de red")
        print("• Metadatos")
        print()
        
        print("🛠️  HERRAMIENTAS FORENSES:")
        forensic_tools = [
            "file - Identificar tipo de archivo",
            "strings - Extraer strings de binarios",
            "hexdump - Visualizar contenido hexadecimal",
            "binwalk - Analizar firmware y archivos",
            "exiftool - Análisis de metadatos",
            "steghide - Esteganografía",
            "volatility - Análisis de memoria",
            "autopsy - Suite forense completa"
        ]
        
        for tool in forensic_tools:
            print(f"• {tool}")
        
        print("\n📋 COMANDOS ÚTILES:")
        forensic_commands = [
            ("file archivo.bin", "Identificar tipo de archivo"),
            ("strings archivo.bin | grep flag", "Buscar strings con 'flag'"),
            ("hexdump -C archivo.bin | head -20", "Ver contenido hexadecimal"),
            ("binwalk archivo.bin", "Analizar estructura del archivo"),
            ("exiftool imagen.jpg", "Ver metadatos de imagen"),
            ("steghide info imagen.jpg", "Verificar esteganografía"),
            ("dd if=archivo.bin of=extraido.bin bs=1 skip=1024 count=2048", "Extraer porción de archivo"),
            ("foremost archivo.bin", "Recuperar archivos embedded")
        ]
        
        for cmd, desc in forensic_commands:
            print(f"  {cmd}")
            print(f"  └─ {desc}")
            print()
        
        print("🧪 EJEMPLO: ANÁLISIS DE ARCHIVO")
        print("Supongamos que tienes un archivo sospechoso...")
        print("1. file archivo.bin          # Identificar tipo")
        print("2. strings archivo.bin       # Buscar texto")
        print("3. hexdump -C archivo.bin    # Ver en hexadecimal")
        print("4. binwalk archivo.bin       # Analizar estructura")
        print()
        
        print("🕵️  ESTEGANOGRAFÍA:")
        print("• Información oculta en imágenes")
        print("• LSB (Least Significant Bit)")
        print("• Archivos dentro de archivos")
        print("• Canales de color RGB")
        print()
        
        print("Comandos esteganografía:")
        stego_commands = [
            ("steghide embed -cf imagen.jpg -ef secreto.txt", "Ocultar archivo"),
            ("steghide extract -sf imagen.jpg", "Extraer archivo oculto"),
            ("zsteg imagen.png", "Buscar datos ocultos en PNG"),
            ("stegsolve imagen.jpg", "Análisis visual de esteganografía")
        ]
        
        for cmd, desc in stego_commands:
            print(f"  {cmd}")
            print(f"  └─ {desc}")
        
        self.wait_for_user()
    
    def step_7_network_analysis(self):
        """Análisis de red"""
        self.print_step(7, "ANÁLISIS DE RED", 
                       "Técnicas para analizar tráfico y protocolos de red")
        
        print("🌐 ANÁLISIS DE RED:")
        print("• Captura de paquetes")
        print("• Análisis de protocolos")
        print("• Detección de intrusiones")
        print("• Forense de red")
        print()
        
        print("🛠️  HERRAMIENTAS DE RED:")
        network_tools = [
            "wireshark - Analizador de protocolos gráfico",
            "tcpdump - Captura de paquetes en CLI",
            "nmap - Escáner de redes",
            "netstat - Estadísticas de red",
            "ss - Información de sockets",
            "iftop - Monitor de ancho de banda",
            "ettercap - Suite de seguridad de red"
        ]
        
        for tool in network_tools:
            print(f"• {tool}")
        
        print("\n📋 COMANDOS DE RED:")
        network_commands = [
            ("tcpdump -i eth0 -w captura.pcap", "Capturar tráfico"),
            ("tcpdump -r captura.pcap 'host 192.168.1.1'", "Filtrar por host"),
            ("nmap -sn 192.168.1.0/24", "Escanear red local"),
            ("netstat -tulnp", "Puertos abiertos"),
            ("ss -tulnp", "Sockets activos"),
            ("iftop -i eth0", "Monitor de tráfico"),
            ("tcpdump -r file.pcap -A | grep -i password", "Buscar contraseñas")
        ]
        
        for cmd, desc in network_commands:
            print(f"  {cmd}")
            print(f"  └─ {desc}")
            print()
        
        print("🔍 ANÁLISIS WIRESHARK:")
        print("Filtros útiles:")
        wireshark_filters = [
            "http.request.method == GET",
            "tcp.port == 80",
            "ip.addr == 192.168.1.1",
            "dns.qry.name contains 'evil'",
            "tcp contains 'password'",
            "http.response.code == 200",
            "ftp.request.command == 'PASS'"
        ]
        
        for filter_expr in wireshark_filters:
            print(f"• {filter_expr}")
        
        print("\n🧪 EJEMPLO: ANÁLISIS DE PCAP")
        print("1. Abrir archivo PCAP en Wireshark")
        print("2. Aplicar filtros para encontrar tráfico interesante")
        print("3. Seguir streams TCP/UDP")
        print("4. Exportar objetos (archivos transferidos)")
        print("5. Buscar credenciales en texto plano")
        
        self.wait_for_user()
    
    def step_8_binary_exploitation(self):
        """Explotación de binarios"""
        self.print_step(8, "EXPLOTACIÓN DE BINARIOS", 
                       "Técnicas para explotar vulnerabilidades en programas")
        
        print("💻 EXPLOTACIÓN DE BINARIOS:")
        print("• Buffer overflow")
        print("• Format string bugs")
        print("• Use after free")
        print("• Integer overflow")
        print("• ROP/JOP chains")
        print()
        
        print("🛠️  HERRAMIENTAS BINARIAS:")
        binary_tools = [
            "gdb - Debugger",
            "objdump - Análisis de binarios",
            "readelf - Información de ELF",
            "ltrace - Trace de llamadas a librerías",
            "strace - Trace de system calls",
            "peda - Plugin de GDB",
            "checksec - Verificar protecciones"
        ]
        
        for tool in binary_tools:
            print(f"• {tool}")
        
        print("\n📋 COMANDOS BINARIOS:")
        binary_commands = [
            ("file binario", "Información del ejecutable"),
            ("checksec binario", "Verificar protecciones"),
            ("objdump -d binario", "Desensamblado"),
            ("strings binario", "Strings en el binario"),
            ("ltrace ./binario", "Trace de llamadas"),
            ("strace ./binario", "Trace de syscalls"),
            ("gdb ./binario", "Debugger"),
            ("readelf -h binario", "Header ELF")
        ]
        
        for cmd, desc in binary_commands:
            print(f"  {cmd}")
            print(f"  └─ {desc}")
            print()
        
        print("🔧 COMANDOS GDB:")
        gdb_commands = [
            "run - Ejecutar programa",
            "break main - Breakpoint en main",
            "info registers - Ver registros",
            "x/20x $esp - Examinar stack",
            "disas main - Desensamblar función",
            "continue - Continuar ejecución",
            "step - Paso a paso",
            "print $eax - Valor de registro"
        ]
        
        for cmd in gdb_commands:
            print(f"• {cmd}")
        
        print("\n🧪 EJEMPLO: BUFFER OVERFLOW")
        print("1. Identificar vulnerabilidad")
        print("2. Controlar EIP/RIP")
        print("3. Encontrar offset exacto")
        print("4. Desarrollar exploit")
        print("5. Bypasses de protecciones")
        
        print("\n⚠️  NOTA: Esta es una introducción básica.")
        print("La explotación de binarios requiere conocimientos avanzados.")
        
        self.wait_for_user()
    
    def step_9_osint(self):
        """OSINT - Inteligencia de fuentes abiertas"""
        self.print_step(9, "OSINT - INTELIGENCIA DE FUENTES ABIERTAS", 
                       "Técnicas para recopilar información de fuentes públicas")
        
        print("🔍 OSINT (Open Source Intelligence):")
        print("• Búsqueda en motores de búsqueda")
        print("• Redes sociales")
        print("• Registros públicos")
        print("• Bases de datos")
        print("• Metadatos")
        print()
        
        print("🛠️  HERRAMIENTAS OSINT:")
        osint_tools = [
            "Google Dorking - Búsquedas avanzadas",
            "Shodan - Motor de búsqueda de dispositivos",
            "Maltego - Análisis de vínculos",
            "theHarvester - Recolección de emails",
            "Recon-ng - Framework de reconocimiento",
            "SpiderFoot - Automatización OSINT",
            "Wayback Machine - Versiones históricas"
        ]
        
        for tool in osint_tools:
            print(f"• {tool}")
        
        print("\n📋 GOOGLE DORKS:")
        google_dorks = [
            'site:target.com filetype:pdf',
            'inurl:admin site:target.com',
            'intitle:"index of" site:target.com',
            'cache:target.com',
            '"password" filetype:txt site:target.com',
            'inurl:wp-admin site:target.com',
            'intitle:"login" site:target.com'
        ]
        
        for dork in google_dorks:
            print(f"• {dork}")
        
        print("\n🌐 COMANDOS OSINT:")
        osint_commands = [
            ("theharvester -d target.com -b google", "Buscar emails"),
            ("shodan search 'apache 2.4'", "Buscar servidores Apache"),
            ("whois target.com", "Información de dominio"),
            ("dig target.com any", "Registros DNS"),
            ("nslookup target.com", "Resolución DNS"),
            ("curl -s 'https://crt.sh/?q=target.com&output=json'", "Certificados SSL"),
            ("waybackurls target.com", "URLs históricas")
        ]
        
        for cmd, desc in osint_commands:
            print(f"  {cmd}")
            print(f"  └─ {desc}")
            print()
        
        print("🧪 EJEMPLO: RECONOCIMIENTO DE DOMINIO")
        domain = input("Ingresa un dominio para reconocimiento OSINT: ")
        if domain:
            print(f"\n🔍 Analizando {domain}...")
            
            # Whois lookup
            try:
                result = subprocess.run(f"whois {domain}", 
                                      shell=True, capture_output=True, text=True)
                if result.returncode == 0:
                    lines = result.stdout.split('\n')[:5]
                    for line in lines:
                        if line.strip():
                            print(f"  {line}")
            except:
                print("  No se pudo obtener información whois")
            
            # DNS lookup
            try:
                import socket
                ip = socket.gethostbyname(domain)
                print(f"  IP: {ip}")
            except:
                print("  No se pudo resolver DNS")
        
        print("\n⚠️  ÉTICA EN OSINT:")
        print("• Usar solo fuentes públicas")
        print("• Respetar términos de servicio")
        print("• No realizar actividades ilegales")
        print("• Documentar fuentes")
        
        self.wait_for_user()
    
    def step_10_practice_platforms(self):
        """Plataformas de práctica"""
        self.print_step(10, "PLATAFORMAS DE PRÁCTICA", 
                       "Sitios web y plataformas para practicar CTF")
        
        print("🏆 PLATAFORMAS CTF PERMANENTES:")
        platforms = [
            "OverTheWire - Wargames clásicos",
            "HackTheBox - Máquinas virtuales",
            "TryHackMe - Aprendizaje guiado",
            "VulnHub - VMs descargables",
            "PicoCTF - CTF educativo",
            "CTFtime - Calendario de CTFs",
            "CyberDefenders - Blue team",
            "Root-Me - Múltiples categorías"
        ]
        
        for platform in platforms:
            print(f"• {platform}")
        
        print("\n🎯 SITIOS DE PRÁCTICA ESPECÍFICOS:")
        specific_sites = {
            "Web": ["DVWA", "WebGoat", "bWAPP", "Mutillidae"],
            "Crypto": ["CryptoPals", "MysteryTwister", "CryptoHack"],
            "Forensics": ["Digital Forensics Framework", "Autopsy Cases"],
            "Binary": ["SmashTheStack", "Exploit Education"],
            "Network": ["Malware Traffic Analysis", "PacketTotal"]
        }
        
        for category, sites in specific_sites.items():
            print(f"{category}:")
            for site in sites:
                print(f"  • {site}")
        
        print("\n🏅 COMPETENCIAS CTF FAMOSAS:")
        competitions = [
            "DEFCON CTF - La competencia más prestigiosa",
            "Google CTF - Competencia anual de Google",
            "PlaidCTF - Organizada por PPP",
            "TokyoWesterns CTF - Competencia japonesa",
            "CSAW CTF - Competencia estudiantil",
            "BSides CTF - Competencias locales",
            "Pwn2Own - Competencia de 0-days"
        ]
        
        for comp in competitions:
            print(f"• {comp}")
        
        print("\n📚 RECURSOS DE APRENDIZAJE:")
        resources = [
            "CTF Field Guide - Guía completa",
            "CTF Wiki - Wikipedia de CTF",
            "LiveOverflow YouTube - Videos educativos",
            "IppSec YouTube - Walkthroughs HackTheBox",
            "John Hammond YouTube - CTF writeups",
            "CTFlearn - Plataforma de aprendizaje",
            "Cybrary - Cursos online gratuitos"
        ]
        
        for resource in resources:
            print(f"• {resource}")
        
        print("\n🛠️ DISTRIBUCIONES ESPECIALIZADAS:")
        distributions = [
            "Kali Linux - Distribución de pentesting",
            "Parrot Security OS - Alternativa a Kali",
            "BackBox - Distribución de seguridad",
            "BlackArch - Basada en Arch Linux",
            "Pentoo - Basada en Gentoo",
            "DEFT - Digital Evidence & Forensics Toolkit"
        ]
        
        for distro in distributions:
            print(f"• {distro}")
        
        self.wait_for_user()
    
    def step_11_writeups_documentation(self):
        """Documentación y writeups"""
        self.print_step(11, "WRITEUPS Y DOCUMENTACIÓN", 
                       "Cómo documentar y compartir soluciones de CTF")
        
        print("📝 ESTRUCTURA DE UN WRITEUP:")
        print("1. Título del challenge")
        print("2. Categoría y dificultad")
        print("3. Descripción del problema")
        print("4. Análisis inicial")
        print("5. Proceso de solución")
        print("6. Exploits/scripts utilizados")
        print("7. Flag obtenida")
        print("8. Lecciones aprendidas")
        print()
        
        print("🎯 ELEMENTOS IMPORTANTES:")
        elements = [
            "Screenshots de evidencia",
            "Código fuente de exploits",
            "Comandos ejecutados",
            "Explicación del razonamiento",
            "Referencias útiles",
            "Herramientas utilizadas",
            "Tiempo invertido",
            "Dificultades encontradas"
        ]
        
        for element in elements:
            print(f"• {element}")
        
        print("\n📋 HERRAMIENTAS PARA WRITEUPS:")
        writeup_tools = [
            "Markdown - Formato de texto",
            "GitHub - Repositorio de writeups",
            "Obsidian - Notas interconectadas",
            "Notion - Documentación colaborativa",
            "Jupyter Notebook - Código y documentación",
            "Asciinema - Grabación de terminal",
            "Flameshot - Screenshots",
            "OBS Studio - Grabación de video"
        ]
        
        for tool in writeup_tools:
            print(f"• {tool}")
        
        print("\n🔍 PLANTILLA DE WRITEUP:")
        template = """
# Challenge Name
**Categoría:** Web/Crypto/Forensics/etc.
**Dificultad:** Easy/Medium/Hard
**Puntos:** 100

## Descripción
Descripción del challenge...

## Análisis Inicial
Primeras observaciones...

## Solución
### Paso 1: Reconocimiento
```bash
comando1
comando2
```

### Paso 2: Explotación
```python
# Código del exploit
```

### Paso 3: Obtención del flag
```
flag{ejemplo_flag}
```

## Conclusión
Lecciones aprendidas...

## Referencias
- Link1
- Link2
        """
        
        print(template)
        
        print("\n💡 CONSEJOS PARA WRITEUPS:")
        tips = [
            "Sé claro y conciso",
            "Incluye todos los pasos",
            "Explica el 'por qué', no solo el 'cómo'",
            "Usa formato markdown",
            "Incluye código funcional",
            "Agrega screenshots relevantes",
            "Revisa antes de publicar",
            "Respeta las reglas del CTF"
        ]
        
        for tip in tips:
            print(f"• {tip}")
        
        self.wait_for_user()
    
    def step_12_team_collaboration(self):
        """Colaboración en equipo"""
        self.print_step(12, "COLABORACIÓN EN EQUIPO", 
                       "Estrategias para trabajar efectivamente en equipo")
        
        print("👥 ROLES EN UN EQUIPO CTF:")
        roles = {
            "Web Expert": "Especialista en vulnerabilidades web",
            "Crypto Specialist": "Experto en criptografía",
            "Forensics Analyst": "Analista forense",
            "Binary Exploiter": "Especialista en explotación",
            "Network Analyst": "Experto en redes",
            "OSINT Specialist": "Especialista en inteligencia",
            "Team Leader": "Coordinador del equipo",
            "Generalist": "Conocimientos amplios"
        }
        
        for role, description in roles.items():
            print(f"• {role}: {description}")
        
        print("\n🛠️ HERRAMIENTAS DE COLABORACIÓN:")
        collab_tools = [
            "Discord/Slack - Comunicación en tiempo real",
            "GitHub/GitLab - Compartir código y writeups",
            "Google Docs - Documentación colaborativa",
            "Trello/Notion - Gestión de tareas",
            "Screen sharing - Compartir pantalla",
            "Etherpad - Notas colaborativas",
            "Miro/Mural - Pizarra digital",
            "Zoom/Teams - Videoconferencias"
        ]
        
        for tool in collab_tools:
            print(f"• {tool}")
        
        print("\n📋 ESTRATEGIAS DE EQUIPO:")
        strategies = [
            "Dividir challenges por especialidad",
            "Comunicación constante",
            "Documentar todo el proceso",
            "Rotar entre diferentes challenges",
            "Ayuda mutua en challenges difíciles",
            "Revisión cruzada de soluciones",
            "Gestión del tiempo efectiva",
            "Celebrar los éxitos juntos"
        ]
        
        for strategy in strategies:
            print(f"• {strategy}")
        
        print("\n⏰ GESTIÓN DEL TIEMPO:")
        time_management = [
            "Priorizar challenges por puntos/dificultad",
            "Establecer límites de tiempo por challenge",
            "Alternar entre challenges bloqueados",
            "Aprovechar hints cuando sea necesario",
            "Enfocarse en categorías fuertes",
            "Dejar tiempo para challenges de último minuto",
            "Monitorear el scoreboard regularmente"
        ]
        
        for tip in time_management:
            print(f"• {tip}")
        
        print("\n🎯 COMUNICACIÓN EFECTIVA:")
        communication = [
            "Reportar progreso regularmente",
            "Compartir findings importantes",
            "Pedir ayuda cuando sea necesario",
            "Explicar soluciones al equipo",
            "Usar canales específicos por categoría",
            "Mantener un log de actividades",
            "Celebrar pequeños avances"
        ]
        
        for comm in communication:
            print(f"• {comm}")
        
        self.wait_for_user()
    
    def main_menu(self):
        """Menú principal interactivo"""
        while True:
            self.clear_screen()
            self.print_header()
            
            print("📚 MENÚ PRINCIPAL - GUÍA CTF")
            print("=" * 40)
            
            steps = [
                "1. Introducción a CTF",
                "2. Configuración del Entorno",
                "3. Reconocimiento",
                "4. Desafíos Web",
                "5. Criptografía",
                "6. Análisis Forense",
                "7. Análisis de Red",
                "8. Explotación de Binarios",
                "9. OSINT",
                "10. Plataformas de Práctica",
                "11. Writeups y Documentación",
                "12. Colaboración en Equipo",
                "13. Resumen y Recursos",
                "0. Salir"
            ]
            
            for step in steps:
                status = "✅" if any(str(i) in step for i in self.completed_steps) else "⭕"
                print(f"{status} {step}")
            
            print("\n" + "=" * 40)
            choice = input("Selecciona una opción: ")
            
            if choice == "0":
                print("¡Gracias por usar la guía CTF! 🏁")
                break
            elif choice == "1":
                self.step_1_introduction()
                self.completed_steps.append(1)
            elif choice == "2":
                self.step_2_environment_setup()
                self.completed_steps.append(2)
            elif choice == "3":
                self.step_3_reconnaissance()
                self.completed_steps.append(3)
            elif choice == "4":
                self.step_4_web_challenges()
                self.completed_steps.append(4)
            elif choice == "5":
                self.step_5_cryptography()
                self.completed_steps.append(5)
            elif choice == "6":
                self.step_6_forensics()
                self.completed_steps.append(6)
            elif choice == "7":
                self.step_7_network_analysis()
                self.completed_steps.append(7)
            elif choice == "8":
                self.step_8_binary_exploitation()
                self.completed_steps.append(8)
            elif choice == "9":
                self.step_9_osint()
                self.completed_steps.append(9)
            elif choice == "10":
                self.step_10_practice_platforms()
                self.completed_steps.append(10)
            elif choice == "11":
                self.step_11_writeups_documentation()
                self.completed_steps.append(11)
            elif choice == "12":
                self.step_12_team_collaboration()
                self.completed_steps.append(12)
            elif choice == "13":
                self.step_13_summary()
                self.completed_steps.append(13)
            else:
                print("Opción no válida. Presiona Enter para continuar...")
                input()
    
    def step_13_summary(self):
        """Resumen final y recursos"""
        self.print_step(13, "RESUMEN Y RECURSOS FINALES", 
                       "Resumen de conceptos y recursos adicionales")
        
        print("🎓 RESUMEN DE CONCEPTOS CLAVE:")
        concepts = [
            "CTF = Capture The Flag - Competencias de ciberseguridad",
            "Reconocimiento es el primer paso crucial",
            "Cada categoría requiere herramientas específicas",
            "La práctica constante es esencial",
            "Documentar todo el proceso",
            "Trabajar en equipo multiplica las capacidades",
            "Aprender de writeups de otros",
            "La ética es fundamental en seguridad"
        ]
        
        for concept in concepts:
            print(f"• {concept}")
        
        print("\n🚀 PRÓXIMOS PASOS:")
        next_steps = [
            "Instalar herramientas básicas",
            "Registrarse en plataformas de práctica",
            "Comenzar con challenges fáciles",
            "Unirse a comunidades CTF",
            "Participar en competencias",
            "Crear writeups detallados",
            "Formar o unirse a un equipo",
            "Especializarse en una categoría"
        ]
        
        for step in next_steps:
            print(f"• {step}")
        
        print("\n📚 RECURSOS ADICIONALES:")
        additional_resources = [
            "https://ctftime.org - Calendario de CTFs",
            "https://github.com/apsdehal/awesome-ctf - Lista de recursos",
            "https://trailofbits.github.io/ctf/ - CTF Field Guide",
            "https://ctf101.org - Introducción a CTF",
            "https://picoctf.org - CTF educativo permanente",
            "https://overthewire.org/wargames/ - Wargames clásicos",
            "https://hackthebox.eu - Máquinas virtuales",
            "https://www.vulnhub.com - VMs descargables"
        ]
        
        for resource in additional_resources:
            print(f"• {resource}")
        
        print("\n🏆 COMUNIDADES Y DISCORD:")
        communities = [
            "CTFtime Discord",
            "HackTheBox Discord",
            "TryHackMe Discord",
            "InfoSec Twitter",
            "Reddit r/netsec",
            "Reddit r/AskNetsec",
            "Local BSides chapters",
            "OWASP local chapters"
        ]
        
        for community in communities:
            print(f"• {community}")
        
        print("\n⚡ COMANDOS DE REFERENCIA RÁPIDA:")
        quick_commands = [
            "nmap -sS -sV target.com",
            "curl -I http://target.com",
            "strings archivo.bin | grep flag",
            "file archivo.bin",
            "base64 -d archivo.b64",
            "hashcat -m 0 hash.txt wordlist.txt",
            "tcpdump -i eth0 -w capture.pcap",
            "gdb ./binario"
        ]
        
        for cmd in quick_commands:
            print(f"• {cmd}")
        
        print("\n🎯 MENSAJE FINAL:")
        print("¡Felicidades por completar la guía CTF!")
        print("Recuerda: La ciberseguridad es un campo en constante evolución.")
        print("Mantente actualizado, practica regularmente y diviértete aprendiendo.")
        print("¡Buena suerte en tus futuras competencias CTF! 🚀")
        
        self.wait_for_user()

def main():
    """Función principal"""
    guide = CTFGuide()
    
    print("🏁 Bienvenido a la Guía Interactiva CTF")
    print("Esta guía te ayudará a aprender Capture The Flag paso a paso")
    print()
    
    choice = input("¿Deseas comenzar el tutorial interactivo? (s/n): ")
    
    if choice.lower() == 's':
        guide.main_menu()
    else:
        print("¡Gracias por usar la guía CTF!")
        print("Ejecuta el programa nuevamente cuando quieras aprender CTF.")

if __name__ == "__main__":
    main()
