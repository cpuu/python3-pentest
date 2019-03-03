#!/usr/bin/env python3

import socket

protocols = ["ftp", "ssh", "telnet", "smtp", "http", "pop3"]
for protocol in protocols:
     print("the port number for", protocol, "is", socket.getservbyname(protocol, "tcp"))

protocols = ["domain", "snmp"]
for protocol in protocols:
     print("the port number for", protocol, "is", socket.getservbyname(protocol, "udp"))

numbers = (20, 21, 22, 23, 25, 53, 67, 68, 80, 110, 161, 162)
for number in numbers:
     print("the service for", number, "is", socket.getservbyport(number))

print(socket.gethostname())
print(socket.gethostbyname(socket.gethostname()))
print(socket.gethostbyname("google.com"))
