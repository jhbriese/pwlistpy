#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Title:        pwListPy
# Author:       Jan-Hendrik Briese
# License:      ToDo
# Description:  Easy create Password Lists with custom strength
import os, sys, getopt, random
version = '0.1alpha'
banner = '''
██████╗ ██╗    ██╗██╗     ██╗███████╗████████╗██████╗ ██╗   ██╗
██╔══██╗██║    ██║██║     ██║██╔════╝╚══██╔══╝██╔══██╗╚██╗ ██╔╝
██████╔╝██║ █╗ ██║██║     ██║███████╗   ██║   ██████╔╝ ╚████╔╝
██╔═══╝ ██║███╗██║██║     ██║╚════██║   ██║   ██╔═══╝   ╚██╔╝
██║     ╚███╔███╔╝███████╗██║███████║   ██║   ██║        ██║
╚═╝      ╚══╝╚══╝ ╚══════╝╚═╝╚══════╝   ╚═╝   ╚═╝        ╚═╝

pwListpy Version: %s
''' % version

script = os.path.basename(sys.argv[0])
usage = '''Usage:
%s [options]

Options:
 -h, --help
 --count=NUMBER (Password count)
 --length=NUMBER (Length of Passwords)
 --output=FILE (Name of the File to Save Passwords)
 -L, --lowercase (Use Lowercase Characters a-z)
 -U, --uppercsae (Use Uppercase Characters A-Z)
 -N, --numbers (Use Numbers 0-9)
 -S, --symbols (Use Symbols e.g. #,.-/)
''' % script

try:
    opts, args = getopt.getopt(sys.argv[1:],'b:hLUNS:',
                               ['help', 'count=', 'length=', 'output=',
                                'lowercase', 'uppercsae','numbers', 'symbols'])
except getopt.GetoptError:
    print('Error parsing options:')
    print(usage)
    sys.exit(2)

styleargs = False
banner_printed = False

for opt, arg in opts:
    if opt in ('-h', '--help'):
        if not banner_printed:
            print(banner)
            banner_printed = True
        print(usage)
        sys.exit()
    elif opt in ('--count'):
        count = arg
        if not count.isdigit():
            if not banner_printed:
                print(banner)
                banner_printed = True
            print('Woring count!\n\n' + usage)
            sys.exit()
        count = int(count)
    elif opt in ('--length'):
        length = arg
        if not length.isdigit():
            if not banner_printed:
                print(banner)
                banner_printed = True
            print('Woring length!\n\n' + usage)
            sys.exit()
        length = int(length)
    elif opt in ('--output'):
        output = arg
    elif opt in ('-L', '--lowercase'):
        lowercase = True
        styleargs = True
    elif opt in ('-U', '--uppercase'):
        uppercase = True
        styleargs = True
    elif opt in ('-N', '--numbers'):
        numbers = True
        styleargs = True
    elif opt in ('-S', '--symbols'):
        symbols = True
        styleargs = True

if not 'count' in locals():
    if not banner_printed:
        print(banner)
        banner_printed = True
    count = input('Enter Password count: ')
    if not count.isdigit():
        print('Error! only positive numbers supportet')
        sys.exit()
    count = int(count)

if not 'length' in locals():
    if not banner_printed:
        print(banner)
        banner_printed = True
    length = input('Enter Password length: ')
    if not length.isdigit():
        print('Error! only positive numbers supportet')
        sys.exit()
    length = int(length)

if 'output' in locals():
    to_file = True
    outputfile = open(output, 'w')
else:
    to_file = False

chars=[]
while not len(chars) > 0:
    while not 'lowercase' in locals():
        if not styleargs:
            if not banner_printed:
                print(banner)
                banner_printed = True
            tmp_input = input('Use Lowercaes (Y/N): ')
            if tmp_input == 'Y' or tmp_input == 'y':
                lowercase = True
            elif tmp_input == 'N' or tmp_input == 'n':
                lowercase = False
        else:
            lowercase = False

    while not 'uppercase' in locals():
        if not styleargs:
            if not banner_printed:
                print(banner)
                banner_printed = True
            tmp_input = input('Use Uppercaes (Y/N): ')
            if tmp_input == 'Y' or tmp_input == 'y':
                uppercase = True
            elif tmp_input == 'N' or 'n':
                uppercase = False
        else:
            uppercase = False

    while not 'numbers' in locals():
        if not styleargs:
            if not banner_printed:
                print(banner)
                banner_printed = True
            tmp_input = input('Use Numbers (Y/N): ')
            if tmp_input == 'Y' or tmp_input == 'y':
                numbers = True
            elif tmp_input == 'N' or tmp_input == 'n':
                numbers = False
        else:
            numbers = False

    while not 'symbols' in locals():
        if not styleargs:
            if not banner_printed:
                print(banner)
                banner_printed = True
            tmp_input = input('Use Symbols (Y/N): ')
            if tmp_input == 'Y' or tmp_input == 'y':
                symbols = True
            elif tmp_input == 'N' or tmp_input == 'n':
                symbols = False
        else:
            symbols = False

    if lowercase:
        for i in range(97, 123):
            chars.append(chr(i))

    if uppercase:
        for i in range(65, 91):
            chars.append(chr(i))

    if numbers:
        for i in range(48, 58):
            chars.append(chr(i))

    if symbols:
        for i in range(33, 48):
            chars.append(chr(i))
        for i in range(58, 65):
            chars.append(chr(i))
        for i in range(91, 96):
            chars.append(chr(i))

    del lowercase, uppercase, numbers, symbols

password = ''


for c in range(0,count):
    for l in range(0, length):
        rnd = random.randint(0, len(chars)-1)
        password = password + chars[rnd]
    password = password + '\n'
if to_file:
    outputfile.write(password)
else:
    print(password)
