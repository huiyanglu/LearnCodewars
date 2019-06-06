#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Huiyang Lu
import itertools

def ans(n: int) -> str:
    s = '11'
    for _ in range(n-1):
        s = ''.join(str(len(list(group)))+digit for digit,group in itertools.groupby(s))
    return len(s)

print(ans(30))

# next level:http://www.pythonchallenge.com/pc/return/5808.html