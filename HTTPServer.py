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
        try:
            request = conn.recv(1024)
            print (request, '::', request.split()[0],':',request.split()[1])
            filename = request.split()[1]
            print(filename, '||', filename[1:])
            f = open(filename[1:])
            outputdata = f.read()
            print(outputdata)
            conn.send(bytes('\nHTTP/1.1 200 OK\n\n', 'utf-8'))
            conn.send(bytes(outputdata, 'utf-8'))
            conn.close()
            write_and_print(request.decode('utf-8'))
        except IOError:
            print("404 Not Found")
            conn.send(bytes('\HTTP/1.1 404 Not Found\n\n', 'utf-8'))
#        http_response = """\
#               HTTP/1.1 200 OK
#
 #
  #              Hello, World
 #               """
  #      conn.sendall(bytes(http_response, 'utf-8'))
   #     conn.close()


def write_and_print(a):
    """
    Prints a to terminal as well as writes a to file
    """
    with open("ServerLog.txt", "a") as f:
        current_time = time.asctime(time.localtime(time.time()))
        f.write('[{}] '.format(current_time) + a + "\n")


main()
