import threading
import socket


def handle_conn(sock, addr):
    with sock:
        print(f'Connection from {addr}')
        while True:
            data = sock.recv(1024)
            if not data:
                break
            sock.sendall(data)


def connection(host: str, port: int) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        handlers = []
        while True:
            s.listen()
            sock, addr = s.accept()
            handlers.append(threading.Thread(target=handle_conn, args=(sock, addr)))
            handlers[-1].start()


