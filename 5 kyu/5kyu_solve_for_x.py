"""
Solve For X

https://www.codewars.com/kata/59c2e2a36bddd2707e000079

You will be given an equation as a string and you will need to solve for X and return x's value. For example:

solve_for_x('x - 5 = 20') # should return 25
solve_for_x('20 = 5 * x - 5') # should return 5
solve_for_x('5 * x = x + 8') # should return 2
solve_for_x('(5 - 3) * x = x + 2') # should return 2
NOTES:

All numbers will be whole numbers
Don't forget about the order of operations.
If the random tests don't pass the first time, just run them again.

"""

def solve_for_x(equation):
    for x in range(-1000,1001):
        if eval(equation.replace('=','==')):
            return x

print(solve_for_x('2*x+1=5'))
