#!/usr/bin/env python3
import re
import subprocess
import time
from collections import defaultdict
from datetime import datetime

LOG_FILE = "/var/log/auth.log"  # Cambiar si hace falta

INTENTOS_MAX = 5      # Intentos fallidos para bloquear
BLOQUEO_DURACION = 3600  # En segundos (1 hora)

fallos_ip = defaultdict(int)
ips_bloqueadas = {}

regex_fallo = re.compile(r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)")

def bloquear_ip(ip):
    print(f"[{datetime.now()}] Bloqueando IP {ip}")
    subprocess.run(["iptables", "-I", "INPUT", "-s", ip, "-j", "DROP"])
    ips_bloqueadas[ip] = time.time()

def desbloquear_ip(ip):
    print(f"[{datetime.now()}] Desbloqueando IP {ip}")
    subprocess.run(["iptables", "-D", "INPUT", "-s", ip, "-j", "DROP"])
    ips_bloqueadas.pop(ip, None)
    fallos_ip.pop(ip, None)

def revisar_bloqueos():
    ahora = time.time()
    para_desbloquear = [ip for ip, t in ips_bloqueadas.items() if ahora - t > BLOQUEO_DURACION]
    for ip in para_desbloquear:
        desbloquear_ip(ip)

def monitor_logs():
    print(f"[ * ] Iniciando monitorización de logs: {LOG_FILE}")
    with open(LOG_FILE, "r") as f:
        # Saltar al final del archivo
        f.seek(0,2)

        while True:
            linea = f.readline()
            if not linea:
                revisar_bloqueos()
                time.sleep(1)
                continue

            match = regex_fallo.search(linea)
            if match:
                ip = match.group(1)
                if ip in ips_bloqueadas:
                    continue

                fallos_ip[ip] += 1
                print(f"[{datetime.now()}] Intento fallido #{fallos_ip[ip]} desde {ip}")
                if fallos_ip[ip] >= INTENTOS_MAX:
                    bloquear_ip(ip)

if __name__ == "__main__":
    monitor_logs()
