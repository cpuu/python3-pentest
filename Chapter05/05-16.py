#!/usr/bin/env python3

import nmap

nm = nmap.PortScanner()

nm.scan("127.0.0.1", "22")

for host in nm.all_hosts():
        print("Host: {} {}".format(host, nm["127.0.0.1"].hostname()))
        print("State: {}".format(nm["127.0.0.1"].state()))

for protocol in nm["127.0.0.1"].all_protocols():
        print("Protocol: {}".format(protocol))

local_port = list(nm["127.0.0.1"]["tcp"].keys())
local_port.sort()

for port in local_port:
	print("Port: {}".format(port))
	print("State: {}".format(nm["127.0.0.1"][protocol][port]["state"]))
