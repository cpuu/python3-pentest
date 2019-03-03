#!/usr/bin/env python3

import socket
import struct
import binascii

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

data = s.recv(65565)
print(data)
print()

#Ethernet Header
ethernet_header = data[0:14]
ethernet_header = struct.unpack("!6s6s2s", ethernet_header)

desination_mac_address = (binascii.hexlify(ethernet_header[0])).decode()
source_mac_address = (binascii.hexlify(ethernet_header[1])).decode()
type = (binascii.hexlify(ethernet_header[2])).decode()

print("Desination MAC Address:", desination_mac_address)
print("Source MAC Address:", source_mac_address)
print("Type:", type)
print()
