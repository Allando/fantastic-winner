import socket
import time

with open("ServerLog.txt", "a") as f:
    
    
    def write_and_print(a):
        print(a)
        f.write(a)

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = ('localhost', 6789)
    write_and_print('starting up on %s port %s' % server_address)
    #print ( 'starting up on %s port %d' % server_address)
    #f.write('starting up on %s port %d' % server_address)
    sock.bind(server_address)

    #Listen for incoming connections
    sock.listen(1)

    while True:
        #wait for connection
        write_and_print('Waiting for connection')
        #print ( 'waiting for connection...')
        #f.write('waiting for connection...')
        connection, client_address = sock.accept()

        try:
            write_and_print('Connection from {}'.format( client_address))
            #print ( 'connection from', client_address)
            #f.write('connection from', client_address)

            #receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(1024)
                write_and_print('Received {}'.format(data))
                #print ('received "%s" ' % data)
                #f.write('received "%s" ' % data)
                if data:
                    write_and_print('Sending data back to the client')
                    #print ( 'sending data back to the client')
                    #f.write('sending data back to the client')
                else:
                    write_and_print('No more data from {}'.format(client_address))
                    #print('no more data from', client_address)
                    #f.write('no more data from', client_address)
                    break
        finally:
            #Clean up the connection
            connection.close()

