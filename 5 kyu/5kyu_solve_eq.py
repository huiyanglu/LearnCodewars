""""
https://www.codewars.com/kata/59280c056d6c5a74ca000149/solutions/python

Description:
We have 3 equations with 3 unknowns x, y, and z and we are to solve for these unknowns.

Equations 4x -3y +z = -10, 2x +y +3z = 0, and -x +2y -5z = 17
will be passed in as an array of [[4, -3, 1, -10], [2, 1, 3, 0], [-1, 2, -5, 17]]
and the result should be returned as an array like [1, 4, -2] (i.e. [x, y, z]).
"""
import numpy as np

def solve_eq(eq):
    lst1 = []
    lst2 = []
    for i in range(0,len(eq)):
        lst1.append(eq[i][-1])
        lst2.append(eq[i][:-1])
    rst = np.linalg.solve(lst2, lst1)
    return [int(round(x)) for x in list(rst)]

eq = [[-26, 28, 13, -124], [7, -26, -24, -63], [28, -2, -4, 238]]
print(solve_eq(eq))
