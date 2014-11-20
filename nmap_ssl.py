#!/usr/bin/env python
# -*- coding: utf-8 -*-

# SSL port list from Nmap XML

# (C) 2014 Adam Ziaja <adam@adamziaja.com> http://adamziaja.com

import sys
from lxml import etree

f = sys.argv[1] # nmap xml
doc = etree.parse(f)
for addr in doc.xpath('//nmaprun/host/address/@addr'): # xacobeo
	for port in doc.xpath('//nmaprun/host[address[@addr="' + addr + '"]]/ports/port[script[@id="ssl-cert"]]/@portid'):
		print addr + ":" + port
