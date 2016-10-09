#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Apache2 combined log parser
# (C) 2016 Adam Ziaja <adam@adamziaja.com> http://adamziaja.com

import re

# LogFormat "%h %l %u %t \"%r\" %>s %O \"%{Referer}i\" \"%{User-Agent}i\"" combined
regex = '([(\d\.)]+) (\w|-) (\w|-) \[(.*?)\] "(.*?)" (\d+) (\d+|-) "(.*?)" "(.*?)"'

with open('/var/log/apache2/access.log') as f:
	for line in f:
		print line,
		print re.match(regex, line).groups()
		hostname = re.match(regex, line).groups()[0] # %h	Remote hostname.
		# re.match(regex, line).groups()[1] # %l	Remote logname (from identd, if supplied).
		# re.match(regex, line).groups()[2] # %u	Remote user if the request was authenticated.
		time = re.match(regex, line).groups()[3] # %t	Time the request was received.
		request = re.match(regex, line).groups()[4] # %r	First line of request.
		status = re.match(regex, line).groups()[5] # %s	Status.
		# re.match(regex, line).groups()[6] # %O	Bytes sent, including headers.
		referer = re.match(regex, line).groups()[7] # %{Referer}i
		useragent = re.match(regex, line).groups()[8] # %{User-Agent}i
		print hostname, time, request, status, referer, useragent
		print
