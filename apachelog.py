#!/usr/bin/env python
# -*- coding: utf-8 -*-

# check ASN from apache log
# python apachelog.py | grep AS5617 -B1

# (C) 2014 Adam Ziaja <adam@adamziaja.com> http://adamziaja.com

import pygeoip  # sudo pip install pygeoip
from IPy import IP  # sudo pip install ipy

gi = pygeoip.GeoIP('/usr/share/GeoIP/GeoIPASNum.dat') # debian/ubuntu

class bcolors:
    purple = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    end = '\033[0m'

with open('/var/log/apache2/access.log') as f: # debian/ubuntu
    for line in f:
        print bcolors.green + line + bcolors.end,
        if IP(line.split(' ')[0]).version() is 4 and gi.org_by_name(line.split(' ')[0]) is not None:
            # if 'ASXXXXX' in gi.org_by_name(line.split(' ')[0]):
            print bcolors.yellow + gi.org_by_name(line.split(' ')[0]) + bcolors.end
        else:
            print bcolors.red + line.split(' ')[0] + ' is not in the GeoIP database' + bcolors.end
