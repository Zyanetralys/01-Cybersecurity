#!/usr/bin/env python3
"""
Guía Interactiva para Resolver CTFs
Metodologías y técnicas paso a paso para diferentes categorías de CTF
"""

import os
import sys
import time
import random
from enum import Enum
from typing import Dict, List, Optional

class CTFCategory(Enum):
    WEB = "Web Exploitation"
    CRYPTO = "Cryptography"
    REVERSE = "Reverse Engineering"
    FORENSICS = "Digital Forensics"
    PWNING = "Binary Exploitation"
    STEGANOGRAPHY = "Steganography"
    MISC = "Miscellaneous"
    OSINT = "Open Source Intelligence"

class CTFSolverGuide:
    def __init__(self):
        self.current_session = None
        self.methodology_progress = {}
        
    def show_banner(self):
        """Muestra el banner de la aplicación"""
        print("\n" + "="*70)
        print("🎯 GUÍA INTERACTIVA PARA RESOLVER CTFs 🎯")
        print("="*70)
        print("Aprende metodologías y técnicas paso a paso")
        print("="*70 + "\n")
    
    def show_main_menu(self):
        """Muestra el menú principal"""
        print("\n🚀 MENÚ PRINCIPAL")
        print("-" * 40)
        print("1. 🌐 Web Exploitation")
        print("2. 🔐 Cryptography")
        print("3. 🔄 Reverse Engineering")
        print("4. 🔍 Digital Forensics")
        print("5. 💥 Binary Exploitation")
        print("6. 🖼️  Steganography")
        print("7. 🌍 OSINT")
        print("8. 📦 Miscellaneous")
        print("9. 🎓 Tips generales")
        print("10. 🛠️ Herramientas recomendadas")
        print("0. Salir")
        print("-" * 40)
    
    def web_exploitation_guide(self):
        """Guía para Web Exploitation"""
        print("\n🌐 GUÍA: WEB EXPLOITATION")
        print("="*50)
        
        methodology = [
            {
                "step": 1,
                "title": "Reconocimiento inicial",
                "description": "Analiza la aplicación web objetivo",
                "actions": [
                    "Examina el código fuente (Ctrl+U)",
                    "Busca comentarios HTML <!-- -->",
                    "Revisa archivos JavaScript",
                    "Inspecciona elementos (F12)",
                    "Busca archivos robots.txt, sitemap.xml"
                ],
                "tools": ["Navegador", "Burp Suite", "OWASP ZAP"],
                "tips": [
                    "Siempre mira el código fuente primero",
                    "Los desarrolladores a veces dejan pistas en comentarios",
                    "Revisa las rutas de archivos CSS/JS"
                ]
            },
            {
                "step": 2,
                "title": "Enumeración de directorios",
                "description": "Busca archivos y directorios ocultos",
                "actions": [
                    "Usa herramientas de fuzzing de directorios",
                    "Busca archivos de backup (.bak, .old, ~)",
                    "Prueba rutas comunes (/admin, /login, /config)",
                    "Enumera parámetros GET/POST"
                ],
                "tools": ["gobuster", "dirbuster", "ffuf", "wfuzz"],
                "commands": [
                    "gobuster dir -u http://target.com -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt",
                    "ffuf -w wordlist.txt -u http://target.com/FUZZ",
                    "wfuzz -c -z file,wordlist.txt --hc 404 http://target.com/FUZZ"
                ]
            },
            {
                "step": 3,
                "title": "Identificación de vulnerabilidades",
                "description": "Busca vulnerabilidades web comunes",
                "actions": [
                    "Testa SQL Injection en formularios",
                    "Busca XSS (Cross-Site Scripting)",
                    "Verifica CSRF (Cross-Site Request Forgery)",
                    "Prueba Local/Remote File Inclusion",
                    "Testa Command Injection"
                ],
                "payloads": {
                    "SQL Injection": ["' OR '1'='1", "' UNION SELECT null--", "'; DROP TABLE users;--"],
                    "XSS": ["<script>alert('XSS')</script>", "<img src=x onerror=alert('XSS')>"],
                    "Command Injection": ["; ls", "| whoami", "&& cat /etc/passwd"]
                }
            },
            {
                "step": 4,
                "title": "Explotación",
                "description": "Explota las vulnerabilidades encontradas",
                "actions": [
                    "Desarrolla el payload específico",
                    "Usa herramientas especializadas",
                    "Automatiza con scripts si es necesario",
                    "Extrae información sensible"
                ],
                "tools": ["sqlmap", "Burp Suite", "scripts personalizados"]
            }
        ]
        
        self.show_methodology(methodology)
    
    def crypto_guide(self):
        """Guía para Cryptography"""
        print("\n🔐 GUÍA: CRYPTOGRAPHY")
        print("="*50)
        
        methodology = [
            {
                "step": 1,
                "title": "Análisis del texto cifrado",
                "description": "Identifica el tipo de cifrado",
                "actions": [
                    "Examina la longitud del texto",
                    "Busca patrones en caracteres",
                    "Identifica el conjunto de caracteres usado",
                    "Verifica si es hexadecimal, base64, etc."
                ],
                "tools": ["CyberChef", "dcode.fr", "Cryptii"],
                "tips": [
                    "Base64 termina con = o ==",
                    "Hexadecimal solo usa 0-9 y A-F",
                    "ROT13 mantiene espacios y puntuación"
                ]
            },
            {
                "step": 2,
                "title": "Identificación del cifrado",
                "description": "Determina el algoritmo específico",
                "actions": [
                    "Usa herramientas de identificación automática",
                    "Prueba cifrados clásicos (César, Vigenère)",
                    "Verifica cifrados modernos (AES, RSA)",
                    "Busca pistas en la descripción del reto"
                ],
                "common_ciphers": [
                    "César (ROT13, ROT47)",
                    "Vigenère",
                    "Atbash",
                    "Base64/Base32",
                    "Morse Code",
                    "Binary/ASCII"
                ]
            },
            {
                "step": 3,
                "title": "Análisis criptográfico",
                "description": "Busca debilidades en la implementación",
                "actions": [
                    "Análisis de frecuencia de caracteres",
                    "Busca claves débiles o reutilizadas",
                    "Identifica patrones en el cifrado",
                    "Verifica la entropía del texto"
                ],
                "techniques": [
                    "Frequency analysis",
                    "Kasiski examination",
                    "Index of coincidence",
                    "Brute force de claves cortas"
                ]
            },
            {
                "step": 4,
                "title": "Descifrado",
                "description": "Obtén el texto en claro",
                "actions": [
                    "Aplica la técnica de descifrado apropiada",
                    "Verifica si el resultado tiene sentido",
                    "Busca la flag en el texto descifrado",
                    "Prueba diferentes configuraciones si es necesario"
                ],
                "tools": ["John the Ripper", "Hashcat", "Custom scripts"]
            }
        ]
        
        self.show_methodology(methodology)
    
    def reverse_engineering_guide(self):
        """Guía para Reverse Engineering"""
        print("\n🔄 GUÍA: REVERSE ENGINEERING")
        print("="*50)
        
        methodology = [
            {
                "step": 1,
                "title": "Análisis estático básico",
                "description": "Examina el binario sin ejecutarlo",
                "actions": [
                    "Verifica el tipo de archivo (file comando)",
                    "Examina strings legibles",
                    "Analiza imports/exports",
                    "Identifica la arquitectura y sistema"
                ],
                "tools": ["file", "strings", "objdump", "readelf", "nm"],
                "commands": [
                    "file binary_name",
                    "strings binary_name | grep -i flag",
                    "objdump -d binary_name",
                    "readelf -h binary_name"
                ]
            },
            {
                "step": 2,
                "title": "Análisis dinámico",
                "description": "Ejecuta y monitorea el comportamiento",
                "actions": [
                    "Ejecuta en entorno controlado",
                    "Monitorea llamadas al sistema",
                    "Rastrea flujo de ejecución",
                    "Analiza interacciones con archivos/red"
                ],
                "tools": ["strace", "ltrace", "gdb", "radare2"],
                "commands": [
                    "strace ./binary_name",
                    "ltrace ./binary_name",
                    "gdb ./binary_name"
                ]
            },
            {
                "step": 3,
                "title": "Desensamblado y análisis",
                "description": "Examina el código ensamblador",
                "actions": [
                    "Desensambla funciones clave",
                    "Identifica el flujo de control",
                    "Busca comparaciones y validaciones",
                    "Encuentra la lógica de verificación"
                ],
                "tools": ["IDA Pro", "Ghidra", "radare2", "Binary Ninja"],
                "focus_areas": [
                    "Función main()",
                    "Funciones de validación",
                    "Comparaciones de strings",
                    "Saltos condicionales"
                ]
            },
            {
                "step": 4,
                "title": "Explotación/Bypass",
                "description": "Bypasea la protección o extrae la flag",
                "actions": [
                    "Modifica el binario si es necesario",
                    "Parchea validaciones",
                    "Extrae algoritmos de verificación",
                    "Reconstruye la lógica original"
                ],
                "techniques": [
                    "Binary patching",
                    "Algorithm reconstruction",
                    "Input manipulation",
                    "Memory dumping"
                ]
            }
        ]
        
        self.show_methodology(methodology)
    
    def forensics_guide(self):
        """Guía para Digital Forensics"""
        print("\n🔍 GUÍA: DIGITAL FORENSICS")
        print("="*50)
        
        methodology = [
            {
                "step": 1,
                "title": "Análisis inicial del archivo",
                "description": "Examina la evidencia digital",
                "actions": [
                    "Verifica la integridad (hash MD5/SHA)",
                    "Identifica el tipo de archivo",
                    "Examina metadatos",
                    "Busca archivos ocultos o eliminados"
                ],
                "tools": ["file", "exiftool", "binwalk", "foremost"],
                "commands": [
                    "file evidence_file",
                    "exiftool evidence_file",
                    "binwalk evidence_file",
                    "foremost evidence_file"
                ]
            },
            {
                "step": 2,
                "title": "Recuperación de datos",
                "description": "Extrae información oculta o eliminada",
                "actions": [
                    "Busca archivos eliminados",
                    "Extrae datos de slack space",
                    "Recupera particiones perdidas",
                    "Analiza journaling del sistema"
                ],
                "tools": ["PhotoRec", "TestDisk", "Scalpel", "Volatility"],
                "focus_areas": [
                    "Archivos eliminados",
                    "Metadatos EXIF",
                    "Archivos temporales",
                    "Logs del sistema"
                ]
            },
            {
                "step": 3,
                "title": "Análisis de memoria",
                "description": "Examina dumps de memoria RAM",
                "actions": [
                    "Identifica el perfil del sistema",
                    "Lista procesos activos",
                    "Examina conexiones de red",
                    "Extrae passwords y keys"
                ],
                "tools": ["Volatility", "Rekall", "MemProcFS"],
                "commands": [
                    "volatility -f memory.dmp imageinfo",
                    "volatility -f memory.dmp --profile=Win7SP1x64 pslist",
                    "volatility -f memory.dmp --profile=Win7SP1x64 netscan"
                ]
            },
            {
                "step": 4,
                "title": "Análisis de red y logs",
                "description": "Examina tráfico de red y logs",
                "actions": [
                    "Analiza capturas de paquetes",
                    "Examina logs de sistema",
                    "Busca patrones sospechosos",
                    "Reconstruye eventos"
                ],
                "tools": ["Wireshark", "tcpdump", "Zeek", "Suricata"]
            }
        ]
        
        self.show_methodology(methodology)
    
    def steganography_guide(self):
        """Guía para Steganography"""
        print("\n🖼️ GUÍA: STEGANOGRAPHY")
        print("="*50)
        
        methodology = [
            {
                "step": 1,
                "title": "Análisis de la imagen",
                "description": "Examina el archivo de imagen",
                "actions": [
                    "Verifica el formato de imagen",
                    "Examina metadatos EXIF",
                    "Analiza el tamaño y propiedades",
                    "Busca anomalías visuales"
                ],
                "tools": ["exiftool", "identify", "hexdump"],
                "commands": [
                    "exiftool image.jpg",
                    "identify -verbose image.jpg",
                    "hexdump -C image.jpg | head -20"
                ]
            },
            {
                "step": 2,
                "title": "Búsqueda de datos ocultos",
                "description": "Busca información escondida",
                "actions": [
                    "Examina LSB (Least Significant Bits)",
                    "Busca archivos embebidos",
                    "Analiza canales de color por separado",
                    "Verifica la tabla de colores"
                ],
                "tools": ["steghide", "stegsolve", "binwalk", "zsteg"],
                "techniques": [
                    "LSB substitution",
                    "DCT coefficient modification",
                    "Palette-based steganography",
                    "Frequency domain hiding"
                ]
            },
            {
                "step": 3,
                "title": "Extracción de datos",
                "description": "Extrae la información oculta",
                "actions": [
                    "Usa herramientas especializadas",
                    "Prueba diferentes algoritmos",
                    "Testa con y sin contraseña",
                    "Examina diferentes formatos de salida"
                ],
                "tools": ["steghide", "outguess", "stegpy", "stegcracker"],
                "commands": [
                    "steghide extract -sf image.jpg",
                    "binwalk -e image.jpg",
                    "zsteg image.png",
                    "stegcracker image.jpg wordlist.txt"
                ]
            },
            {
                "step": 4,
                "title": "Análisis avanzado",
                "description": "Técnicas especializadas",
                "actions": [
                    "Análisis espectral",
                    "Correlación estadística",
                    "Análisis de histogramas",
                    "Detección de patrones"
                ],
                "tools": ["StegExpose", "Steganalysis tools", "Custom scripts"]
            }
        ]
        
        self.show_methodology(methodology)
    
    def osint_guide(self):
        """Guía para OSINT"""
        print("\n🌍 GUÍA: OSINT (Open Source Intelligence)")
        print("="*50)
        
        methodology = [
            {
                "step": 1,
                "title": "Recopilación de información básica",
                "description": "Obtén datos iniciales del objetivo",
                "actions": [
                    "Busca en motores de búsqueda",
                    "Examina redes sociales",
                    "Verifica dominios y subdominios",
                    "Recopila metadatos públicos"
                ],
                "tools": ["Google", "Shodan", "Censys", "theHarvester"],
                "search_operators": [
                    "site:example.com",
                    "filetype:pdf",
                    "intitle:\"confidential\"",
                    "inurl:admin"
                ]
            },
            {
                "step": 2,
                "title": "Análisis de redes sociales",
                "description": "Investiga presencia en redes sociales",
                "actions": [
                    "Busca perfiles en todas las plataformas",
                    "Analiza conexiones y relaciones",
                    "Examina posts y comentarios",
                    "Verifica información de contacto"
                ],
                "tools": ["Sherlock", "Social-Analyzer", "Maltego"],
                "platforms": [
                    "Twitter/X", "LinkedIn", "Facebook", "Instagram",
                    "GitHub", "Reddit", "Discord"
                ]
            },
            {
                "step": 3,
                "title": "Análisis de infraestructura",
                "description": "Examina la infraestructura técnica",
                "actions": [
                    "Enumera subdominios",
                    "Verifica certificados SSL",
                    "Analiza registros DNS",
                    "Busca servicios expuestos"
                ],
                "tools": ["Subfinder", "Amass", "Nmap", "Masscan"],
                "techniques": [
                    "DNS enumeration",
                    "Certificate transparency logs",
                    "Port scanning",
                    "Service fingerprinting"
                ]
            },
            {
                "step": 4,
                "title": "Correlación y análisis",
                "description": "Conecta la información recopilada",
                "actions": [
                    "Crea mapas de relaciones",
                    "Verifica información cruzada",
                    "Identifica patrones y conexiones",
                    "Documenta hallazgos"
                ],
                "tools": ["Maltego", "Gephi", "Custom scripts"]
            }
        ]
        
        self.show_methodology(methodology)
    
    def general_tips(self):
        """Consejos generales para CTFs"""
        print("\n🎓 TIPS GENERALES PARA CTFs")
        print("="*50)
        
        tips = [
            {
                "category": "🧠 Mentalidad",
                "advice": [
                    "Lee la descripción del reto cuidadosamente",
                    "Busca pistas en el título y descripción",
                    "No te obsesiones con una sola técnica",
                    "Toma descansos cuando te atasques",
                    "Colabora con tu equipo"
                ]
            },
            {
                "category": "🔍 Reconocimiento",
                "advice": [
                    "Siempre empieza con file, strings y exiftool",
                    "Examina el código fuente en retos web",
                    "Busca archivos ocultos o de backup",
                    "Verifica metadatos en imágenes",
                    "Usa binwalk en archivos sospechosos"
                ]
            },
            {
                "category": "🛠️ Herramientas",
                "advice": [
                    "Mantén un toolkit actualizado",
                    "Aprende shortcuts de tus herramientas",
                    "Usa CyberChef para operaciones rápidas",
                    "Automatiza tareas repetitivas",
                    "Ten scripts personalizados listos"
                ]
            },
            {
                "category": "📝 Documentación",
                "advice": [
                    "Documenta todos los pasos",
                    "Guarda comandos útiles",
                    "Mantén un log de técnicas",
                    "Anota patrones comunes",
                    "Comparte conocimientos con el equipo"
                ]
            },
            {
                "category": "🎯 Estrategia",
                "advice": [
                    "Ataca primero los retos fáciles",
                    "Distribuye tiempo entre categorías",
                    "No gastes mucho tiempo en un reto",
                    "Busca quick wins",
                    "Mantén la motivación alta"
                ]
            }
        ]
        
        for tip_group in tips:
            print(f"\n{tip_group['category']}")
            print("-" * 30)
            for advice in tip_group['advice']:
                print(f"• {advice}")
    
    def recommended_tools(self):
        """Muestra herramientas recomendadas por categoría"""
        print("\n🛠️ HERRAMIENTAS RECOMENDADAS")
        print("="*50)
        
        tools = {
            "🌐 Web": [
                "Burp Suite - Proxy y scanner web",
                "OWASP ZAP - Scanner de vulnerabilidades",
                "gobuster - Directory fuzzing",
                "sqlmap - SQL injection automation",
                "nikto - Web server scanner",
                "ffuf - Fast web fuzzer"
            ],
            "🔐 Crypto": [
                "CyberChef - Swiss army knife",
                "dcode.fr - Cipher identification",
                "John the Ripper - Password cracking",
                "Hashcat - Hash cracking",
                "sage - Mathematical computations",
                "factordb.com - Integer factorization"
            ],
            "🔄 Reverse": [
                "Ghidra - NSA reverse engineering",
                "IDA Pro - Disassembler",
                "radare2 - Reverse engineering framework",
                "gdb - GNU debugger",
                "x64dbg - Windows debugger",
                "Binary Ninja - Analysis platform"
            ],
            "🔍 Forensics": [
                "Volatility - Memory analysis",
                "Wireshark - Network analysis",
                "Autopsy - Digital forensics",
                "binwalk - Firmware analysis",
                "foremost - File recovery",
                "exiftool - Metadata extraction"
            ],
            "🖼️ Steganography": [
                "steghide - Hide data in images",
                "stegsolve - Image analysis",
                "zsteg - PNG/BMP steganography",
                "outguess - Statistical steganography",
                "stegcracker - Steganography brute force",
                "binwalk - Embedded file extraction"
            ],
            "🌍 OSINT": [
                "Maltego - Link analysis",
                "Shodan - Internet device search",
                "theHarvester - Email/subdomain gathering",
                "Sherlock - Username investigation",
                "Amass - Network mapping",
                "Recon-ng - Web reconnaissance"
            ]
        }
        
        for category, tool_list in tools.items():
            print(f"\n{category}")
            print("-" * 30)
            for tool in tool_list:
                print(f"• {tool}")
    
    def show_methodology(self, methodology):
        """Muestra una metodología paso a paso"""
        print(f"\n📋 METODOLOGÍA ({len(methodology)} pasos)")
        print("="*50)
        
        for step_info in methodology:
            print(f"\n🔹 PASO {step_info['step']}: {step_info['title']}")
            print(f"📝 {step_info['description']}")
            print("\n📋 ACCIONES:")
            for action in step_info['actions']:
                print(f"  • {action}")
            
            if 'tools' in step_info:
                print(f"\n🛠️ HERRAMIENTAS: {', '.join(step_info['tools'])}")
            
            if 'commands' in step_info:
                print("\n💻 COMANDOS:")
                for cmd in step_info['commands']:
                    print(f"  $ {cmd}")
            
            if 'tips' in step_info:
                print("\n💡 TIPS:")
                for tip in step_info['tips']:
                    print(f"  • {tip}")
            
            if 'payloads' in step_info:
                print("\n🎯 PAYLOADS:")
                for payload_type, payloads in step_info['payloads'].items():
                    print(f"  {payload_type}:")
                    for payload in payloads:
                        print(f"    - {payload}")
            
            print("-" * 50)
        
        input("\n⏸️ Presiona Enter para continuar...")
    
    def interactive_challenge_solver(self):
        """Simulador interactivo de resolución de retos"""
        print("\n🎮 SIMULADOR DE RESOLUCIÓN DE RETOS")
        print("="*50)
        
        scenarios = [
            {
                "title": "Reto Web: Login Bypass",
                "description": "Hay una página de login que parece vulnerable",
                "hints": [
                    "El formulario no valida correctamente las entradas",
                    "SQL injection podría ser posible",
                    "Prueba payloads básicos primero"
                ],
                "solution": "SQL injection con payload: admin' OR '1'='1'--"
            },
            {
                "title": "Reto Crypto: Texto Cifrado",
                "description": "Tienes un texto cifrado: 'Uryyb Jbeyq'",
                "hints": [
                    "El texto mantiene espacios y estructura",
                    "Podría ser un cifrado por sustitución",
                    "ROT13 es muy común en CTFs"
                ],
                "solution": "ROT13 cipher - resultado: 'Hello World'"
            },
            {
                "title": "Reto Steganography: Imagen Sospechosa",
                "description": "Una imagen JPG que parece normal",
                "hints": [
                    "Los metadatos podrían contener información",
                    "Podría haber datos ocultos en LSB",
                    "Prueba herramientas automáticas primero"
                ],
                "solution": "steghide extract -sf image.jpg"
            }
        ]
        
        scenario = random.choice(scenarios)
        print(f"\n🎯 RETO: {scenario['title']}")
        print(f"📝 {scenario['description']}")
        
        print("\n💡 PISTAS DISPONIBLES:")
        for i, hint in enumerate(scenario['hints'], 1):
            show_hint = input(f"¿Quieres ver la pista {i}? (s/n): ")
            if show_hint.lower() == 's':
                print(f"  💡 {hint}")
        
        print(f"\n🏆 SOLUCIÓN: {scenario['solution']}")
        input("\n⏸️ Presiona Enter para continuar...")
    
    def run(self):
        """Ejecuta la aplicación principal"""
        self.show_banner()
        
        while True:
            self.show_main_menu()
            
            try:
                choice = input("\nSelecciona una opción: ").strip()
                
                if choice == '1':
                    self.web_exploitation_guide()
                elif choice == '2':
                    self.crypto_guide()
                elif choice == '3':
                    self.reverse_engineering_guide()
                elif choice == '4':
                    self.forensics_guide()
                elif choice == '5':
                    print("\n💥 BINARY EXPLOITATION - Próximamente...")
                    input("Presiona Enter para continuar...")
                elif choice == '6':
                    self.steganography_guide()
                elif choice == '7':
                    self.osint_guide()
                elif choice == '8':
                    print("\n📦 MISCELLANEOUS - Combina técnicas de otras categorías")
                    input("Presiona Enter para continuar...")
                elif choice == '9':
                    self.general_tips()
                    input("\n⏸️ Presiona Enter para continuar...")
                elif choice == '10':
                    self.recommended_tools()
                    input("\n⏸️ Presiona Enter para continuar...")
                elif choice == '0':
                    print("\n👋 ¡Buena suerte en tus CTFs! Happy hacking!")
                    break
                else:
                    print("❌ Opción inválida. Intenta nuevamente.")
                    
            except KeyboardInterrupt:
                print("\n\n👋 ¡Hasta luego! Happy hacking!")
                break
            except Exception as e:
                print(f"❌ Error: {str(e)}")

def main():
    """Función principal"""
    try:
        guide = CTFSolverGuide()
        guide.run()
    except Exception as e:
        print(f"❌ Error crítico: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
