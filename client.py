# base tcp server code from https://realpython.com/python-sockets/#tcp-sockets
import socket

HOST = "127.0.0.1"
PORT = 5467

pckt = [None] * 2

pckt[0] = input("Who will this message be from? ") # username
pckt[1] = input("Please type a message. ")         # message contents 

# TODO: make this server side
while len(pckt[0]) >= 12 or len(pckt[1]) > 256:
    print("ERR 40: MESSAGE TOO LONG")
    msg = input("Please type a message. ")

res = ",".join(pckt)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(bytes(res, "utf-8"))
    data = s.recv(1024)

print(f"Received {data!r}")
