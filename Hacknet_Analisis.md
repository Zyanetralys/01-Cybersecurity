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
• Auto-completado con TAB (comandos y nombres).
• Editar ficheros: ‘cat’ + ‘replace’/‘append’. Si da “Assuming active flag file”, usa la forma completa de replace con nombre de fichero.
• Tras comprometer, ‘scan’ SIEMPRE para descubrir extensiones/eOS.

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
• “PortHack” requiere N puertos abiertos (según el host) antes de otorgar root. 
• Proxies: abre shells en otros nodos y pulsa “Overload” para bajarlos; ‘Trap’ cambia tu IP si te rastrean.
• Firewalls: ‘analyze’ → ‘solve’ (puzzle de colores/ritmos/figuras). Lanza solve al ritmo correcto.

---

## 4) eOS (ePhones/ePads): patrón
1. Compromete el PC vinculado (SSH/FTP/… → PortHack).
2. Ejecuta ‘eosDeviceScan.exe’ para listar el dispositivo.
3. ‘connect’ al ePhone/ePad → ‘login’ con admin / alpine (por defecto).
4. Entra a /eos/mail o /eos/notes para extraer lo que pidan (p.ej., *.act). 
5. Limpia logs en ambos lados si procede.

---


## 5) Walkthrough táctico
• Inicio (Bit): recupera x-server.sys si Naix te rompe el escritorio: cd /log → IP → connect → SSHcrack → PortHack → scp /sys/x-server.sys → reboot -i.
• Entropy: baja FTPBounce y SMTPoverflow; usa proxies/shell para sobrecargar; no borres logs locales antes del hack de “Aggression must be punished” (los necesitarás para la trama de Naix).
• Naix & /el: venganza (WebServerWorm), acceso al /el Message Board, Santuario Polar (4 pruebas → IP compuesto).
• CSEC: invitación (gauntlets), CFC cadena, “Ghosting the Vault” (Decypher), “Through the Spyglass” (DECHead), red line (cambia IP en ISP Management), “Project Junebug” (KBT_PortTest y marcapasos, 104).
• Final de Bit: TraceKill → cadena EnTech (Prometheus/Romulus) → Sequencer + múltiples shells → purge de archivos en backups.

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

Fin de guía.

---
