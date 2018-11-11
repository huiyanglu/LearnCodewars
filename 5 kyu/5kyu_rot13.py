"""
Rot13

https://www.codewars.com/kata/530e15517bc88ac656000716

ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using "encode" in Python is considered cheating.

"""
# -*- coding:utf-8 -*-

import string

def rot13(s):
    uppd = {}
    lowd = {}
    upletters = string.ascii_uppercase  # 大写
    lowletters = string.ascii_lowercase  # 小写
    for i in range(0, len(lowletters)):
        if i < 13:
            lowd[lowletters[i]] = lowletters[i + 13]
        else:
            lowd[lowletters[i]] = lowletters[i - 13]

    for i in range(0, len(upletters)):
        if i < 13:
            lowd[upletters[i]] = upletters[i + 13]
        else:
            lowd[upletters[i]] = upletters[i - 13]
    lst = []
    for m in s:
        if m in lowd:
            lst.append(lowd[m])
        elif m in uppd:
            lst.append(uppd[m])
        else:
            lst.append(m)
    return ''.join(lst)
print(rot13('about'))


