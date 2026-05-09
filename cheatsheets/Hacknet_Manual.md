# Hacknet — Guía completa
Nota: Todo lo aquí descrito es para entrenamiento, CTFs y simulación. No lo uses fuera de entornos autorizados.

---

## 0) Resumen
- Eres un hacker que recibe el “Hacknet OS”. El bucle: enumerar → abrir puertos → PortHack → hacer el objetivo → limpiar → responder.
- Facciones y tramas: Entropy → Naix / /el → CSEC → cadena final de Bit. DLC “Labyrinths” añade nuevas herramientas y puertos.
- Tres defensas clave: PROXY (se sobrecarga), FIREWALL (se “analiza/solve”), TRACE (temporizador que sube con acciones; puedes “congelarlo”).
- “eOS devices” (ePhone/ePad): si están vinculados a un nodo, suele valer login por defecto admin / alpine.

---

## 1) Operativo (checklist)
1. Recon: ‘probe’ (servicios), ‘scan’ (topología), leer /home y /log del objetivo.
2. Preparar acceso: lanzar port-crackers necesarios (mínimo de puertos abiertos según seguridad del nodo).
3. Escalada: ‘PortHack’ para root (cuando tengas los puertos requeridos).
4. Acciones: leer/copiar/editar/subir lo que pida la misión (usa ‘cat’, ‘scp’, ‘upload’, ‘replace’, ‘append’).
5. Antiforense: borra /log del objetivo y revisa tu /log local si el flujo lo requiere.
6. Descubrimiento lateral: ‘scan’ tras entrar para descubrir nuevos nodos (eOS, servidores vinculados, etc.).
7. Salida limpia: ‘disconnect’/’dc’. Responde al correo del contrato.

Equivalencia real: Recon (Nmap) → Exploit (msf/PoC) → Post-explotación (shell) → Acciones (exfil/modificación) → Limpieza (log-wipe) → Pivoting.

---

## 2) Comandos del terminal
Sintaxis entre [ ]. Los más usados arriba. Todo en minúsculas salvo “PortHack”.

- connect [IP] ……… Conecta a un nodo.  ≈ ssh/telnet/nc a un host.
- probe ………………… Enumera puertos/servicios del nodo.  ≈ nmap -sV en simple.
- scan ………………… Descubre nodos vecinos desde el host actual.  ≈ arp-scan/traceroute/enum interna.
- PortHack ………… Acción para tomar root cuando hay suficientes puertos abiertos.  ≈ exploit/priv-esc + toma de control.
- exe [archivo.exe] … Ejecuta un binario de /bin (tu máquina).  ≈ lanzar herramienta local.
- scp [fichero] …… Copia DEL remoto A tu /home.  ≈ scp/sftp descarga.
- upload [fichero] … Sube de tu /home al remoto (directorio actual).  ≈ scp/sftp subida.
- cat [fichero] …… Muestra contenido.  ≈ cat/type.
- rm [fichero] …… Borra.  ≈ rm/del (útil para limpiar /log).
- cd [/ruta] ……… Cambia de carpeta.  ≈ cd.
- mv [origen] [dest] … Renombra/mueve.  ≈ mv/rename.
- replace [fichero] "A" "B" … Sustituye texto en fichero.  ≈ sed/replace in-file.
- append [fichero] "línea" … Añade texto al final.  ≈ echo >>.
- login ………………… Inicia sesión en servicios que lo requieren (p.ej., formularios).  ≈ auth web/API.
- ps ……………………… Lista procesos.  ≈ ps/tasklist.
- kill [PID] ………… Mata proceso.  ≈ kill/taskkill.
- analyze …………… Inicia análisis de firewall.  ≈ fingerprint/bypass analysis (analógico).
- solve ………………… Introduce la solución del firewall (tras analyze).  ≈ responder desafío/clave.
- shell ………………… Abre una shell remota “ligera” en el host (sirve para overload y trampa IP).  ≈ reverse shell / foothold.
- clear ………………… Limpia la pantalla.  ≈ clear.
- disconnect | dc … Corta la conexión actual.  ≈ exit/close.
- reboot -i ………… Reinicia el nodo (útil tras recuperar x-server.sys).  ≈ reboot.
- openCDTray / closeCDTray … Gags (unidades ópticas).  ≈ eject.
- addNote "texto" … Nota local en el nodo.  ≈ nota del operador.
- save ………………… Punto de guardado manual.  ≈ snapshot/commit.
- FirstTimeInit …… Inicializa sistema (casos raros).

