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

#TCP Header
tcp_header = data[34:54]
tcp_header = struct.unpack("!HHLLBBHHH", tcp_header)

source_port = tcp_header[0]
destination_port = tcp_header[1]
sequence_number = tcp_header[2]
acknowledgment_number = tcp_header[3]
offset_reserved = tcp_header[4]
tcp_header_length = offset_reserved >> 4
window = tcp_header[5]
checksum = tcp_header[6]
urgent_pointer = tcp_header[7]

print("TCP Header")
print("Source Port Number:", str(source_port))
print("Destination Port Number:", str(destination_port))
print("Sequence Number:", str(sequence_number))
print("Acknowledgment Number:", str(acknowledgment_number))
print("TCP Header Length:", str(tcp_header_length))
print("Window:", str(window))
print("Checksum:", str(checksum))
print("Urgent Pointer:", str(urgent_pointer))
print()

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
