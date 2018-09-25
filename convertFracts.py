from functools import reduce

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def convertFracts(lst):
    denoms = [i[1] for i in lst] # denominator分母
    nums = [i[0] for i in lst] # numerator分子
    lsttt = denoms + nums # [4, 6, 8, 2, 2, 2]
    _gcd = reduce(gcd,lsttt) # 2
    denoms2 = [i[1]//_gcd for i in lst] # 化简后的分母
    nums2 = [i[0]//_gcd for i in lst] # 化简后的分子
    _lcm = reduce(lcm,denoms2) # lcm是函数
    multi = [_lcm//i for i in denoms2]
    return [[i*m,_lcm] for i,m in zip(nums2,multi)]

a = [[2,4], [2, 6], [2, 8]] 
print(convertFracts(a))
