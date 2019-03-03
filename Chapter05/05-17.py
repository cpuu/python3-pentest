#!/usr/bin/env python3

import socket

hosts = ["127.0.0.1"]

for host in hosts:
	for port in range(0, 1024):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		result = s.connect((host, port))
		if result == 0:
			print("[*]Port " + str(port) + " open!")

		s.close()
