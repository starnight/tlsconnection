#!/bin/env python3

import socket
import ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations("server.crt")
context.check_hostname = False

cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssock = context.wrap_socket(cli_sock)
ssock.connect(('127.0.0.1', 8443))

ssock.send("test".encode())
data = ssock.recv(256)
print(data.decode())
ssock.close()
