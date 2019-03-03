#!/usr/bin/env python3

import socket

host = "127.0.0.1"
port = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.connect((host, port))

message = b"This is the message."

sock.sendto(message, (host, port))
print("sending {}".format(message))

sock.close()
