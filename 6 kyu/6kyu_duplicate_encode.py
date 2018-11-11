"""
Duplicate Encoder

https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

The goal of this exercise is to convert a string to a new string where each character in the new string is '(' if that character appears only once in the original string, or ')' if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples:

"din" => "((("

"recede" => "()()()"

"Success" => ")())())"

"(( @" => "))(("


Notes:

Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" is actually the expected result, not the input! (these languages are locked so that's not possible to correct it).

"""

from collections import Counter
import re

def duplicate_encode(n):
    nn = n.lower()
    dct = dict(Counter(nn))
    del_1 = dict((key,value)for key,value in dct.items()if value!=1)
    b = [i for i in del_1.keys()]
    nn.split(',')
    a = []
    for i in range(0, len(nn)):
        if nn[i] in b:
            num = re.sub(r'\D', ")", nn[i])
        else:
            num = re.sub(r'[0-9a-zA-Z\s\_\@\(\)\*\:\!\'\"]', "(", nn[i])
        a.append(num)
        i += 1
    return ''.join(a)
