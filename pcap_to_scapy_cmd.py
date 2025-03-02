#!/usr/bin/env python3
# PCAP to Scapy commands
# (C) 2014,2025 Adam Ziaja <adam@adamziaja.com> http://adamziaja.com

from scapy.all import *

def Handler(pkt):
    #print(pkt.show())
    #print(pkt.summary())
    print(pkt.command())
    print(pkt.command()).hide_defaults()
    
sniff(offline=sys.argv[1], prn=Handler)
