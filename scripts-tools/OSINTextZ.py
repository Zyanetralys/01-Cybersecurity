#!/usr/bin/env python3
import whois
import requests
import socket
import argparse
import concurrent.futures
from datetime import datetime

# Diccionario básico de subdominios (ampliable!!)
SUBDOMS = [
    "www", "mail", "ftp", "dev", "test", "portal", "api", "blog",
    "staging", "vpn", "admin", "secure", "beta", "db", "shop"
]

# ---------------------------
# WHOIS INFO
# ---------------------------
def get_whois_info(domain):
    try:
        info = whois.whois(domain)
        print("\n[+] Información WHOIS:")
        for key, value in info.items():
            print(f"   {key}: {value}")
    except Exception as e:
        print(f"[-] Error obteniendo WHOIS: {e}")

# ---------------------------
# SUBDOMINIOS
# ---------------------------
def check_subdomain(sub, domain):
    url = f"{sub}.{domain}"
    try:
        ip = socket.gethostbyname(url)
        return url, ip
    except:
        return None

def scan_subdomains(domain):
    print("\n[+] Buscando subdominios...")
    found = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        results = executor.map(lambda s: check_subdomain(s, domain), SUBDOMS)
        for res in results:
            if res:
                found.append(res)
    if found:
        print("   Subdominios encontrados:")
        for s, ip in found:
            print(f"   - {s} -> {ip}")
    else:
        print("   Ninguno encontrado con diccionario básico.")
    return found

# ---------------------------
# MAIN
# ---------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Zya Recon - OSINT Extractor")
    parser.add_argument("domain", help="Dominio objetivo (ejemplo: ejemplo.com)")
    args = parser.parse_args()
    target = args.domain

    print(f"\n[ * ] Iniciando OSINT contra {target}")
    print(f"[ * ] Hora de inicio: {datetime.now()}")
    
    get_whois_info(target)
    scan_subdomains(target)

    print(f"\n[ * ] OSINT finalizado: {datetime.now()}")
