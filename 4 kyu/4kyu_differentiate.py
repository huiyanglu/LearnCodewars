"""
Differentiate a polynomial

https://www.codewars.com/kata/566584e3309db1b17d000027/solutions/python

Description:
Create a function that differentiates a polynomial for a given value of x.

Your function will receive 2 arguments: a polynomial as a string, and a point to evaluate the equation as an integer.

Assumptions:
There will be a coefficient near each x, unless the coefficient equals 1 or -1.
There will be an exponent near each x, unless the exponent equals 0 or 1.
All exponents will be greater or equal to zero
Examples:
differenatiate("12x+2", 3)      ==>   returns 12
differenatiate("x^2+3x+2", 3)   ==>   returns 9
"""

import re

def differentiate(equation,point):
    res = re.split(r'(\+|-)',equation)
    res1 = res[1:]
    res1 = [res[0]]+["".join(i).strip() for i in zip(res1[0::2],res1[1::2])]
    #if res1[0] == '':
        #res1.pop(0)
    if '^' in res1[0]:
        zhishuMax = res1[0][res1[0].index('^')+1:]
        l = int(zhishuMax)+1
    else:
        l = len(res1)
    lst = [0]*l
    len_lst = len(res1)
    for i in range(0,len_lst):
        if 'x' not in res1[i]:
            lst[-1] = int(res1[i])
        else:
            idx_x = res1[i].index('x')
            if '^' in res1[i]:
                idx_2 = res1[i].index('^')
                zhishu = res1[i][idx_2+1:]
            else:
                zhishu = 1
            if idx_x == 0 or (idx_x == 1 and res1[i][0] == '+'):
                lst[l - int(zhishu) - 1] = 1
            elif idx_x == 1 and res1[i][0] == '-':
                lst[l - int(zhishu) - 1] = -1
            else:
                lst[l - int(zhishu) - 1] = int(res1[i][:idx_x])
    sum = 0
    for i in range(0,len(lst)):
        if lst[i]==0:
            pass
        elif l-i-2>=0 and lst[i]!=0:
            sum+=lst[i]*(l-i-1)*(point**(l-i-2))
        else:
            break
    return sum

print(differentiate('48x^6+36x^5-18x^4+x^3+76x^2+36x+1',4968))


