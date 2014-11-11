#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Passive scan for WiFi networks

# (C) 2014 Adam Ziaja <adam@adamziaja.com> http://adamziaja.com

from scapy.all import *

unique_ssid = []

def Handler(pkt):
    if pkt.haslayer(Dot11): # 802.11
        #if pkt.type == 0 and pkt.subtype == 8: # https://en.wikipedia.org/wiki/Beacon_frame
        try:
            if pkt.info not in unique_ssid and len(pkt.info) > 0:
                unique_ssid.append(pkt.info)
                print unique_ssid
                print pkt.info
                #print pkt.show()
                pkt.pdfdump(filename=pkt.info + "_" + pkt.addr2 + ".pdf") # sudo apt-get update && sudo apt-get install -y python-pyx
        except AttributeError:
            pass

sniff(iface="mon0", count=0, prn=Handler, store=0) # sudo rfkill unblock wifi && sudo airmon-ng start wlan0
