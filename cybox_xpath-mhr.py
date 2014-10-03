#!/usr/bin/env python
# -*- coding: utf-8 -*-

# (C) 2014 Adam Ziaja <adam@adamziaja.com> http://adamziaja.com

from lxml import etree # http://lxml.de/xpathxslt.html#the-xpath-method
import hashlib
# http://www.team-cymru.org/Services/MHR/
from cymru.mhr.dns import DNSClient as mhr # pip install cymru-services

namespaces = {
	'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
	'stix': 'http://stix.mitre.org/stix-1',
	'stixVocabs': 'http://stix.mitre.org/default_vocabularies-1',
	'stixCommon': 'http://stix.mitre.org/common-1',
	'cybox': 'http://cybox.mitre.org/cybox-2',
	'cyboxCommon': 'http://cybox.mitre.org/common-2',
	'cyboxVocabs': 'http://cybox.mitre.org/default_vocabularies-2',
	'indicator': 'http://stix.mitre.org/Indicator-2',
	'ttp': 'http://stix.mitre.org/TTP-1',
	'marking': 'http://data-marking.mitre.org/Marking-1',
	'simpleMarking': 'http://data-marking.mitre.org/extensions/MarkingStructure#Simple-1',
	'openiocTM': 'http://stix.mitre.org/extensions/TestMechanism#OpenIOC2010-1',
	'mandiant': 'http://www.mandiant.com',
	'FileObj': 'http://cybox.mitre.org/objects#FileObject-2',
	'WinServiceObj': 'http://cybox.mitre.org/objects#WinServiceObject-2',
	'WinProcessObj': 'http://cybox.mitre.org/objects#WinProcessObject-2',
	'WinExecutableFileObj': 'http://cybox.mitre.org/objects#WinExecutableFileObject-2',
	'WinRegistryKeyObj': 'http://cybox.mitre.org/objects#WinRegistryKeyObject-2',
	'WinHandleObj': 'http://cybox.mitre.org/objects#WinHandleObject-2',
	'ProcessObj': 'http://cybox.mitre.org/objects#ProcessObject-2',
	'WinDriverObj': 'http://cybox.mitre.org/objects#WinDriverObject-2'
}

client=mhr()
f = 'APT1-STIX/Appendix_G_IOCs_Full.xml' # http://stix.mitre.org/downloads/APT1-STIX.zip
doc = etree.parse(f)
for r in doc.xpath('/stix:STIX_Package/stix:Observables/cybox:Observable/cybox:Object/cybox:Properties/FileObj:Hashes/cyboxCommon:Hash/cyboxCommon:Simple_Hash_Value', namespaces=namespaces):
	print r.text
	print client.lookup(r.text)
