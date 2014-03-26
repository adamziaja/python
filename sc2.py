#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# SC2 API
# (C) 2014 Adam Ziaja <adam@adamziaja.com> http://adamziaja.com

import requests # debian: python3-requests
import datetime

r = requests.get('http://eu.battle.net/api/sc2/profile/2446271/1/Adam/matches?locale=pl_PL')

#print(r.json())
for match in r.json()['matches']:
	date = datetime.datetime.fromtimestamp(int(match['date'])).strftime('%Y-%m-%d %H:%M:%S')
	decision = match['decision']
	type = match['type']
	print(date, decision, type)
