#!/usr/bin/env python
# -*- coding: utf-8 -*-

# (C) 2016 Adam Ziaja <adam@adamziaja.com> http://adamziaja.com

# http://docs.bleachbit.org/doc/cleanerml.html
# https://github.com/az0/cleanerml/
# https://github.com/az0/bleachbit/blob/master/doc/cleaner_markup_language.xsd
# https://github.com/az0/bleachbit/tree/master/cleaners
# https://github.com/az0/bleachbit/blob/master/bleachbit/Cleaner.py

import os
from lxml import etree # http://lxml.de/xpathxslt.html#the-xpath-method
import xml.etree.ElementTree

for file in os.listdir('.'): # https://github.com/az0/bleachbit/tree/master/cleaners
    if file.endswith('.xml'):
        e = xml.etree.ElementTree.parse(file).getroot()
        #print e.attrib['id']
        print e.find('label').text + ' -',
        try:
            print e.find('description').text
        except:
            pass

        for option in e.findall('option'):
            print option.find('description').text

            for action in option.iter('action'):
                print action.attrib
                #if 'path' in action.attrib:
                #    print action.attrib['path']
                #else:
                #    for action in option.iter('action'):
                #        print action.attrib
    print
# https://gist.github.com/adamziaja/34e6dea311c166bcd506
