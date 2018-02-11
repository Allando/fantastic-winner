#!/bin/python

import socket
import time


def main():
    PORT = 6789
    BUFF = 1024
    msg = "HTTP/1.1 200 OK\r\n"

    http_response = """ HTTP \ 1.1 200 OK\r\n """

    # Create a TCP/IP socket
    sock = socket.socket()

    # Bind the socket to the port
    server_address = ('', PORT)
    sock.bind(server_address)
    write_and_print('Starting up on %s port %s' % server_address)
    
    # Listen for incoming connections
    sock.listen(1)

    while True:
        # Wait for connection
        write_and_print('Waiting for connection')
        connection, client_address = sock.accept()

        try:
            write_and_print('Connection from {}'.format(client_address))
            data = connection.recv(BUFF)
            write_and_print('Received {}'.format(data.decode('utf-8')))
            
            if data:
                connection.sendall(bytes(http_response, 'utf-8'))
            else:
                write_and_print('No more data from {}'.format(client_address))
                break
        
        finally:
            # Clean up the connection
            connection.close()


def write_and_print(a):
    """
    Prints a to terminal as well as writes a to file
    """
    with open("ServerLog.txt", "a") as f:
        print(a)
        current_time = time.asctime(time.localtime(time.time()))
        f.write('[{}] '.format(current_time) + a + "\n")


if __name__ == '__main__':
    main()

