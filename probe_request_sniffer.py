#!/usr/bin/env python
# -*- coding: utf-8 -*-

# WiFi probe request sniffer (passive)

# (C) 2014 Adam Ziaja <adam@adamziaja.com> http://adamziaja.com

import sys
from scapy.all import *

manuf = open("manuf.txt").read() # curl -s "https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob_plain;f=manuf;hb=HEAD" > manuf.txt
unique_probe = []

def Handler(pkt):
    if pkt.haslayer(Dot11): # 802.11
        if pkt.type == 0 and pkt.subtype == 4: # mgmt, probe request
            ssid_mac = pkt.info + " " + pkt.addr2
            if ssid_mac not in unique_probe and len(pkt.info) > 0:
                unique_probe.append(pkt.info + " " + pkt.addr2)
                mac = ":".join(pkt.addr2.split(":")[:3]).upper()
                vendor = "\n".join(line for line in manuf.splitlines() if line.startswith(mac)).split("# ")[1]
                print "%s (%s %s)" % (pkt.info, pkt.addr2, vendor)
                #print pkt.show()

sniff(iface="mon0", count=0, prn=Handler, store=0) # sudo rfkill unblock wifi && sudo airmon-ng start wlan0
