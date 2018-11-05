def largest_rect(histogram):
    histogram.append(0)
    stack = [-1] # s是h1的index的序列
    result = 0
    for i in range(0,len(histogram)):
        while histogram[i] < histogram[stack[-1]]:#s序列的最后一位对应的h1里的数
            h = histogram[stack.pop()] # []里是去掉的那个数
            w = i - stack[-1] - 1
            result = max(result, h * w)
        stack.append(i)
    histogram.pop()
    return result

print(largest_rect([3,4,5,4,3,4,5]))