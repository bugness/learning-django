import socket
import threading

def client_handler(conn, addr):
    print(addr)
    while True:
        data = conn.recv(1024)
        if data.decode().startswith('close'): break
        conn.send(data)
    conn.close()

def run():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', 2222))
    s.listen(10)

    while True:
        conn, addr = s.accept()
        t = threading.Thread(target=client_handler, args=(conn, addr))
        t.start()

    s.close()


if __name__ == '__main__':
    run()