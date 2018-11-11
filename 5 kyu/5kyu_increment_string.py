"""
String incrementer

https://www.codewars.com/kata/54a91a4883a7de5d7800009c

Your job is to write a function which increments a string, to create a new string. If the string already ends with a number, the number should be incremented by 1. If the string does not end with a number the number 1 should be appended to the new string.

Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.


"""

import re

def increment_string(s):
    number = re.findall(r'\d+', s) #找到所有数字
    if number:
        lst = number[-1]
        s = s.rsplit(lst, 1)[0] # 从右向左找最后一个数，取除最后一个数以外的前面部分
        number = str(int(lst) + 1) # 先把最后一个数转为数字，加1，再转为字符串（过程中lst的位数会变化）
        return s + '0' * (len(lst) - len(number)) + number #转换中少掉的0要补上
    else:
        return s + '1'
