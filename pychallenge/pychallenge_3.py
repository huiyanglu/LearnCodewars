#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Huiyang Lu
import re

def ans():
    text1 = open('hint2.txt','r')
    text2 = text1.read()
    reg = re.findall(r'[a-z]{1}[A-Z]{3}([a-z]{1})[A-Z]{3}[a-z]{1}',text2)
    return ''.join(reg)

print(ans())