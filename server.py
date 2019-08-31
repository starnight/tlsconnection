#!/bin/env python3

import socket
import ssl

class server:
    def __init__(self):
        self.context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        self.context.load_cert_chain("server.crt", "server.key")
        self.svr_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def deal_cli(self, ssock):
        data = ssock.recv(256)
        print("Client {}: {}".format(ssock.getpeername(), data.decode()))
        data = "Server got {}".format(data.decode())
        ssock.send(data.encode())

    def run(self):
        self.svr_sock.bind(('127.0.0.1', 8443))
        self.svr_sock.listen(5)

        while True:
            cli_sock, addr = self.svr_sock.accept()
            ssock = self.context.wrap_socket(cli_sock, server_side=True)

            try:
                self.deal_cli(ssock)
            finally:
                ssock.shutdown(socket.SHUT_RDWR)
                ssock.close()

    def __del__(self):
        self.svr_sock.close()

if __name__ == '__main__':
    svr = server()
    print("Server start")
    svr.run()
