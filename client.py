# base tcp server code from https://realpython.com/python-sockets/#tcp-sockets
import socket

HOST = "127.0.0.1"
PORT = 5467

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Received {data!r}")
