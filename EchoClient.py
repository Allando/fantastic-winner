import socket


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 6789)
print ( 'connecting to %s port %s' % server_address)
sock.connect(server_address)



# Send data

message = input("200 OK! Hello, there!\n")
m = True
while m is True:
    message = input("- ")

    print( 'sending "%s"' % message)

    sock.sendall(message.encode())

# Look for the response
amount_received = 0
amount_expected = len(message)

while amount_received < amount_expected:
    data = sock.recv(1024)
    amount_received += len(data)
    print ('received "%s"' % data)


# finally:
#     print ( 'closing socket')
#     sock.close()