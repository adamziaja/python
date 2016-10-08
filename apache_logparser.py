#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Apache2 combined log parser
# (C) 2016 Adam Ziaja <adam@adamziaja.com> http://adamziaja.com

import re
regex = '([(\d\.)]+) (\w+|-) (\w+|-) \[(.*?)\] "(.*?)" (\d+) (\d+|-) "(.*?)" "(.*?)"' # LogFormat "%h %l %u %t \"%r\" %>s %O \"%{Referer}i\" \"%{User-Agent}i\"" combined

with open('/var/log/access.log') as f:
	for line in f:
		print re.match(regex, line).groups()
		print re.match(regex, line).groups()[0] # %h	Remote hostname.
		print re.match(regex, line).groups()[1] # %l	Remote logname (from identd, if supplied).
		print re.match(regex, line).groups()[2] # %u	Remote user if the request was authenticated.
		print re.match(regex, line).groups()[3] # %t	Time the request was received.
		print re.match(regex, line).groups()[4] # %r	First line of request.
		print re.match(regex, line).groups()[5] # %s	Status.
		print re.match(regex, line).groups()[6] # %O	Bytes sent, including headers.
		print re.match(regex, line).groups()[7] # %{Referer}i
		print re.match(regex, line).groups()[8] # %{User-agent}i
