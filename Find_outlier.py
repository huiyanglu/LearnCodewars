def find_outlier(integers):
    even = []
    odd = []
    for num in integers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    if len(even)>1 and len(odd)==1:
        return odd[0]
    elif len(odd)>1 and len(even)==1:
        return even[0]

print(find_outlier([1,2,3]))
