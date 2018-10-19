def iq_test(lines):
    even = []
    odd = []
    integers = lines.split(' ')
    #分割每个数字，分别加引号，成为一个数组[]
    print(integers)
    for num in integers:
        if int(num) % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    if len(even)>1 and len(odd)==1:
        spec = odd[0]
        return integers.index(spec)+1
        #index生成该数字的索引，即在数列中的位置，从0开始

    elif len(odd)>1 and len(even)==1:
        spec = even[0]
        return integers.index(spec)+1

print(iq_test('1 3 5 7 8'))
