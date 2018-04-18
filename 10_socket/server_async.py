#!/usr/bin/python3

import asyncore
import socket
import sys

class EchoHandler(asyncore.dispatcher_with_send):
    def headle_read(self):
        data = self.recv(8192)
        if data:
            self.send(data)


class EchoServer(asyncore.dispatcher):
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accept(self):
        pair = self.accpet()
        if pair is not None:
            sock, addr = pair
            print('Incoming connection from {}'.format(repr(addr)))
            handler = EchoHandler(sock)

if __name__=="__main__":
    server = EchoServer('localhost', 8080)
    asyncore.loop()


























    
