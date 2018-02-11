#!/bin/python

import socket
import time


def main():
    HOST = ''
    PORT = 6789

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(1)
    
    write_and_print('Serving HTTP on port {}...'.format(PORT))
    while True:
        conn, addr = sock.accept()
        request = conn.recv(1024)
        
        write_and_print(request.decode('utf-8'))

        http_response = """\
                HTTP/1.1 200 OK 
                
                
                Hello, World
                """
        conn.sendall(bytes(http_response, 'utf-8'))
        conn.close()


def write_and_print(a):
    """
    Prints a to terminal as well as writes a to file
    """
    with open("ServerLog.txt", "a") as f:
        current_time = time.asctime(time.localtime(time.time()))
        f.write('[{}] '.format(current_time) + a + "\n")


main()
