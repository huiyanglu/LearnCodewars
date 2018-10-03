# wrong answer
# Timed out!

def find_all(sum2, b):
    x = []
    for a in range(10**(b-1),10**b):
        i2 = str(a)
        c = [int(i2[i]) for i in range(0, len(i2))]
        if c == sorted(c):
            if sum(c) == sum2:
                x.append(a)
            else:
                a += 1
        else:
            a+=1
    if x == []:
        return []
    else:
        return [len(x),x[0],x[-1]]

print(find_all(10,3))