Consejos:
- Auto-completado con TAB (comandos y nombres).
- Editar ficheros: ‘cat’ + ‘replace’/‘append’. Si da “Assuming active flag file”, usa la forma completa de replace con nombre de fichero.
- Tras comprometer, ‘scan’ SIEMPRE para descubrir extensiones/eOS.

---

##  3) Ejecutables (EXE) y “port-crackers” (con puertos)
Base del juego:
- SSHcrack.exe  (22) … Abre SSH.  ≈ fuerza bruta/cred-spray/exp SSH.
- FTPBounce.exe (21) … Abre FTP con técnica de bouncing.  ≈ abuso del modo PORT/FTP bounce.
- SMTPoverflow.exe (25) … Desborda SMTP.  ≈ vulnerabilidades históricas de servidores de correo.
- WebServerWorm.exe (80) … Explota HTTP.  ≈ RCE web genérico (think: vuln en CGI/CMS).
- SQLBufferOverflow.exe / SQL_MemCorrupt.exe (1433) … Explota MS-SQL.  ≈ buffer overflow (p.ej., familia Slammer, distinto puerto real).

Herramientas de soporte:
- SecurityTracer.exe … Muestra la traza/contador.  ≈ detección de response/IPS.
- TraceKill.exe … Congela/ralentiza la traza temporalmente.  ≈ TTP de evasión (túneles, pausas, misdirection).
- eosDeviceScan.exe … Enumera y revela eOS vinculados al host.  ≈ discovery de móviles/IoT en subred.
- DECHead.exe … Analiza archivos .dec para extraer metadatos/pistas.  ≈ análisis de contenedor/cabecera (forense).
- Decypher.exe … Descifra .dec con contraseña.  ≈ openssl/gpg descifrado.
- Sequencer.exe … Orquesta shells para la misión final.  ≈ coordinador de tareas/booter interno.
- MemForensics.exe … Analiza MemoryDump.  ≈ Volatility rekall.
- MemoryDumpGenerator.exe … Genera volcados de memoria.  ≈ procdump/dd.
- Clock.exe … Reloj. (gag)

“Project Junebug”:
- KBT_PortTest.exe (104) … Abre puerto 104 (ecosistema médico/DICOM).  ≈ test harness/PoC contra servicio médico.

DLC “Labyrinths” (además de las anteriores):
- FTPSprint.exe (21) … Variante rápida de FTP crack (consume más CPU).  ≈ tool más agresiva (paraleliza).
- RTSPCrack.exe (554) … Abre RTSP (streams/cámaras).  ≈ ataque a credenciales/vulns de cámaras IP.
- SSLTrojan.exe (443) … Toma control a través de capa TLS.  ≈ implante/mitm en HTTPS.
- TorrentStreamInjector.exe (6881) … Abre servicio tipo BitTorrent.  ≈ peer poisoning/inyección en swarm.
- PacificPortcrusher.exe (192) … Abre “Pacific Dedicated”.  ≈ explot/cred en servicio propietario.

Notas:
- “PortHack” requiere N puertos abiertos (según el host) antes de otorgar root. 
-  Proxies: abre shells en otros nodos y pulsa “Overload” para bajarlos; ‘Trap’ cambia tu IP si te rastrean.
- Firewalls: ‘analyze’ → ‘solve’ (puzzle de colores/ritmos/figuras). Lanza solve al ritmo correcto.

---

## 4) eOS (ePhones/ePads): patrón
1. Compromete el PC vinculado (SSH/FTP/… → PortHack).
2. Ejecuta ‘eosDeviceScan.exe’ para listar el dispositivo.
3. ‘connect’ al ePhone/ePad → ‘login’ con admin / alpine (por defecto).
4. Entra a /eos/mail o /eos/notes para extraer lo que pidan (p.ej., *.act). 
5. Limpia logs en ambos lados si procede.

---


