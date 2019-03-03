#!/usr/bin/env python3

import socket
import struct
import binascii

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0806))

data = s.recv(65565)

#Ethernet Header
ethernet_header = data[0:14]
ethernet_header = struct.unpack("!6s6s2s", ethernet_header)

source_mac_address = (binascii.hexlify(ethernet_header[1])).decode()
desination_mac_address = (binascii.hexlify(ethernet_header[0])).decode()
type = (binascii.hexlify(ethernet_header[2])).decode()

print("Source MAC Address:", source_mac_address)
print("Desination MAC Address:", desination_mac_address)
print("Type:", type)
print()

#ARP Header
arp_header = data[14:42]
arp_header = struct.unpack("!2s2s1s1s2s6s4s6s4s", arp_header)

hardware_type = (binascii.hexlify(arp_header[0])).decode()
protocol_type = (binascii.hexlify(arp_header[1])).decode()
hardware_size = (binascii.hexlify(arp_header[2])).decode()
protocol_size = (binascii.hexlify(arp_header[3])).decode()
op_code = (binascii.hexlify(arp_header[4])).decode()
source_mac_address = (binascii.hexlify(arp_header[5])).decode()
source_ip_address = socket.inet_ntoa(arp_header[6])
desination_mac_address = (binascii.hexlify(arp_header[7])).decode()
destination_ip_address = socket.inet_ntoa(arp_header[8])

print("Hardware Type:", hardware_type)
print("Protocol Type:", protocol_type)
print("Hardware Size:", hardware_size)
print("Protocol Size:", protocol_size)
print("OP Code:", op_code)
print("Source MAC Address:", source_mac_address)
print("Source IP Address:", source_ip_address)
print("Desination MAC Address:", desination_mac_address)
print("Destination IP Address:", destination_ip_address)
print()
