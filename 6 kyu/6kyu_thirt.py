def thirt(n):
    x = []
    for i in range(0,len(str(n))+1):
        a = (10**i)%13
        x.append(a)
        i+=1
    l1 = [int(i) for i in str(n)]
    l1.reverse()
    prod = [a * b for a, b in zip(l1, x)]
    s1 = sum(prod)
    for j in range(0,100):
        l2 = [int(i) for i in str(s1)]
        l2.reverse() #数列反序
        prod2 = [a * b for a, b in zip(l2, x)] #数组相乘
        s2 = sum(prod2)
        if s1 != s2:
            j+=1
            s1 = s2
            s2 = 0
        else:
            return s1

