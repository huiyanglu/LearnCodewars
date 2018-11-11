"""
Description:
https://en.wikipedia.org/wiki/Diophantine_equation
In mathematics, a Diophantine equation is a polynomial equation, usually with two or more unknowns, such that only the integer solutions are sought or studied.

In this kata we want to find all integers x, y (x >= 0, y >= 0) solutions of a diophantine equation of the form:

x2 - 4 * y2 = n
(where the unknowns are x and y, and n is a given positive number) in decreasing order of the positive xi.

If there is no solution return [] or "[]" or "". (See "RUN SAMPLE TESTS" for examples of returns).

Examples:
solEquaStr(90005) --> "[[45003, 22501], [9003, 4499], [981, 467], [309, 37]]"
solEquaStr(90002) --> "[]"
Hint:
x2 - 4 * y2 = (x - 2*y) * (x + 2*y)
"""

import math

def sol_equa(n):
    rst = []
    for i in range(1,int(math.sqrt(n))+1):
        if n % i != 0:
            continue
        j = n//i
        x = (i+j)//2
        y = (j-i)//4
        if x>=0 and y>=0 and (i==x-2*y) and (j ==x+2*y):
            rst.append([x,y])
    return rst

print(sol_equa(16))
