"""
Rot13

https://www.codewars.com/kata/530e15517bc88ac656000716

ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using "encode" in Python is considered cheating.

"""
# -*- coding:utf-8 -*-
import re
import string

regex = re.compile('[a-z]{1}', re.IGNORECASE)

def replace(match):
    upletters = string.ascii_uppercase  # 大写
    lowletters = string.ascii_lowercase  # 小写

    word = match.group(0)
    if word in lowletters:
        return lowletters[lowletters.index(word[0])+13 if lowletters.index(word[0])<13 else lowletters.index(word[0])-13]
    else:
        return upletters[
            upletters.index(word[0]) + 13 if upletters.index(word[0]) < 13 else upletters.index(word[0]) - 13]

def rot13(s):
    return regex.sub(replace, s)

print(rot13('aboutYOU'))
