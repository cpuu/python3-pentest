#!/usr/bin/env python3

import socket

host = "www.google.com"
port = 80

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

address = socket.gethostbyname(host)

sock.connect((address, port))

print("Socket Connected to {} on {}".format(host, address))

message = b"GET / HTTP/1.1\r\n\r\n"

sock.sendall(message)

data = sock.recv(65565)

print(data)

sock.close()
