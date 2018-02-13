#!/usr/bin/python3

import getopt
import socket
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], 's:p:f:h', ['src=', 'port=', 'file=', 'help'])
except getopt.GetoptError as e:
    print(e)
    exit(2)

for opt, arg in opts:
    if opt in ('-h', '--help'):
        exit(2)
    elif opt in ('-d', '--destination'):
        HOST = arg
    elif opt in ('-p', '--port'):
        PORT = arg
    elif opt in ('-f', '--file'):
        FILE = arg
    else:
        exit(2)

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

