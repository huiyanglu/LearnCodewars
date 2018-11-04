# my wrong answer because of timed out

def decomp(num):
    mylist = []
    for i in range(0, num + 1):
        each_factor = primeFactor(i)
        mylist += each_factor
    sorted_myset = sorted(set(mylist))
    ones = []
    single_ones = []
    for item in sorted_myset:
        if mylist.count(item)>1:
            each_one = str("%d^%d" %(item, mylist.count(item)))
            ones.append(each_one)
        else:
            single_ones.append(str(item))
        ones2 = ones + single_ones
    return ' * '.join(ones2)

def primeFactor(num):
    list1 = []
    for i in range(2, num):
        while True:
            if num % i == 0:
                list1.append(i)
                num = num / i
            else:
                break
    if list1 == [] and num>=2:
        return [num]
    return list1

print(decomp(30))

# Given solutions
from collections import defaultdict


def dec(n):
    decomp = defaultdict(lambda: 0)
    i = 2
    while n > 1:
        while n % i == 0:
            n /= i
            decomp[i] += 1
        i += 1
    return decomp


def decomp(n):
    ans = defaultdict(lambda: 0)
    for i in range(2, n + 1):
        for key, value in dec(i).items():
            ans[key] += value
    return ' * '.join('{}^{}'.format(x, y) if y > 1 else str(x) for x, y in sorted(ans.items()))

---
from itertools import count

dec = [[], [], [1]]
primes = [2]


def genPrimes():
    for x in count(3, 2):
        sq = int(x ** .5)
        if all(p > sq or x % p for p in primes):
            yield x


primGen = genPrimes()


def genPrimesUpTo(n):
    while primes[-1] < n:
        primes.append(next(primGen))


def genPrimeDivs(n):
    genPrimesUpTo(n)
    dec.append(dec[-1][:])  # Duplicate last factorial decomposition
    for i, p in enumerate(primes):
        while not n % p:
            n //= p
            while i >= len(dec[-1]): dec[-1].append(0)
            dec[-1][i] += 1
            if n < 2: break


def decomp(n):
    while len(dec) <= n:
        genPrimeDivs(len(dec))
    return " * ".join(str(p) if c == 1 else "{}^{}".format(p, c) for p, c in zip(primes, dec[n]))

---
is_prime = lambda n: n == 2 or n % 2 and all(n % d for d in range(3, int(n ** .5) + 1, 2))
order = lambda n, k: n and n // k + order(n // k, k)
decomp = lambda n: ' * '.join(str(p) if n < 2 * p else '%d^%d' % (p, order(n, p)) for p in range(2, n+1) if is_prime(p))

---
from math import sqrt, floor
from collections import Counter

def fac(n):
    step = lambda x: 1 + (x<<2) - ((x>>1)<<1)
    maxq = long(floor(sqrt(n)))
    d = 1
    q = n % 2 == 0 and 2 or 3
    while q <= maxq and n % q != 0:
        q = step(d)
        d += 1
    return q <= maxq and [q] + fac(n//q) or [n]

def decomp(n):
    res = []
    for k, v in sorted(Counter([z for y in map(fac, [x for x in range(2, n+1)]) for z in y]).items()):
        if v != 1: res.append(str(k) + "^"+ str(v))
        else: res.append(str(k))
    return " * ".join(res)
