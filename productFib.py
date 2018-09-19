def productFib(prod):
    a = [0,1,1]
    b = [0,1,2]
    for i in range(2,100):
        a[i]=a[i-1]+a[i-2]
        a.append(a[i])
        i+=1
    for j in range(2,100):
        b[j]=a[j]*a[j+1]
        b.append(b[j])
        j+=1
    for x in range(0,100):
        if prod - b[x] == 0:
            return [a[x],a[x+1],True]
        else:
            x+=1
        if prod != b[x]:
            for y in range(0, 100):
                if prod > b[y] and prod < b[y + 1]:
                    if prod - b[y] > prod - b[y + 1]:
                        return [a[y + 1], a[y + 2], False]
                    elif prod - b[y] < prod - b[y + 1]:
                        return [a[y], a[y + 1], False]
                else:
                    y += 1

print(productFib(105))