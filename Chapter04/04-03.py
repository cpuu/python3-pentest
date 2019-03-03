#!/usr/bin/env python3

import socket

host = "127.0.0.1"
port = 12345

parent = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
parent.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

parent.bind((host, port))

parent.listen(10)

(child, address) = parent.accept()

(data, address) = child.recvfrom(65565)
print("received {} bytes from {}".format(len(data), address))

child.close()
parent.close()
