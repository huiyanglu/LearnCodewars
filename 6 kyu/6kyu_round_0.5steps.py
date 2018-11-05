def solution(a):
    b = int(a)
    c = a - b
    if c<0.25:
        return b
    elif c>0.25 and c<0.75:
        return b+0.5
    elif c > 0.75:
        return b+1
    else:
        return a+0.25
