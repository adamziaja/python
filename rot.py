#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ROT-n decryptor (Caesar cipher)
# usage: python rot.py "ZCZL YHZIZ ZCZLYHZIZ.BNL"

# (C) 2014 Adam Ziaja <adam@adamziaja.com> http://adamziaja.com

import sys
import string
import itertools

def rot(char):
    if char is "-":
        alphabet = list(string.uppercase)
    else:
        alphabet = list(reversed(string.uppercase))
    for shift in range(1, 14):
        print "Alphabet shift " + char + str(shift) + "\t",
        clear = ""
        for c in cipher.upper():
            if c in alphabet:
                rot = itertools.cycle(alphabet)
                n = alphabet.index(c) + 1 + shift
                for i in range(n):
                    ch = rot.next()
                clear += ch
            else:
                clear += c
        print clear

cipher = ' '.join(sys.argv[1:])

if cipher:
    rot('-')
    rot('+')
