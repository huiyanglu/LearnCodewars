def maxSequence(arr):
    if arr == []:
        return 0
    else:
        a = []
        for i in range(0,len(arr)):
            for j in range(0,len(arr)):
                sum2 = sum(arr[i:j+1])
                a.append(sum2)
        return max(a)

print(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))