def sum_pairs(ints, s):
    rst = set()
    for i in range(0,len(ints)):
        if s - ints[i] in rst:
            return [s - ints[i],ints[i]]
        rst.add(ints[i])
