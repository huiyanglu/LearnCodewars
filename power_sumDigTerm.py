def power_sumDigTerm(n):
    m = [0]

    for a in range(2,99):
        for b in range(2,42):
            cc = a**b
            i2 = str(cc)
            c = [int(i2[i]) for i in range(0, len(i2))]
            sum1 = sum(c)
            if a == sum1:
                m.append(cc)

    return sorted(m)[n]

print(power_sumDigTerm(6))



