#!/usr/bin/env python3

import socket
import struct
import binascii

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

data = s.recv(65565)

#Ethernet Header
ethernet_header = data[0:14]
ethernet_header = struct.unpack("!6s6s2s", ethernet_header)

source_mac_address = (binascii.hexlify(ethernet_header[1])).decode()
desination_mac_address = (binascii.hexlify(ethernet_header[0])).decode()

print("Source MAC Address:", source_mac_address)
print("Desination MAC Address:", desination_mac_address)
print()

#IP Header
ip_header = data[14:34]
ip_header = struct.unpack("!BBHHHBBH4s4s", ip_header)

source_ip_address = socket.inet_ntoa(ip_header[8])
destination_ip_address = socket.inet_ntoa(ip_header[9])

print("Source IP Address:", source_ip_address)
print("Destination IP Address:", destination_ip_address)
print()

#TCP Header
tcp_header = data[34:54]
tcp_header = struct.unpack("!HHLLBBHHH", tcp_header)

source_port_number = tcp_header[0]
destination_port_number = tcp_header[1]

print("Source Port Number:", source_port_number)
print("Destination Port Number:", destination_port_number)

#TCP Payload
ethernet_header = 14
ip_header = 20
tcp_header = 20

header_size = ethernet_header + ip_header + tcp_header
payload_data_size = len(data) - header_size
tcp_payload_data = data[header_size:]

print("TCP Payload Data")
print("TCP Payload Data:", str(tcp_payload_data))
print()
