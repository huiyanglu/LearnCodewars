def give_triang(per):
    r1 = []
    for b in range(3,per-2):
        if (2 * b > per):
            break
        for c in range(b,per-2):
            if (b + 2 * c > per):
                break
            a = (b * b + b * c + c * c) ** 0.5
            if a+b+c<=per and a == int(a):
                result = [b,c,a]
                r1.append(result)
                c+=1
        b+=1
    return len(r1)