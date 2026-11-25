# base tcp server code from https://realpython.com/python-sockets/#tcp-sockets
import socket

HOST = "127.0.0.1"
PORT = 5467

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