## 5) Walkthrough táctico
- Inicio (Bit): recupera x-server.sys si Naix te rompe el escritorio: cd /log → IP → connect → SSHcrack → PortHack → scp /sys/x-server.sys → reboot -i.
- Entropy: baja FTPBounce y SMTPoverflow; usa proxies/shell para sobrecargar; no borres logs locales antes del hack de “Aggression must be punished” (los necesitarás para la trama de Naix).
- Naix & /el: venganza (WebServerWorm), acceso al /el Message Board, Santuario Polar (4 pruebas → IP compuesto).
- CSEC: invitación (gauntlets), CFC cadena, “Ghosting the Vault” (Decypher), “Through the Spyglass” (DECHead), red line (cambia IP en ISP Management), “Project Junebug” (KBT_PortTest y marcapasos, 104).
- Final de Bit: TraceKill → cadena EnTech (Prometheus/Romulus) → Sequencer + múltiples shells → purge de archivos en backups.

Consejos de ruta:
- Tras cada root: ‘scan’. Muchos hilos se abren así (eOS, repos, mainframes).
- Lee /home y /bin del objetivo: a menudo hay regalos (nuevos EXE).
- No renombres ni borres archivos de misión que no debas: puedes romper scripts de progreso.

---


## 6) Buenas prácticas
- Limpieza: /log del objetivo SIEMPRE; tu /log local cuando un guion lo pida (algunas misiones verifican logs).
- Velocidad: teclear comandos mientras corren los EXE ahorra segundos de traza.
- Shells: levántalas en nodos fáciles (routers, test servers) para apoyar overload/Sequencer.
- Firewall: practica el patrón del puzzle con analyze antes de solve; si fallas, repite rápido.
- Documenta: usa ‘addNote’ en nodos críticos (puertas, contraseñas, pistas).

---

## 7) Tabla de equivalencias Hacknet → Pentesting
- probe → Nmap (descubrimiento/servicios).
- scan → mapeo de red (arp-scan, traceroute, net view).
- PortHack → combinación exploit + elevación (Metasploit/PoC + setuid/etc.).
- SSHcrack/FTPBounce/SMTPoverflow/WebServerWorm/SQL* → familias de exploits (Hydra/Ncrack para cred-spray; sqlmap/PoCs; CVEs históricas).
- SSLTrojan → MITM/implant en TLS (mitmproxy, rogue certs, implant post-auth).
- RTSPCrack → cámaras IP (default creds/CVEs DVR).
- TorrentStreamInjector → manipulación de protocolos P2P (peer poisoning).
- KBT_PortTest → IoT/medtech (DICOM/HL7, PoCs regulados).
- SecurityTracer/TraceKill → OPSEC/antiforense (cortes de sesión, tunelado, chaff).
- DECHead/Decypher → cripto/esteganálisis básica (gpg/openssl + análisis de encabezados).
- shell → reverse shell/foothold (nc -e, socat, meterpreter).
- rm /log → limpieza (log-tampering; cuidado, ilegal fuera de labs).

---

## 8) Cheatsheet express (10 pasos)
1) connect [IP] → probe → anota puertos.
2) Lanza los EXE necesarios (SSH/FTP/SMTP/HTTP/SQL/…).
3) Cuando llegues al requisito: PortHack.
4) scan para descubrir red/eOS.
5) cd a la ruta objetivo → cat/replace/append según misión.
6) scp para extraer; upload para plantar archivo.
7) Si hay firewall: analyze → solve.
8) Si hay proxy: monta shells en 2-3 nodos → Overload.
9) Borra /log del remoto (y lo que toque local).
10) disconnect → responde al correo.

---

## 9) Errores típicos a evitar
- Abandonar contratos a mitad (puede romper la progresión).
- Borrar/renombrar ficheros de misión por “limpieza excesiva”.
- Olvidar ‘scan’ tras rootear un nodo.
- No revisar /bin del objetivo (muchos EXE se “regalan” ahí).

---

10) Apéndice A — Lista de comandos (glosario)
help | connect [IP] | probe | scan | PortHack | exe [f] | scp [f] | upload [f] | cat [f] | rm [f] | cd [/ruta] | mv [a] [b] | replace [f] "A" "B" | append [f] "línea" | login | ps | kill [PID] | analyze | solve | shell | clear | disconnect|dc | reboot -i | openCDTray | closeCDTray | addNote "texto" | save | FirstTimeInit

---

