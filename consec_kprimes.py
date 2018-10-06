def factoring(n):
    primefac = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            primefac.append(d)
            n //= d
        d += 1
    if n > 1:
        primefac.append(n)
    return len(primefac)


def consec_kprimes(k, arr):
    x = []
    for i in range(0, len(arr)-1):
        b = factoring(arr[i])
        b2 = factoring(arr[i+1])
        if b == k and b2 == k :
            x.append(b)
            i += 1
        else:
            i += 1
    return len(x)
