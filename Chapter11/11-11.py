#!/usr/bin/env python3

import socket
import struct
import binascii

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

data = s.recv(65565)

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

#IP Header
ip_header = data[14:34]
ip_header = struct.unpack("!BBHHHBBH4s4s", ip_header)

version_ip_header_length = ip_header[0]
version = version_ip_header_length >> 4
ip_header_length = version_ip_header_length & 0xF
ip_header_length = ip_header_length * 4
ttl = ip_header[5]
protocol = ip_header[6]
ip_source_address = socket.inet_ntoa(ip_header[8])
ip_destination_address = socket.inet_ntoa(ip_header[9])

print("IP Header")
print("Version:", str(version))
print("IP Header Length:", str(ip_header_length))
print("TTL:", str(ttl))
print("Protocol:", str(protocol))
print("Source IP Address:", str(ip_source_address))
print("Destination IP Address:", str(ip_destination_address))
print()

#ICMP Header
icmp_header = data[34:42]
icmp_header = struct.unpack("!BBHHH", icmp_header)

type = icmp_header[0]
code = icmp_header[1]
checksum = icmp_header[2]
id = icmp_header[3]
seq = icmp_header[4]

print("ICMP Header")
print("Type:", str(type))
print("Code:", str(code))
print("Checksum:", str(checksum))
print("ID:", str(id))
print("Sequence:", str(seq))
print()

#ICMP Payload
ethernet_header = 14
ip_header = 20
icmp_header = 8

header_size = ethernet_header + ip_header + icmp_header
payload_data_size = len(data) - header_size
icmp_payload_data = data[header_size:]

print("ICMP Payload")
print("Payload Data:", str(icmp_payload_data))
print()
