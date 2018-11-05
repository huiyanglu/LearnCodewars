import re

def printer_error(s):
    # your code
    m = str(len(re.findall(r'[n-z]',s)))
    q = str(len(s))#总长度 要加str!
    return m+'/'+q

s="aammmxyzz"
x = printer_error(s)
print(x)