arr = [1,2,3]
def sum_array(arr):
    if arr==None:
        return 0
    elif len(arr)>1:
        arr.remove(min(arr))
        arr.remove(max(arr))
        return sum(arr)
    else:
        return 0
print(sum_array(arr))