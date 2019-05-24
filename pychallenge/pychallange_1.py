#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Huiyang Lu
def ans(a):
    rst = []
    for i in range(len(a)):
        if a[i].isalpha():
            asc_num = ord(a[i])+2
            if asc_num < 123:
                rst.append(chr(asc_num))
            else:
                asc_num -= 26
                rst.append(chr(asc_num))
        else:
            rst.append(a[i])
    return ''.join(rst)

a = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
b = 'map'
print(ans(b))