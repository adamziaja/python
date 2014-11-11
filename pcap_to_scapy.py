#!/usr/bin/env python
# -*- coding: utf-8 -*-

# PCAP to Scapy

# (C) 2014 Adam Ziaja <adam@adamziaja.com> http://adamziaja.com

from scapy.all import *
from termcolor import colored # sudo apt-get update && sudo apt-get install -y python-termcolor

i = 0

def Handler(pkt):
    #print pkt.show()
    print colored(pkt.summary(), 'green')
    print colored(pkt.command(), 'yellow')
    global i
    i += 1
    pkt.pdfdump(filename=str(i) + ".pdf") # sudo apt-get update && sudo apt-get install -y python-pyx

sniff(offline="file.pcap", prn=Handler) # file.pcap
