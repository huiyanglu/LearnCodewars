
import itertools

def slogan_maker(a):
    a2 = list(set(a))
    a2.sort(key=a.index) # 字符串去重后按原顺序排列
    x = []
    result = list(itertools.permutations(a2, len(a2))) # 字符串排列组合考虑顺序
    for i in range(0,len(result)):
        x.append(join1(result[i]))
        i+=1
    return x

def join1(x): # 字符串合并join
    x1 = list(x)
    return ' '.join(x1)
