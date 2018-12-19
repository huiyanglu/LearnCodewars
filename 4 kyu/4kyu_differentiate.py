import re
import numpy as np

def differentiate(equation,point):
    res = re.split(r'(\+|-)',equation)
    res1 = res[1:]
    res1 = [res[0]]+["".join(i).strip() for i in zip(res1[0::2],res1[1::2])]
    if res1[0] == '':
        res1.pop(0)
    no_x = [i for i in res1 if 'x' not in i]
    if '^' in res1[0]:
        zhishuMax = res1[0][res1[0].index('^')+1:]
        l = int(zhishuMax)+1
    else:
        l = len(res1)
    #if no_x == []:
        #l = len(res1)+1
    #else:
        #l=len(res1)
    lst = [0]*l
    for i in range(0,l-1):
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
    a = np.array(lst)
    p = np.poly1d(a)
    deri = p.deriv()
    return deri(point)

txt = '21x^4+3x^3'
print(differentiate(txt,414))