#!/usr/bin/env python
# -*- coding: utf-8 -*-

# PCAP to Scapy

# (C) 2014 Adam Ziaja <adam@adamziaja.com> http://adamziaja.com

from scapy.all import *

i = 0

def Handler(pkt):
    print pkt.summary()
    #print pkt.show()
    #print pkt.command()
    global i
    i += 1
    pkt.pdfdump(filename=str(i) + ".pdf") # sudo apt-get update && sudo apt-get install -y python-pyx

sniff(offline="file.pcap", prn=Handler) # file.pcap
