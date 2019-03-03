#!/usr/bin/env python3

import socket

host = "www.google.com"
port = 80

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

address = socket.gethostbyname(host)

sock.connect((address, port))

print("Socket Connected to {} on {}".format(host, address))

sock.close()
