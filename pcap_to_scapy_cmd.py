#!/usr/bin/env python
# -*- coding: utf-8 -*-

# PCAP to Scapy commands

# (C) 2014 Adam Ziaja <adam@adamziaja.com> http://adamziaja.com

from scapy.all import *

def Handler(pkt):
    #print pkt.show()
    #print pkt.summary()
    print pkt.command()
    
sniff(offline=sys.argv[1], prn=Handler)
