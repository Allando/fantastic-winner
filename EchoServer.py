import socket
import time

with open("ServerLog.txt", "a") as f:

    def write_and_print(a):
        """
        Prints a to terminal as well as writes a to file
        """
        print(a)
        current_time = time.asctime(time.localtime(time.time()))
        f.write('[{}] '.format(current_time) + a + "\n")   

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = ('localhost', 6789)
    write_and_print('Starting up on %s port %s' % server_address)
    sock.bind(server_address)

    #Listen for incoming connections
    sock.listen(1)

    while True:
        #wait for connection
        write_and_print('Waiting for connection')
        connection, client_address = sock.accept()

        try:
            write_and_print('Connection from {}'.format( client_address))

            #receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(1024)
                write_and_print('Received {}'.format(data))
                print (data)
                http_response ="""\
            HTTP/1.1 200 OK
            
            Hello
            """
                if data:
                    write_and_print('Sending data back to the client')
                else:
                    write_and_print('No more data from {}'.format(client_address))
                    break
        finally:
            #Clean up the connection
            connection.close()


