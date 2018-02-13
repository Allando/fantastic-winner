#!/usr/bin/python3

import socket

HOST = '127.0.0.1'
PORT = 6789
REQUEST = "GET / HTTP/1.1\r\nHost:{}:{}\r\n".format(HOST, PORT)

print("[*] Connecting to {}:{}".format(HOST, PORT))
# create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connection to hosocktname on the port.
sock.connect((HOST, PORT))
print("[*] Connected to {}:{}".format(HOST, PORT))

sock.sendall(REQUEST.encode())

# Receive no more than 1024 bytesock
msg = sock.recv(1024)

sock.close()
print(msg.decode('utf-8'))
