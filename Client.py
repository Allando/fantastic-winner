#!/bin/python

import socket

HOST = "127.0.0.1"
PORT = 6789

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
sock.connect(server_address)
print('connected to %s port %s' % server_address)

# Send data
message = "GET / HTTP/1.1\r\nHost:{}:{}\r\n".format(HOST, PORT)
m = True
while m is True:
    print('sending "%s"' % message)

    sock.sendall(message.encode())

# Look for the response
amount_received = 0
amount_expected = len(message)

while amount_received < amount_expected:
    data = sock.recv(1024)
    amount_received += len(data)
    print('received: {}'.format(data))

sock.close()
