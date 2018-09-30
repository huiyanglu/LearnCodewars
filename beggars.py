def beggars(a,n):
    res = [ 0 for i in range(n)]
    for j in range(0,len(a)):
        if n != 0:
            res[j%n] += a[j]
        else:
            return []
    return res
