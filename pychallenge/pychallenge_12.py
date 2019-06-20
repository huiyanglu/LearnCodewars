#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Huiyang Lu
with open('evil2.gfx','rb') as f:
    data = f.read()
for i in range(5):
    with open('evil_%d.jpg'%i,'wb') as rst:
        rst.write(data[i::5]) #从i开始 间隔为5