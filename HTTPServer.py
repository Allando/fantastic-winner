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
    
    logger('Starting connection on port {}...'.format(PORT))
    while True:
        conn, addr = sock.accept()
        try:
            request = conn.recv(1024)
            logger("Request: {}".format(request))
            filename = request.split()[1]
            logger("Filename: {}".format(filename))
            if filename == b'' or filename == b'/':
                f = open('index.html')
                outputdata = f.read()
                logger(outputdata)
                conn.send(bytes('\nHTTP/1.1 200 OK\n\n', 'utf-8'))
                conn.send(bytes(outputdata, 'utf-8'))
                f.close()
            else:
                f = open(filename[1:])
                outputdata = f.read()
                logger(outputdata)
                conn.send(bytes('\nHTTP/1.1 200 OK\n\n', 'utf-8'))
                conn.send(bytes(outputdata, 'utf-8'))
                f.close()
                logger(request.decode('utf-8'))
        except IOError:
            logger("404 Not Found")
            conn.send(bytes('\HTTP/1.1 404 Not Found\n\n', 'utf-8'))
        finally:
            conn.close()


def logger(a):
    """
    Prints a to terminal as well as writes a to file
    """
    print(a)
    with open("ServerLog.txt", "a") as f:
        current_time = time.asctime(time.localtime(time.time()))
        f.write('[{}] '.format(current_time) + a + "\n")


if __name__ == '__main__':
    main()
