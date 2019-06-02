#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Huiyang Lu

from urllib.request import urlretrieve
from PIL import Image
import re

def ans(img):
    data = [chr(i[0]) for i in [img.getpixel((j,img.size[1]/2)) for j in range(0,img.size[0],7)]]
    s1 = str(''.join(data)) #找到线索
    rst = re.findall(r"[[](.*?)[]]",s1) #用正则找到[]里的内容
    lst = rst[0].split(',') #生成坐标形式用chr转换成字母
    return ''.join(chr(int(i)) for i in lst)


urlretrieve("http://www.pythonchallenge.com/pc/def/oxygen.png","oxygen.png")
img = Image.open("oxygen.png")
print(ans(img))

"""
this level: http://www.pythonchallenge.com/pc/def/oxygen.html
smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]pe_
['105', ' 110', ' 116', ' 101', ' 103', ' 114', ' 105', ' 116', ' 121']
integrity
next level: http://www.pythonchallenge.com/pc/def/integrity.html
"""