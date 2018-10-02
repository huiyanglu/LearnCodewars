def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mixed_fraction(s):
    m = s.split('/')
    a = int(m[0])
    b = int(m[1])
    if (a >=0 and b>0) or (a<0 and b<0):
        c = a // b
    elif (a<0 and b>0) or (a>0 and b<0):
        c = a//b+1
    elif a==0:
        c = 0
    d = a - c * b
    e = gcd(d, b)
    r2 = abs(b // e)
    if d == 0:
        return '%d' %(c)
    elif d !=0 and c == 0:
        r1 = d // e
        if r2 == 1:
            return '%d' % (r1)
        else:
            return '%d/%d' % (r1, r2)
    else:
        r1 = abs(d // e)
        if r2 == 1:
            c = c-r1
            return '%d' % (c)
        else:
            return '%d %d/%d' % (c, r1, r2)