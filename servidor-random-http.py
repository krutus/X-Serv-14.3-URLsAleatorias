#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import random

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind((socket.gethostname(), 1234))
mySocket.listen(8)


while True:
    print 'Waiting for connections'
    (recvSocket, address) = mySocket.accept()
    print 'HTTP request received:'
    print recvSocket.recv(1024)
    NewNum = random.randrange(1000000)
    recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                    "<html>" +
                    "<body>" + "Hola. " +
                    "<a href='" + str(NewNum) + "'>Dame Otra</a>" +
                    "</body></html>" +
                    "\r\n")
    recvSocket.close()
