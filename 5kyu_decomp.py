def decomp(num):
    ans = []
    for i in range(2, num + 1):
        ans += primeFactor(i)
    sorted_myset = sorted(set(ans))
    ones = []
    single_ones = []
    for item in sorted_myset:
        if ans.count(item)>1:
            each_one = str("%d^%d" %(item, ans.count(item)))
            ones.append(each_one)
        else:
            single_ones.append(str(item))
        ones2 = ones + single_ones
    return ' * '.join(ones2)

def primeFactor(n):
    decomp = []
    i = 2
    while n > 1:
        while n % i == 0: #如果能被i整除
            n /= i
            decomp.append(i) #在list里加入i的值
        i += 1 #如果不能被整除，则i+1
    return decomp
