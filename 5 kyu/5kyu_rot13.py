
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


