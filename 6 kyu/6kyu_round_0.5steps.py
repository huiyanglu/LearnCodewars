"""
Round by 0.5 steps

https://www.codewars.com/kata/51f1342c76b586046800002a

Round any given number to the closest 0.5 step

I.E.

solution(4.2) = 4
solution(4.3) = 4.5
solution(4.6) = 4.5
solution(4.8) = 5
Round up if number is as close to previous and next 0.5 steps.

solution(4.75) == 5

"""


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
