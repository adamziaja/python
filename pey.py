#!/usr/bin/env python
# -*- coding: utf-8 -*-

# (C) 2014 Adam Ziaja <adam@adamziaja.com> http://adamziaja.com

__author__ = 'Adam Ziaja'
__email__ = 'adam@adamziaja.com'

import sys
import argparse

parser = argparse.ArgumentParser(
    description='check for PEiD and/or Yara signatures')

parser.add_argument(dest='filenames', metavar='filename', nargs='*')

parser.add_argument('-v', dest='verbose', action='store_true', help='verbose')

parser.add_argument('-vv', dest='veryverbose',
                    action='store_true', help='very verbose')

parser.add_argument(
    '-p', dest='peid', action='store', help='peid signatures file')

parser.add_argument(
    '-y', dest='yara', action='store', help='yara signatures file')

args = parser.parse_args()

if not args.peid and not args.yara:
    sys.exit('you need define at least one signatures file')

if args.peid:
    try:
        import pefile
        import peutils
    except ImportError:
        sys.exit('pefile module not installed')  # pip install pefile

if args.yara:
    try:
        import yara
    except ImportError:
        sys.exit('yara module not installed')  # pip install yara

if args.peid:
    try:
        # sigs = peutils.SignatureDatabase('http://research.pandasecurity.com/blogs/images/userdb.txt')
        # sigs = peutils.SignatureDatabase('userdb.txt')
        sigs = peutils.SignatureDatabase(args.peid)  # PEiD signatures
    except IOError:
        sys.exit('peid signatures file does not exist')

if args.yara:
    try:
        rules = yara.compile(args.yara)  # Yara signatures
    except IOError:
        sys.exit('yara signatures file does not exist')

if not args.filenames:
    sys.exit('you must select at least one file')

for file in args.filenames:
    print(file)

    if args.peid:
        try:
            if args.veryverbose:
                pe = pefile.PE(file, fast_load=False)
            else:
                pe = pefile.PE(file, fast_load=True)
        except IOError:
            sys.exit('no such file ' + file)

        pe_matches = sigs.match(pe, ep_only=True)
        if pe_matches is not None:
            for pe_match in pe_matches:
                print('PEiD: ' + pe_match)

    if args.yara:
        yara_matches = rules.match(file)
        try:
            for yara_match in yara_matches['main']:
                try:
                    print('Yara: ' + yara_match['meta']['description'])
                except KeyError:
                    pass
        except KeyError:
            pass

    print

    if args.peid:
        if args.verbose or args.veryverbose:
            print(pe.dump_info())
