#!/usr/bin/env python3

import socket

host = "127.0.0.1"
port = 23

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

result = s.connect_ex((host, port))
print(result)
s.close
