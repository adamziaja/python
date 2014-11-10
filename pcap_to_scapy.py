#!/usr/bin/env python
# -*- coding: utf-8 -*-

# PCAP to Scapy

# (C) 2014 Adam Ziaja <adam@adamziaja.com> http://adamziaja.com

import sys
from scapy.all import *

i = 0

def Handler(pkt):
    #if pkt.haslayer(Dot11): # 802.11
        #if pkt.type == 0 and pkt.subtype == 8: # https://en.wikipedia.org/wiki/Beacon_frame
    print pkt.show()
    global i
    i += 1
    pkt.pdfdump(filename=str(i) + ".pdf")

sniff(offline="file.pcap", prn=Handler)
