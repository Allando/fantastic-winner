import socket
import time

with open("ServerLog.txt", "a") as f:

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = ('localhost', 6789)
    print ( 'starting up on %s port %d' % server_address)
    f.write('starting up on %s port %d' % server_address)
    sock.bind(server_address)

    #Listen for incoming connections
    sock.listen(1)

    while True:
        #wait for connection
        print ( 'waiting for connection...')
        f.write('waiting for connection...')
        connection, client_address = sock.accept()

        try:
            print ( 'connection from', client_address)
            f.write('connection from', client_address)

            #receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(1024)
                print ('received "%s" ' % data)
                f.write('received "%s" ' % data)
                if data:
                    print ( 'sending data back to the client')
                    f.write('sending data back to the client')
                else:
                    print('no more data from', client_address)
                    f.write('no more data from', client_address)
                    break
        finally:
            #Clean up the connection
            connection.close()
