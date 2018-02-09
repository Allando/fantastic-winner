#!/usr/bin/python3           # This is server.py file
import socket                                         

HOST = socket.gethostname()
PORT = 6789
BUFF = 1024


def main():
    # create a socket object
    serversocket = socket.socket()                            

    # bind to the port
    serversocket.bind((HOST, PORT))                                  

    # queue up to 5 requests
    serversocket.listen(5)                                           

    while True:
        # establish a connection
        clientsocket, addr = serversocket.accept()      

        print("Got a connection from %s" % str(addr))
    
        msg = 'Thank you for connecting'+ "\r\n"
        clientsocket.send(msg.encode('ascii'))
        clientsocket.close()

main()