## 11) Apéndice B — Port-crackers por puerto (memoria)
21 FTP → FTPBounce / FTPSprint (DLC)
22 SSH → SSHcrack
25 SMTP → SMTPoverflow
80 HTTP → WebServerWorm
104 DICOM/medtech (KBT) → KBT_PortTest
1433 MS-SQL → SQLBufferOverflow / SQL_MemCorrupt
443 HTTPS → SSLTrojan (DLC)
554 RTSP → RTSPCrack (DLC)
6881 Torrent → TorrentStreamInjector (DLC)
192 “Pacific Dedicated” → PacificPortcrusher (DLC)

---

# HACKNET — COMANDOS

<img src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/365450/header.jpg?t=1726271733" alt="Header" width="400"/>

---

## COMANDOS DEL TERMINAL 

**help [PÁGINA]**
- Qué hace: Muestra la página de ayuda de comandos.
- Equivalencia real: `man`, `--help`.

**scp [FICHERO] [destino opcional]**
- Qué hace: Copia un fichero del equipo remoto al local (por defecto a /bin).
- Equivalencia real: `scp`, `sftp get`.

**scan**
- Qué hace: Descubre y añade a tu mapa los hosts enlazados desde el equipo conectado.
- Equivalencia real: Enumeración/redescubrimiento de nodos accesibles (osint/redir), similar a mapear relaciones o rutas.

**rm [FICHERO | *]**
- Qué hace: Borra el/los ficheros indicados.
- Equivalencia real: `rm`, `del` (borrado de archivos; *no* forense).

**ps**
- Qué hace: Lista procesos y PIDs activos.
- Equivalencia real: `ps`, `tasklist`.

**kill [PID]**
- Qué hace: Mata el proceso con el PID dado.
- Equivalencia real: `kill`, `taskkill`.

**cd [RUTA]**
- Qué hace: Cambia de directorio (ej.: `cd home`, `cd ..`, `cd /`).
- Equivalencia real: `cd`.

**mv [ORIGEN] [DESTINO]**
- Qué hace: Mueve o renombra ficheros.
- Equivalencia real: `mv`, `move`.

**connect [IP|NombreHost]**
- Qué hace: Conecta tu terminal a otro equipo.
- Equivalencia real: Apertura de sesión/conexión a servicio (p. ej. `ssh`/`telnet`/`nc` hacia un host).

**probe**
- Qué hace: Sonda el equipo: puertos activos y nivel de seguridad.
- Equivalencia real: `nmap -sV`/fingerprinting básico de servicios.

**exe**
- Qué hace: Lista ejecutables locales en /bin (incluye ocultos/embebidos).
- Equivalencia real: `ls ~/bin`, `which -a`.

**disconnect  (alias: dc)**
- Qué hace: Cierra la conexión actual.
- Equivalencia real: `exit`, cerrar sesión/terminal.

**cat [FICHERO]**
- Qué hace: Muestra el contenido de un fichero.
- Equivalencia real: `cat`, `type`.

**openCDTray  /  closeCDTray**
- Qué hace: Abre/Cierra la bandeja del CD del PC jugador si estás conectado a tu propio nodo.
- Equivalencia real: `eject` (control de dispositivo local).

**reboot [-i]**
- Qué hace: Reinicia el equipo conectado (instante con `-i`).
- Equivalencia real: `reboot`, `shutdown -r now`.

**replace [FICHERO] "texto_objetivo" "texto_nuevo"**
- Qué hace: Sustitución de texto dentro de un fichero.
- Equivalencia real: `sed -i`, `perl -pe`.

**analyze**
- Qué hace: Analiza el firewall; hay que repetirlo varias veces para revelar la solución.
- Equivalencia real: Fingerprinting/analítica de WAF/ACL (no exacto).

**solve [SOLUCIÓN_FIREWALL]**
- Qué hace: Intenta resolver el firewall para permitir tráfico UDP.
- Equivalencia real: Aplicar bypass/regla/técnica sobre WAF/ACL (conceptual).

**login**
- Qué hace: Pide usuario y password para autenticarte en el sistema.
- Equivalencia real: `ssh user@host` (autenticación).

**upload [RUTA_LOCAL/FICHERO]**
- Qué hace: Sube un fichero local al directorio actual del remoto.
- Equivalencia real: `scp put`, `sftp put`, `curl -T`.

**clear**
- Qué hace: Limpia la consola.
- Equivalencia real: `clear`, `cls`.

