#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Huiyang Lu
import os
import re
import zipfile

def ans(num):
    meragefiledir = os.getcwd()
    filenames = os.listdir(meragefiledir+'/channel')
    infile = meragefiledir+'/channel.zip'
    fzip = zipfile.ZipFile(infile)
    for i in range(0,len(filenames)):
        text1 = open(meragefiledir+'/channel/'+ str(num) +'.txt', 'r')
        text2 = text1.read()
        find_next_num = re.findall('\d+', text2)
        if find_next_num:
            next_num = int(find_next_num[0])
            num = next_num
            now_file = str(next_num)+'.txt'
            print(fzip.getinfo(now_file).comment.decode("utf-8"), end="")
        else:
            break
    return find_next_num

print(ans(90052))

# answer: hockey
# http://www.pythonchallenge.com/pc/def/hockey.html
# it's in the air. look at the letters.
# http://www.pythonchallenge.com/pc/def/oxygen.html