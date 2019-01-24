"""
Square into Squares. Protect trees!

https://www.codewars.com/kata/54eb33e5bc1a25440d000891/solutions/python

My little sister came back home from school with the following task: given a squared sheet of paper she has to cut it in pieces which, when assembled, give squares the sides of which form an increasing sequence of numbers. At the beginning it was lot of fun but little by little we were tired of seeing the pile of torn paper. So we decided to write a program that could help us and protects trees.

Examples
decompose(11) must return [1,2,4,10]. Note that there are actually two ways to decompose 11², 11² = 121 = 1 + 4 + 16 + 100 = 1² + 2² + 4² + 10² but don't return [2,6,9], since 9 is smaller than 10.

For decompose(50) don't return [1, 1, 4, 9, 49] but [1, 3, 5, 8, 49] since [1, 1, 4, 9, 49] doesn't form a strictly increasing sequence.
"""
def decompose(n):
    rst = [n]
    rest = 0
    while rst:
        current = rst.pop()
        rest += current**2
        for i in range(current-1,0,-1):
            if rest - (i**2) >=0:
                rest -= i**2
                rst.append(i)
                if rest == 0:
                    return sorted(rst)
    return None

print(decompose(50))