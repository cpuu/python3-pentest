#!/usr/bin/env python3

import os
import socket
from struct import *

os.system("ifconfig eth0 promisc")

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

while True:

	data = s.recv(65565)

	#IP Header
	ip_header = data[0:20]
	ip_header = unpack("!BBHHHBBH4s4s", ip_header)

	version_ip_header_length = ip_header[0]
	version = version_ip_header_length >> 4
	ip_header_length = version_ip_header_length & 0xF
	ip_header_length = ip_header_length * 4

	#UDP Header
	udp_header = data[ip_header_length:ip_header_length + 8]
	udp_header = unpack("!HHHH", udp_header)

	source_port = udp_header[0]
	destination_port = udp_header[1]
	length = udp_header[2]
	checksum = udp_header[3]

	print("UDP Header")
	print("Source Port Number:", str(source_port))
	print("Destination Port Number:", str(destination_port))
	print("Length:", str(length))
	print("Checksum:", str(checksum))
	print()

	#UDP Payload
	udp_header_length = 8
	header_size = ip_header_length + udp_header_length
	payload_data_size = len(data) - header_size
	udp_payload_data = data[header_size:]

	print("UDP Payload")
	print("Payload Data:", str(udp_payload_data))
	print()
