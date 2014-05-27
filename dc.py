#!/usr/bin/env python
# -*- coding: utf-8 -*-

# recursive check of DNS zone export (AXFR)
# Python version of 'dc.php' from https://code.google.com/p/dns-check/

# (C) 2014 Adam Ziaja <adam@adamziaja.com> http://adamziaja.com

import sys
import dns.resolver
import dns.message
import dns.name
import dns.query
import dns.rdatatype

def axfr(domain):
    if domain[-1:] is not '.':
        domain = domain + '.'
    print domain
    lastsubdomain = ''

    try:
        answers = dns.resolver.query(domain, 'NS')
    except:
        try:
            queue.remove(domain)
        except ValueError:
            pass
        print queue
        if not queue:
            sys.exit(0)
        axfr(queue[:1][0])

    for rdata in answers:
        msg = dns.message.make_query(
            dns.name.from_text(domain), dns.rdatatype.AXFR)

        try:
            response = dns.query.tcp(msg, rdata.to_text())
        except:
            try:
                queue.remove(domain)
            except ValueError:
                pass
            print queue
            if not queue:
                sys.exit(0)
            axfr(queue[:1][0])

        filename = domain[:-1] + '_' + rdata.to_text() + 'txt'
        print filename
        file = open(filename, 'w')
        file.write(response.to_text())
        file.close()

        for records in response.answer:
            if records.rdtype is 2:
                for record in records.to_text().splitlines():
                    if not domain == record.split(' ')[0]:
                        subdomain = record.split(' ')[0]
                        if subdomain != lastsubdomain:
                            queue.append(subdomain)
                        lastsubdomain = subdomain

    try:
        queue.remove(domain)
    except ValueError:
        pass
    print queue
    if not queue:
        sys.exit(0)
    axfr(queue[:1][0])

if __name__ == "__main__":
    queue = []
    axfr(sys.argv[1])
