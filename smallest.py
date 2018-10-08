def smallest(n):
    n2 = [i for i in str(n)]
    x = []
    for i,n in enumerate(n2):
        ns = list(n2)
        ns.pop(i)
        for j in range(len(n2)):
            x2 = list(ns)
            x2.insert(j,n)
            x2 = int(''.join(x2))
            x.append([x2,i,j])
    return min(x,key = lambda x:x[0])
