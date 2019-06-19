#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Huiyang Lu
from PIL import Image
#Image模块是在Python PIL图像处理中常见的模块
im = Image.open(r'cave.jpg')
x,y = im.size #图片大小

im1 = Image.new(im.mode,(x//2,y//2))
im2 = Image.new(im.mode,(x//2,y//2))

for i in range(x):
    for j in range(y):
        pixel = im.getpixel((i,j))#获得像素点
        if i%2==0 and j%2==0:
            im1.putpixel((i//2,j//2),pixel)
        if i%2==0 and j%2!=0:
            im2.putpixel((i//2,j//2),pixel)
        if i%2!=0 and j%2==0:
            im2.putpixel((i//2,j//2),pixel)
        if i%2!=0 and j%2!=0:
            im1.putpixel((i//2,j//2),pixel)
im1.point(lambda i:i*10)
im1.show()
im2.show()