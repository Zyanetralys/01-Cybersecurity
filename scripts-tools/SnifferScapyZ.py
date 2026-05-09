#!/usr/bin/env python3
from scapy.all import sniff, TCP, IP, Raw
from datetime import datetime

def packet_callback(packet):
    if packet.haslayer(TCP) and packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        sport = packet[TCP].sport
        dport = packet[TCP].dport
        
        if packet.haslayer(Raw):
            payload = packet[Raw].load
            try:
                payload_text = payload.decode('utf-8', errors='ignore')
            except:
                payload_text = "<No legible payload>"
        else:
            payload_text = "<Sin payload>"
        
        print(f"\n[ {datetime.now()} ] Paquete capturado:")
        print(f"   {ip_src}:{sport} -> {ip_dst}:{dport}")
        print(f"   Payload: {payload_text[:100]}")  # Mostrar primeros 100 caracteres

def main():
    print("[ * ] Iniciando sniffer (Ctrl+C para parar)...")
    sniff(filter="tcp", prn=packet_callback, store=False)

if __name__ == "__main__":
    main()
