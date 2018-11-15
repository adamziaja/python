#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Adam Michal Ziaja http://adamziaja.com
# 2012-01-21

# Remote Wake-up (RWU)

import sys
import socket

mac = "".join(chr(int(x, 16)) for x in sys.argv[1].split(':'))
ip = sys.argv[2]

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto('\xff'*6+mac*16, (ip, 9))
