#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

def validnumber(num):
    if num.isdigit() and len(num) == 10:
        return num
    elif num[0] == '+' and num[1:].isdigit() and 9 <= len(num) < 14:
        if len(num) == 9:
            num = '0' + num
        return re.compile('(\+380|380)').sub('0', num)
    else:
        print('Invalid phone number format')
