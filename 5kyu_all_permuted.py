def all_permuted(n):
    a,b = 0, 1
    for i in range(1,n):
        a,b = b, (i+1)*(a+b)
    return a

print(all_permuted(4))