#!/usr/bin/env python3
import socket
import threading
import queue
import argparse
from datetime import datetime

# ---------------------------
# CONFIGURACIÓN DEL ESCANEO
# ---------------------------
print_lock = threading.Lock()

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Tiempo de espera por puerto
        result = sock.connect_ex((target, port))
        if result == 0:
            with print_lock:
                print(f"[+] Puerto abierto: {port}")
        sock.close()
    except Exception:
        pass

def worker():
    while not q.empty():
        port = q.get()
        scan_port(target, port)
        q.task_done()

# ---------------------------
# ARGUMENTOS DEL SCRIPT
# ---------------------------
parser = argparse.ArgumentParser(description="Zya Recon - Scanner de Puertos Avanzado")
parser.add_argument("host", help="Host o dirección IP objetivo")
parser.add_argument("-m", "--modo", choices=["rapido", "completo"], default="rapido",
                    help="Modo de escaneo: rapido (1-1024) o completo (1-65535)")
parser.add_argument("-t", "--threads", type=int, default=100, help="Número de hilos (default 100)")
args = parser.parse_args()

target = socket.gethostbyname(args.host)
print(f"\n[ * ] Iniciando escaneo en {target}")
print(f"[ * ] Modo: {args.modo.upper()} | Hilos: {args.threads}")
print(f"[ * ] Hora de inicio: {datetime.now()}\n")

# ---------------------------
# RANGO DE PUERTOS
# ---------------------------
q = queue.Queue()
if args.modo == "rapido":
    puerto_final = 1024
else:
    puerto_final = 65535

for port in range(1, puerto_final + 1):
    q.put(port)

# ---------------------------
# INICIAR ESCANEO
# ---------------------------
for _ in range(args.threads):
    thread = threading.Thread(target=worker)
    thread.daemon = True
    thread.start()

q.join()
print(f"\n[ * ] Escaneo finalizado: {datetime.now()}")
