#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Huiyang Lu

import pickle

def ans():
    with open('banner.p', 'rb') as fp:
        rst = pickle.load(fp)
    for item in rst:
        print(''.join(each[0]*each[1] for each in item))

print(ans())

# answer: channel