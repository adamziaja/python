#!/usr/bin/python
# -*- coding: utf-8 -*-

# Mozilla places.sqlite to HTML

# (C) 2014 Adam Ziaja <adam@adamziaja.com> http://adamziaja.com

import sqlite3
conn = sqlite3.connect('places.sqlite')
c = conn.cursor()

print '''<!DOCTYPE html>
<html>
<head>
<style type="text/css">
* {
font-family: Verdana, Geneva, sans-serif;
font-size: 12px;
}
</style>
</head>
<body>
<table cellpadding="5" cellspacing="0" border="1">
<tr><th>title</th><th>url</th><th>last_visit_date</th><tr>'''
for row in \
    c.execute('SELECT title, url, datetime("1379767479983000"/1000000,"unixepoch","localtime") FROM moz_places ORDER BY id DESC'
              ):
    title = row[0]
    url = row[1]
    datetime = row[2]
    if title is None:
        title = ''
    print ('<tr><td>' + title + '</td><td><a href="' + url
           + '" target="_blank" rel="noreferrer">' + url
           + '</a></td><td>' + datetime + '</td></tr>').encode('utf-8'
            ).strip()
print '''</table>
</body>
</html>'''
