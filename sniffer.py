#!/usr/bin/env python
# -*- coding: utf-8 -*-

# sniffer (passive)

# (C) 2014 Adam Ziaja <adam@adamziaja.com> http://adamziaja.com

from scapy.all import *

def Handler(pkt):
    # your code
    print pkt.show()

sniff(iface="eth0", count=0, prn=Handler, store=0)