**addNote [TEXTO]**
- Qué hace: Añade una nota al sistema de notas.
- Equivalencia real: Tomar notas locales (sin paralelo de pentesting).

**append [FICHERO] [DATOS]**
- Qué hace: Añade una línea con [DATOS] al final de un fichero.
- Equivalencia real: `echo "…" >> fichero`.

**shell**
- Qué hace: Abre una shell remota con capacidades de sobrecarga de proxy y trampa IP.
- Equivalencia real: Shell remota/bind-reverse shell, DoS al proxy (conceptual).

**save!(SJN!*SNL8vAewew57WewJdwl89(*4;;;&!)@&(ak'^&#@J3KH@!* **
- Qué hace: Comando interno de guardado de partida.
- Equivalencia real: N/A (mecánica del juego).

**FirstTimeInitdswhupwnemfdsiuoewnmdsmffdjsklanfeebfjkalnbmsdakj**
- Qué hace: Comando interno de inicialización/boot y conexión a tu PC.
- Equivalencia real: N/A.

---

## EJECUTABLES (PORTCRACKERS / EXPLOITS DE PUERTO) <br>

Se lanzan escribiendo el nombre sin “.exe”. Muchos disparan la traza activa.
Entre paréntesis: puerto por defecto que abren/crackean.

**PortHack**
- Qué hace: Gana acceso admin si tienes suficientes puertos abiertos; ignora proxy activo; dispara traza.
- Equivalencia real: Paso final de explotación/privesc para root/NT AUTHORITY SYSTEM tras abrir vectores (RCE, creds, etc.).

**SecureShellCrack  (SSH, 22)**
- Qué hace: Abre el puerto SSH.
- Equivalencia real: Ataques a SSH (fuerza bruta/spray, exploit de servicio, claves comprometidas).

**FTP Bounce  (FTP, 21)**
- Qué hace: Abre el puerto FTP.
- Equivalencia real: Exploits/misconfigs FTP, credenciales por defecto; concepto “FTP bounce” histórico.

**SMTP Overflow  (SMTP, 25)**
- Qué hace: Abre el puerto SMTP.
- Equivalencia real: Desbordamiento/bug en servidor SMTP → RCE o bypass.

**Apache WebServer Worm  (HTTP, 80)**
- Qué hace: Abre el puerto HTTP.
- Equivalencia real: Exploit a servidor web (RCE/LFI/RFI/CVE), gusano web.

**SQL Memory Corruption Injector / SQLBufferOverflow  (MSSQL, 1433)**
- Qué hace: Abre el puerto SQL; bypass de proxy activo.
- Equivalencia real: Exploit/buffer overflow/SQLi hasta ejecución de código.

**KBT Port Tester  (Medical Services, 104)**
- Qué hace: Abre el servicio “médico”; no dispara traza.
- Equivalencia real: Exploit de servicio propietario; sonda/PoC específica.

**FTPSprint  (FTP, 21)  [Labyrinths]**
- Qué hace: Versión rápida de FTP Bounce (pensado también para 211 “Transfer” en código fuente).
- Equivalencia real: Variante optimizada del ataque a FTP.

**TorrentStreamInjector  (BitTorrent, 6881)  [Labyrinths]**
- Qué hace: Abre el puerto BitTorrent; bypass de proxy activo.
- Equivalencia real: Exploit/abuso de servicios P2P.

**SSLTrojan  (HTTPS, 443)  [Labyrinths]**
- Qué hace: Abre 443 atravesando otro puerto abierto (requiere uno: -s 22, -f 21, -w 80, -r 554).
- Uso: SSLTrojan 443 -f 21
- Equivalencia real: Pivot/encapsulado/túnel para alcanzar TLS via otro servicio (técnicas de chaining).

**PacificPortcrusher  (Pacific Dedicated, 192)  [Labyrinths]**
- Qué hace: Abre el servicio propietario “Pacific”.
- Equivalencia real: Exploit de servicio industrial/privado.

**RTSPCrack  (RTSP, 554)  [Extensiones]**
- Qué hace: Abre RTSP; bypass de proxy activo.
- Equivalencia real: Ataques a RTSP (auth bypass, overflow, CVEs).

---
## EJECUTABLES (MISC / UTILIDADES)

**FirstTimeInit / Save / Notes / Clock / HexClock / Clock v2 / Theme Switch / Tuneswap / Hacknet / WoWHack / NetmapOrganizer**
- Qué hacen: Utilidades de sistema/tema/reloj/notas/miniapps; QoL/UI.
- Equivalencia real: N/A (interfaz).

**ForkBomb**
- Qué hace: Satura RAM y crashea el sistema objetivo (o tuyo si lo ejecutas local).
- Equivalencia real: DoS por recursos (fork bomb), *no* uso ético salvo entornos controlados.

**Shell (mencionado arriba en comandos)**
- Qué hace: “Overload” (DoS a proxy) o “Trap” (crashear el que conecta a ti).
- Equivalencia real: DoS al proxy / honeypot trampa.

**Security Tracer**
- Qué hace: Muestra/gestiona el estado de la traza activa.
- Equivalencia real: Telemetría/alertas del SOC (analógico); monitor de detección.

**TraceKill**
- Qué hace: Detiene/mitiga la traza activa.
- Equivalencia real: Evasión de detección, anti-forensics (conceptual).

**Sequencer / ESequencer**
- Qué hace: Orquesta acciones en secuencia/automatiza pasos.
- Equivalencia real: Scripting/automatización (bash, Python, `ptas`, `sqlmap` automation, etc.).

**eOS Device Scanner**
- Qué hace: Escanea dispositivos eOS conectados (requiere admin).
- Equivalencia real: Descubrimiento/enum. de IoT/embedded (UPnP/MDNS, escaneo específico).

**DEC File Tracer**
- Qué hace: Traza archivos DEC, mostrando cabecera e IPs donde se cifraron.
- Equivalencia real: Forense de metadatos/encapsulado (analítico).

**Decypher Module**
- Qué hace: Descifra contenido DEC (con material adecuado).
- Equivalencia real: `gpg`/`openssl` (descifrado con claves).

**confloodEOS**
- Qué hace: Inunda/perturba dispositivos eOS (ataque de congestión).
- Equivalencia real: DoS a servicio IoT.

**KaguyaTrial / SignalScramble / ComShell / DNotes / MemoryDumpGenerator / MemForensics / GitTunnel / OpShell**
- Qué hacen (resumen):
  - KaguyaTrial: binario de pruebas (contenido de extensión).
  - SignalScramble: altera/señales (mecánica de extensión).
  - ComShell / OpShell: shells/cons. especiales (operativas).
  - DNotes: notas/documentación.
  - MemoryDumpGenerator: genera volcado de memoria.
  - MemForensics: analiza volcados.
  - GitTunnel: túnel/relé vía Git (C2/logística en extensión).
- Equivalencia real:
  - Volcados: `procdump`, `gcore`; análisis: Volatility/Redline.
  - Túneles/C2: `chisel`, `ssh -L/-R`, `iodine`, *git over HTTP(S)* para exfil/pivot.
  - Shells especiales: frameworks C2/pty mejoradas (p. ej. `socat`/`winpty`/implant).

---

## NOTAS RÁPIDAS DE USO (EN JUEGO)
- Flujo típico: probe → (abrir puertos con portcrackers) → analyze/solve firewall si existe → PortHack → login/shell → scp/upload según objetivo.
- Muchos ejecutables disparan la traza: gestiona tiempo (Security Tracer/TraceKill/Shell-Overload).
- Algunos ejecutables requieren DLC/Extensiones (marcados).
- Borrado de huellas en juego: `rm *` en /log del host; en la vida real, borrar logs es anti-forense y suele ser ilegal fuera de entornos autorizados.

---

## MAPEO BREVE A HERRAMIENTAS REALES (REFERENCIAL)
- Descubrimiento/puertos: `nmap`, `masscan`, `naabu`
- Autenticación/credenciales: `ssh`, `hydra`, `medusa`
- Web: `burpsuite`, `sqlmap`, `nikto`
- Explotación: `metasploit`, PoC CVEs, RCE específicas
- Movimiento/pivot/túnel: `ssh -D/-L/-R`, `socat`, `chisel`, `iptables`, `proxychains`
- Exfil/copia: `scp`/`sftp`/`rsync`, `curl`

---
- Forense/memoria: `Volatility`, `rekall`, `procdump`
- Evasión/defensa: SIEM/EDR awareness (teórico); *siempre* con permiso y en entornos controlados
