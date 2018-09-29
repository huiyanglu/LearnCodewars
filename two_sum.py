def two_sum(a, b):
    for i in range(0,len(a)):
        x = a[i]
        y = b - x
        for j in range(1,len(a)):
            if y == a[j]:
                return [i,j]
            else:
                j+=1
        i+=1
