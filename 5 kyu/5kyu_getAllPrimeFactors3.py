from collections import defaultdict

def getUniquePrimeFactorsWithCount(n):
    decomp = defaultdict(lambda:0)
    i = 2
    count = []
    num = []
    if str(n).isdigit():
        if n == 1:
            return [[1], [1]]
        else:
            while int(n) > 1:
                while n % i == 0:
                    n /= i
                    decomp[i] += 1
                i += 1
            for key,value in decomp.items():
                count.append(value)
                num.append(key)
            return [num,count]
    else:
        return [[],[]]


def getAllPrimeFactors(n):
    dec = []
    i = 2
    if str(n).isdigit():
        if n == 1:
            return [1]
        else:
            while n > 1:
                while n % i == 0:
                    n /= i
                    dec.append(i)
                i += 1
            return dec
    else:
        return []

def getUniquePrimeFactorsWithProducts(n):
    decomp = defaultdict(lambda:0)
    i = 2
    count = []
    if str(n).isdigit():
        if n == 1:
            return [1]
        else:
            while n > 1:
                while n % i == 0:
                    n /= i
                    decomp[i] += 1
                i += 1
            for key,value in decomp.items():
                count.append(key**value)
            return count
    else:
        return []

print(getUniquePrimeFactorsWithCount('a'))