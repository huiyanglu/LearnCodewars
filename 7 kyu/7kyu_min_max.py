def min_max(lst):
    min = lst[0]
    max = lst[0]
    for i in range(0,len(lst)):
        if lst[i]>max:
            max = lst[i]
        elif lst[i]<min:
            min = lst[i]
        i+1
    return [min,max]