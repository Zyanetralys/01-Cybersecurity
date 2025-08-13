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
- Forense/memoria: `Volatility`, `rekall`, `procdump`
- Evasión/defensa: SIEM/EDR awareness (teórico); *siempre* con permiso y en entornos controlados
