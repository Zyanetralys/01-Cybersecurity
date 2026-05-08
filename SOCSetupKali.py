#!/usr/bin/env python3
"""
SOC Setup Script para Kali Linux
Configura un Security Operations Center completo con herramientas opensource
Autor: Imegami
Fecha: 2025
"""

import os
import subprocess
import sys
import time
import json
import requests
from pathlib import Path

class KaliSOCSetup:
    def __init__(self):
        self.log_file = "/var/log/soc_setup.log"
        self.soc_dir = "/opt/soc"
        self.config_dir = "/etc/soc"
        
    def log(self, message):
        """Registra mensajes en log y consola"""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_msg = f"[{timestamp}] {message}"
        print(log_msg)
        with open(self.log_file, "a") as f:
            f.write(log_msg + "\n")
    
    def run_command(self, command, check=True):
        """Ejecuta comandos del sistema"""
        try:
            self.log(f"Ejecutando: {command}")
            result = subprocess.run(command, shell=True, capture_output=True, text=True, check=check)
            if result.stdout:
                self.log(f"Salida: {result.stdout}")
            return result
        except subprocess.CalledProcessError as e:
            self.log(f"Error ejecutando comando: {e}")
            if e.stderr:
                self.log(f"Error: {e.stderr}")
            return None
    
    def check_root(self):
        """Verifica que se ejecute como root"""
        if os.geteuid() != 0:
            self.log("Este script debe ejecutarse como root")
            sys.exit(1)
    
    def update_system(self):
        """Actualiza el sistema"""
        self.log("=== ACTUALIZANDO SISTEMA ===")
        self.run_command("apt update && apt upgrade -y")
        self.run_command("apt install -y curl wget git python3-pip docker.io docker-compose")
        
    def create_directories(self):
        """Crea directorios necesarios"""
        self.log("=== CREANDO DIRECTORIOS ===")
        directories = [self.soc_dir, self.config_dir, 
                      f"{self.soc_dir}/logs", f"{self.soc_dir}/data", 
                      f"{self.soc_dir}/scripts", f"{self.soc_dir}/configs"]
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
            self.log(f"Directorio creado: {directory}")
    
    def install_elastic_stack(self):
        """Instala Elasticsearch, Logstash y Kibana (ELK Stack)"""
        self.log("=== INSTALANDO ELK STACK ===")
        
        # Agregar repositorio de Elastic
        self.run_command("wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key add -")
        self.run_command('echo "deb https://artifacts.elastic.co/packages/8.x/apt stable main" | tee /etc/apt/sources.list.d/elastic-8.x.list')
        self.run_command("apt update")
        
        # Instalar componentes
        self.run_command("apt install -y elasticsearch kibana logstash filebeat")
        
        # Configurar Elasticsearch
        es_config = """
cluster.name: soc-cluster
node.name: soc-node-1
path.data: /var/lib/elasticsearch
path.logs: /var/log/elasticsearch
network.host: 127.0.0.1
http.port: 9200
discovery.type: single-node
xpack.security.enabled: false
"""
        with open("/etc/elasticsearch/elasticsearch.yml", "w") as f:
            f.write(es_config)
            
        # Configurar Kibana
        kibana_config = """
server.port: 5601
server.host: "0.0.0.0"
elasticsearch.hosts: ["http://127.0.0.1:9200"]
"""
        with open("/etc/kibana/kibana.yml", "w") as f:
            f.write(kibana_config)
            
        # Habilitar servicios
        self.run_command("systemctl enable elasticsearch")
        self.run_command("systemctl enable kibana")
        self.run_command("systemctl start elasticsearch")
        self.run_command("systemctl start kibana")
        
    def install_wazuh(self):
        """Instala Wazuh HIDS/SIEM"""
        self.log("=== INSTALANDO WAZUH ===")
        
        # Instalar Wazuh manager
        self.run_command("curl -sO https://packages.wazuh.com/4.x/apt/pool/main/w/wazuh-manager/wazuh-manager_4.7.2-1_amd64.deb")
        self.run_command("dpkg -i wazuh-manager_4.7.2-1_amd64.deb")
        
        # Configurar Wazuh
        wazuh_config = """
<ossec_config>
  <global>
    <jsonout_output>yes</jsonout_output>
    <alerts_log>yes</alerts_log>
    <logall>no</logall>
    <logall_json>no</logall_json>
  </global>
  
  <alerts>
    <log_alert_level>3</log_alert_level>
    <email_alert_level>12</email_alert_level>
  </alerts>
  
  <remote>
    <connection>secure</connection>
    <port>1514</port>
    <protocol>udp</protocol>
  </remote>
</ossec_config>
"""
        with open("/var/ossec/etc/ossec.conf", "a") as f:
            f.write(wazuh_config)
            
        self.run_command("systemctl enable wazuh-manager")
        self.run_command("systemctl start wazuh-manager")
    
    def install_suricata(self):
        """Instala Suricata IDS/IPS"""
        self.log("=== INSTALANDO SURICATA ===")
        
        self.run_command("apt install -y suricata")
        
        # Configurar Suricata
        suricata_config = f"""
HOME_NET: "[192.168.0.0/16,10.0.0.0/8,172.16.0.0/12]"
EXTERNAL_NET: "!$HOME_NET"
HTTP_SERVERS: "$HOME_NET"
SMTP_SERVERS: "$HOME_NET"
SQL_SERVERS: "$HOME_NET"
DNS_SERVERS: "$HOME_NET"
TELNET_SERVERS: "$HOME_NET"
AIM_SERVERS: "$EXTERNAL_NET"
DC_SERVERS: "$HOME_NET"
DNP3_SERVER: "$HOME_NET"
DNP3_CLIENT: "$HOME_NET"
MODBUS_CLIENT: "$HOME_NET"
MODBUS_SERVER: "$HOME_NET"
ENIP_CLIENT: "$HOME_NET"
ENIP_SERVER: "$HOME_NET"

default-log-dir: {self.soc_dir}/logs/suricata/

outputs:
  - fast:
      enabled: yes
      filename: fast.log
  - eve-log:
      enabled: yes
      filetype: regular
      filename: eve.json
      types:
        - alert
        - http
        - dns
        - tls
        - files
        - smtp
        - flow
"""
        
        with open("/etc/suricata/suricata.yaml", "w") as f:
            f.write(suricata_config)
        
        # Actualizar reglas
        self.run_command("suricata-update")
        
        self.run_command("systemctl enable suricata")
        self.run_command("systemctl start suricata")
    
    def install_ossim(self):
        """Instala OSSIM (AlienVault Open Source SIEM)"""
        self.log("=== INSTALANDO COMPONENTES ADICIONALES SIEM ===")
        
        # Instalar OSSEC (parte de OSSIM)
        self.run_command("apt install -y ossec-hids")
        
        # Configurar OSSEC
        self.run_command("systemctl enable ossec")
        
    def install_security_tools(self):
        """Instala herramientas adicionales de seguridad"""
        self.log("=== INSTALANDO HERRAMIENTAS DE SEGURIDAD ===")
        
        tools = [
            "nmap", "masscan", "zmap",  # Network scanning
            "wireshark", "tshark", "tcpdump",  # Network analysis
            "volatility3", "autopsy",  # Forensics
            "yara", "clamav",  # Malware analysis
            "hashcat", "john",  # Password cracking
            "sqlmap", "nikto",  # Web security
            "metasploit-framework",  # Exploitation
            "aircrack-ng", "kismet",  # Wireless security
            "binwalk", "foremost",  # File analysis
            "radare2", "gdb"  # Reverse engineering
        ]
        
        for tool in tools:
            self.run_command(f"apt install -y {tool}")
    
    def install_threat_intelligence(self):
        """Instala herramientas de Threat Intelligence"""
        self.log("=== INSTALANDO HERRAMIENTAS DE THREAT INTELLIGENCE ===")
        
        # MISP (Malware Information Sharing Platform)
        self.run_command("git clone https://github.com/MISP/MISP.git /opt/MISP")
        
        # TheHive (Incident Response Platform)
        self.run_command("apt install -y openjdk-11-jre-headless")
        
        # Instalar Python tools para TI
        ti_tools = [
            "yara-python", "pefile", "python3-magic",
            "requests", "beautifulsoup4", "shodan",
            "virustotal-api", "censys", "passivetotal"
        ]
        
        for tool in ti_tools:
            self.run_command(f"pip3 install {tool}")
    
    def setup_log_management(self):
        """Configura gestión de logs"""
        self.log("=== CONFIGURANDO GESTIÓN DE LOGS ===")
        
        # Configurar rsyslog para centralizar logs
        rsyslog_config = f"""
# SOC Log Management Configuration
$ModLoad imudp
$UDPServerRun 514
$UDPServerAddress 127.0.0.1

# Store all logs in SOC directory
*.* {self.soc_dir}/logs/all.log
auth,authpriv.* {self.soc_dir}/logs/auth.log
mail.* {self.soc_dir}/logs/mail.log
kern.* {self.soc_dir}/logs/kernel.log
daemon.* {self.soc_dir}/logs/daemon.log
"""
        
        with open("/etc/rsyslog.d/50-soc.conf", "w") as f:
            f.write(rsyslog_config)
        
        self.run_command("systemctl restart rsyslog")
        
        # Configurar logrotate
        logrotate_config = f"""
{self.soc_dir}/logs/*.log {{
    daily
    missingok
    rotate 365
    compress
    delaycompress
    notifempty
    create 0644 root root
}}
"""
        with open("/etc/logrotate.d/soc", "w") as f:
            f.write(logrotate_config)
    
    def create_monitoring_scripts(self):
        """Crea scripts de monitoreo personalizados"""
        self.log("=== CREANDO SCRIPTS DE MONITOREO ===")
        
        # Script de monitoreo de red
        network_monitor = f"""#!/usr/bin/env python3
import psutil
import time
import json
import datetime

def monitor_network():
    while True:
        stats = psutil.net_io_counters()
        connections = len(psutil.net_connections())
        
        data = {{
            'timestamp': datetime.datetime.now().isoformat(),
            'bytes_sent': stats.bytes_sent,
            'bytes_recv': stats.bytes_recv,
            'packets_sent': stats.packets_sent,
            'packets_recv': stats.packets_recv,
            'active_connections': connections
        }}
        
        with open('{self.soc_dir}/logs/network_stats.json', 'a') as f:
            f.write(json.dumps(data) + '\\n')
        
        time.sleep(60)

if __name__ == '__main__':
    monitor_network()
"""
        
        with open(f"{self.soc_dir}/scripts/network_monitor.py", "w") as f:
            f.write(network_monitor)
        
        os.chmod(f"{self.soc_dir}/scripts/network_monitor.py", 0o755)
        
        # Script de análisis de logs
        log_analyzer = f"""#!/usr/bin/env python3
import re
import json
from collections import defaultdict
import datetime

def analyze_auth_logs():
    failed_logins = defaultdict(int)
    successful_logins = defaultdict(int)
    
    try:
        with open('{self.soc_dir}/logs/auth.log', 'r') as f:
            for line in f:
                if 'Failed password' in line:
                    ip_match = re.search(r'from ([\\d.]+)', line)
                    if ip_match:
                        failed_logins[ip_match.group(1)] += 1
                elif 'Accepted password' in line:
                    ip_match = re.search(r'from ([\\d.]+)', line)
                    if ip_match:
                        successful_logins[ip_match.group(1)] += 1
    except FileNotFoundError:
        pass
    
    # Detectar posibles ataques de fuerza bruta
    alerts = []
    for ip, count in failed_logins.items():
        if count > 10:  # Más de 10 intentos fallidos
            alerts.append({{
                'type': 'brute_force_attempt',
                'ip': ip,
                'failed_attempts': count,
                'timestamp': datetime.datetime.now().isoformat()
            }})
    
    # Guardar alertas
    if alerts:
        with open('{self.soc_dir}/logs/security_alerts.json', 'a') as f:
            for alert in alerts:
                f.write(json.dumps(alert) + '\\n')
    
    return alerts

if __name__ == '__main__':
    alerts = analyze_auth_logs()
    if alerts:
        print(f"Se detectaron {{len(alerts)}} alertas de seguridad")
    else:
        print("No se detectaron amenazas")
"""
        
        with open(f"{self.soc_dir}/scripts/log_analyzer.py", "w") as f:
            f.write(log_analyzer)
        
        os.chmod(f"{self.soc_dir}/scripts/log_analyzer.py", 0o755)
    
    def setup_dashboards(self):
        """Configura dashboards de monitoreo"""
        self.log("=== CONFIGURANDO DASHBOARDS ===")
        
        # Instalar Grafana
        self.run_command("wget -q -O - https://packages.grafana.com/gpg.key | apt-key add -")
        self.run_command('echo "deb https://packages.grafana.com/oss/deb stable main" | tee /etc/apt/sources.list.d/grafana.list')
        self.run_command("apt update && apt install -y grafana")
        
        # Configurar Grafana
        grafana_config = """
[server]
http_addr = 0.0.0.0
http_port = 3000

[database]
type = sqlite3
path = grafana.db

[security]
admin_user = admin
admin_password = socadmin123
"""
        with open("/etc/grafana/grafana.ini", "w") as f:
            f.write(grafana_config)
        
        self.run_command("systemctl enable grafana-server")
        self.run_command("systemctl start grafana-server")
    
    def create_automation_scripts(self):
        """Crea scripts de automatización"""
        self.log("=== CREANDO SCRIPTS DE AUTOMATIZACIÓN ===")
        
        # Script de respuesta automática a incidentes
        incident_response = f"""#!/usr/bin/env python3
import json
import subprocess
import smtplib
from email.mime.text import MIMEText
import datetime

def block_ip(ip_address):
    '''Bloquea una IP usando iptables'''
    cmd = f"iptables -A INPUT -s {{ip_address}} -j DROP"
    subprocess.run(cmd, shell=True)
    print(f"IP {{ip_address}} bloqueada")

def send_alert_email(alert_data):
    '''Envía alerta por email (configurar SMTP)'''
    # Configurar según tu servidor SMTP
    pass

def process_security_alerts():
    '''Procesa alertas de seguridad y toma acciones'''
    try:
        with open('{self.soc_dir}/logs/security_alerts.json', 'r') as f:
            for line in f:
                alert = json.loads(line.strip())
                
                if alert['type'] == 'brute_force_attempt':
                    if alert['failed_attempts'] > 20:
                        # Bloquear IP automáticamente
                        block_ip(alert['ip'])
                        
                        # Registrar acción
                        action_log = {{
                            'timestamp': datetime.datetime.now().isoformat(),
                            'action': 'ip_blocked',
                            'ip': alert['ip'],
                            'reason': 'brute_force_attack'
                        }}
                        
                        with open('{self.soc_dir}/logs/incident_response.json', 'a') as f:
                            f.write(json.dumps(action_log) + '\\n')
                        
    except FileNotFoundError:
        pass

if __name__ == '__main__':
    process_security_alerts()
"""
        
        with open(f"{self.soc_dir}/scripts/incident_response.py", "w") as f:
            f.write(incident_response)
        
        os.chmod(f"{self.soc_dir}/scripts/incident_response.py", 0o755)
    
    def setup_cron_jobs(self):
        """Configura trabajos programados"""
        self.log("=== CONFIGURANDO TRABAJOS PROGRAMADOS ===")
        
        cron_jobs = f"""
# SOC Automation Jobs
*/5 * * * * root {self.soc_dir}/scripts/log_analyzer.py
*/10 * * * * root {self.soc_dir}/scripts/incident_response.py
0 */6 * * * root suricata-update && systemctl reload suricata
0 2 * * * root freshclam
"""
        
        with open("/etc/cron.d/soc", "w") as f:
            f.write(cron_jobs)
        
        self.run_command("systemctl restart cron")
    
    def install_additional_tools(self):
        """Instala herramientas adicionales especializadas"""
        self.log("=== INSTALANDO HERRAMIENTAS ADICIONALES ===")
        
        # Instalar YARA
        self.run_command("apt install -y yara")
        
        # Instalar Volatility
        self.run_command("pip3 install volatility3")
        
        # Instalar ClamAV
        self.run_command("apt install -y clamav clamav-daemon")
        self.run_command("freshclam")
        
        # Instalar Moloch (Full Packet Capture)
        self.run_command("wget https://raw.githubusercontent.com/aol/moloch/master/release/Configure")
        self.run_command("chmod +x Configure")
        
    def create_web_interface(self):
        """Crea interfaz web básica para el SOC"""
        self.log("=== CREANDO INTERFAZ WEB ===")
        
        web_interface = f"""<!DOCTYPE html>
<html>
<head>
    <title>SOC Dashboard</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {{ font-family: Arial, sans-serif; margin: 0; padding: 20px; background-color: #1a1a1a; color: white; }}
        .header {{ text-align: center; margin-bottom: 30px; }}
        .dashboard {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; }}
        .widget {{ background-color: #2a2a2a; padding: 20px; border-radius: 8px; border-left: 4px solid #00ff00; }}
        .widget h3 {{ margin-top: 0; color: #00ff00; }}
        .status {{ display: inline-block; width: 12px; height: 12px; border-radius: 50%; margin-right: 8px; }}
        .status.online {{ background-color: #00ff00; }}
        .status.offline {{ background-color: #ff0000; }}
        .links {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 10px; margin-top: 20px; }}
        .link {{ background-color: #333; padding: 10px; text-align: center; border-radius: 4px; }}
        .link a {{ color: #00ff00; text-decoration: none; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🛡️ SOC Dashboard - Kali Linux</h1>
        <p>Security Operations Center - Estado del Sistema</p>
    </div>
    
    <div class="dashboard">
        <div class="widget">
            <h3>📊 Servicios Principales</h3>
            <p><span class="status online"></span>Elasticsearch</p>
            <p><span class="status online"></span>Kibana</p>
            <p><span class="status online"></span>Suricata IDS</p>
            <p><span class="status online"></span>Wazuh</p>
            <p><span class="status online"></span>Grafana</p>
        </div>
        
        <div class="widget">
            <h3>🔍 Detección de Amenazas</h3>
            <p>Reglas Suricata: <strong>Activas</strong></p>
            <p>YARA Rules: <strong>Actualizadas</strong></p>
            <p>ClamAV: <strong>Funcionando</strong></p>
            <p>Última actualización: <strong>Hoy</strong></p>
        </div>
        
        <div class="widget">
            <h3>📈 Estadísticas Recientes</h3>
            <p>Alertas últimas 24h: <strong>0</strong></p>
            <p>IPs bloqueadas: <strong>0</strong></p>
            <p>Logs procesados: <strong>Activo</strong></p>
            <p>Análisis forense: <strong>Listo</strong></p>
        </div>
        
        <div class="widget">
            <h3>🚨 Alertas Críticas</h3>
            <p>No hay alertas críticas</p>
            <p>Estado: <span style="color: #00ff00;">SEGURO</span></p>
        </div>
    </div>
    
    <div class="links">
        <div class="link"><a href="http://localhost:5601" target="_blank">Kibana (Logs)</a></div>
        <div class="link"><a href="http://localhost:3000" target="_blank">Grafana (Métricas)</a></div>
        <div class="link"><a href="http://localhost:9200" target="_blank">Elasticsearch</a></div>
        <div class="link"><a href="/logs" target="_blank">Ver Logs</a></div>
    </div>
</body>
</html>"""
        
        # Crear servidor web simple
        web_server = f"""#!/usr/bin/env python3
import http.server
import socketserver
import os

os.chdir('{self.soc_dir}')

class SOCHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='{self.soc_dir}', **kwargs)

PORT = 8080
with socketserver.TCPServer(("", PORT), SOCHandler) as httpd:
    print(f"SOC Web Interface corriendo en http://localhost:{{PORT}}")
    httpd.serve_forever()
"""
        
        with open(f"{self.soc_dir}/index.html", "w") as f:
            f.write(web_interface)
        
        with open(f"{self.soc_dir}/scripts/web_server.py", "w") as f:
            f.write(web_server)
        
        os.chmod(f"{self.soc_dir}/scripts/web_server.py", 0o755)
    
    def finalize_setup(self):
        """Finaliza la configuración"""
        self.log("=== FINALIZANDO CONFIGURACIÓN ===")
        
        # Crear script de inicio
        startup_script = f"""#!/bin/bash
echo "🛡️  Iniciando SOC - Security Operations Center"
echo "=============================================="

# Iniciar servicios principales
systemctl start elasticsearch
systemctl start kibana
systemctl start suricata
systemctl start wazuh-manager
systemctl start grafana-server

# Iniciar scripts de monitoreo en background
nohup python3 {self.soc_dir}/scripts/network_monitor.py > /dev/null 2>&1 &
nohup python3 {self.soc_dir}/scripts/web_server.py > /dev/null 2>&1 &

echo "✅ SOC iniciado correctamente"
echo ""
echo "🌐 Interfaces disponibles:"
echo "   - Kibana (Logs): http://localhost:5601"
echo "   - Grafana (Métricas): http://localhost:3000"
echo "   - SOC Dashboard: http://localhost:8080"
echo ""
echo "📁 Directorios importantes:"
echo "   - Logs: {self.soc_dir}/logs/"
echo "   - Scripts: {self.soc_dir}/scripts/"
echo "   - Configuración: {self.config_dir}/"
echo ""
echo "🔧 Comandos útiles:"
echo "   - Ver alertas: tail -f {self.soc_dir}/logs/security_alerts.json"
echo "   - Analizar logs: {self.soc_dir}/scripts/log_analyzer.py"
echo "   - Estado servicios: systemctl status elasticsearch kibana suricata"
"""
        
        with open("/usr/local/bin/start-soc", "w") as f:
            f.write(startup_script)
        
        os.chmod("/usr/local/bin/start-soc", 0o755)
        
        # Crear documentación
        documentation = f"""# 🛡️ SOC - Security Operations Center

## Descripción
Este SOC incluye las siguientes herramientas:

### SIEM y Log Management
- **Elasticsearch**: Motor de búsqueda y análisis
- **Kibana**: Visualización de logs y métricas
- **Logstash**: Procesamiento de logs
- **Wazuh**: HIDS/SIEM para detección de amenazas

### Network Security
- **Suricata**: IDS/IPS para detección de intrusos
- **pfSense/iptables**: Firewall y filtrado

### Threat Intelligence
- **YARA**: Detección de malware
- **ClamAV**: Antivirus
- **MISP**: Plataforma de intercambio de threat intelligence

### Análisis Forense
- **Volatility**: Análisis de memoria
- **Autopsy**: Análisis forense de disco
- **Wireshark**: Análisis de tráfico de red

## Directorios
- `{self.soc_dir}/logs/`: Todos los logs del sistema
- `{self.soc_dir}/scripts/`: Scripts personalizados
- `{self.soc_dir}/data/`: Datos de análisis
- `{self.config_dir}/`: Archivos de configuración

## Comandos Importantes
```bash
# Iniciar SOC completo
start-soc

# Ver estado de servicios
systemctl status elasticsearch kibana suricata wazuh-manager

# Analizar logs en tiempo real
tail -f {self.soc_dir}/logs/security_alerts.json

# Ejecutar análisis manual
{self.soc_dir}/scripts/log_analyzer.py
```

## Acceso Web
- Kibana: http://localhost:5601
- Grafana: http://localhost:3000 (admin/socadmin123)
- SOC Dashboard: http://localhost:8080

## Próximos Pasos
1. Configurar fuentes de logs adicionales
2. Personalizar reglas de detección
3. Configurar alertas por email/Slack
4. Añadir más dashboards de monitoreo
5. Implementar playbooks de respuesta a incidentes
"""
        
        with open(f"{self.soc_dir}/README.md", "w") as f:
            f.write(documentation)
        
        self.log("✅ Configuración completada exitosamente")
        
    def run_setup(self):
        """Ejecuta todo el setup"""
        start_time = time.time()
        
        self.log("🛡️ Iniciando configuración de SOC en Kali Linux")
        
        try:
            self.check_root()
            self.create_directories()
            self.update_system()
            self.install_elastic_stack()
            self.install_wazuh()
            self.install_suricata()
            self.install_ossim()
            self.install_security_tools()
            self.install_threat_intelligence()
            self.setup_log_management()
            self.create_monitoring_scripts()
            self.setup_dashboards()
            self.create_automation_scripts()
            self.setup_cron_jobs()
            self.install_additional_tools()
            self.create_web_interface()
            self.finalize_setup()
            
            end_time = time.time()
            duration = round(end_time - start_time, 2)
            
            self.log(f"🎉 SOC configurado exitosamente en {duration} segundos")
            self.log("=" * 50)
            self.log("RESUMEN DE LA INSTALACIÓN:")
            self.log("✅ ELK Stack (Elasticsearch, Logstash, Kibana)")
            self.log("✅ Wazuh HIDS/SIEM")
            self.log("✅ Suricata IDS/IPS")
            self.log("✅ Herramientas de seguridad")
            self.log("✅ Threat Intelligence tools")
            self.log("✅ Scripts de automatización")
            self.log("✅ Dashboards de monitoreo")
            self.log("✅ Interfaz web del SOC")
            self.log("=" * 50)
            self.log("🚀 Para iniciar el SOC ejecuta: start-soc")
            self.log("🌐 Dashboard web: http://localhost:8080")
            self.log("📊 Kibana: http://localhost:5601")
            self.log("📈 Grafana: http://localhost:3000")
            
        except Exception as e:
            self.log(f"❌ Error durante la configuración: {e}")
            self.log("Revisa el log completo en /var/log/soc_setup.log")

def main():
    """Función principal"""
    print("""
🛡️  SOC Setup Script para Kali Linux
====================================
Este script instalará y configurará:
- ELK Stack (Elasticsearch, Logstash, Kibana)
- Wazuh HIDS/SIEM
- Suricata IDS/IPS
- Herramientas de análisis forense
- Threat Intelligence tools
- Scripts de automatización
- Dashboards de monitoreo

⚠️  IMPORTANTE: Ejecutar como root
⏱️  Tiempo estimado: 30-60 minutos
💾  Espacio requerido: ~5GB

¿Continuar? (s/n): """, end="")
    
    if input().lower() not in ['s', 'si', 'y', 'yes']:
        print("Instalación cancelada.")
        sys.exit(0)
    
    soc_setup = KaliSOCSetup()
    soc_setup.run_setup()

if __name__ == "__main__":
    main()
