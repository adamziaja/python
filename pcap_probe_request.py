#!/usr/bin/env python
# -*- coding: utf-8 -*-

# PCAP parser to save WiFi probe requests to MySQL database

# (C) 2014 Adam Ziaja <adam@adamziaja.com> http://adamziaja.com

import sys
from scapy.all import *
import oursql # sudo apt-get update && sudo apt-get install python-pip libmysqlclient-dev && sudo pip install oursql

conn = oursql.connect(host='localhost', user='*USER*', passwd='*PASSWORD*', db='*DATABASE*', port=3307)
curs = conn.cursor(oursql.DictCursor)
curs.execute('CREATE TABLE IF NOT EXISTS wifi (ID int NOT NULL AUTO_INCREMENT UNIQUE, ssid varchar(255) NOT NULL, mac varchar(17) NOT NULL, PRIMARY KEY (ID), UNIQUE KEY `probe` (`ssid`, `mac`))')

def Handler(pkt):
    if pkt.haslayer(Dot11ProbeReq):
        print pkt.summary()
        if len(pkt.info) > 0:
            print pkt.info, pkt.addr2
            try:
                curs.execute('INSERT IGNORE INTO `wifi` (ssid, mac) VALUES (?, ?)',(pkt.info, pkt.addr2))
            except UnicodeDecodeError:
                pass

sniff(offline=sys.argv[1], prn=Handler) # .pcap
