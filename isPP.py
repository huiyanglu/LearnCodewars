from math import ceil, log, sqrt
 
def isPP(n):
    for m in range(2, int(sqrt(n)) + 1):
        k = int(round(log(n, m)))
        if m ** k == n:
            return [m, k]
    return None
 
 
