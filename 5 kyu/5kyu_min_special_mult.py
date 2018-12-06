"""
Find The Minimum Number Divisible by Integers of an Array II
https://www.codewars.com/kata/56f1b3c94d0c330e4a000e95/solutions/python

Description:
Given a certain array of integers, create a function that may give the minimum number that may be divisible for all the numbers of the array.

This will be a harder version of Find The Minimum Number Divisible by integers of an array I

This is an example that shows how many times, a brute force algorithm cannot give a fast solution. We need the help of maths, in this case of number theory.

We need to apply the prime factorization of a number:

Think in doing the prime factorization of the product of all the different values of the array and think how to obtain from it the minimum number that is divisible by all the values of the array.

See the same cases as the previous part:

min_special_mult([2, 3 ,4 ,5, 6, 7]) == 420
The array may have integers that occurs more than once:

min_special_mult([18, 22, 4, 3, 21, 6, 3]) == 2772
The array should have all its elements integer values. If the function finds an invalid entry (or invalid entries) like strings of the alphabet or symbols will not do the calculation and will compute and register them, outputting a message in singular or plural, depending on the number of invalid entries.

min_special_mult([16, 15, 23, 'a', '&', '12']) == "There are 2 invalid entries: ['a', '&']"

min_special_mult([16, 15, 23, 'a', '&', '12', 'a']) == "There are 3 invalid entries: ['a', '&', 'a']"

min_special_mult([16, 15, 23, 'a', '12']) == "There is 1 invalid entry: a"
If the string is a valid number, the function will convert it as an integer.

min_special_mult([16, 15, 23, '12']) == 5520

min_special_mult([16, 15, 23, '012']) == 5520
All the None elements of the array will be ignored:

min_special_mult([18, 22, 4, , None, 3, 21, 6, 3]) == 2772
If the array has a negative number, the function will convert to a positive one.

min_special_mult([18, 22, 4, , None, 3, -21, 6, 3]) == 2772

min_special_mult([16, 15, 23, '-012']) == 5520
The test for this part will be more challenging having arrays up to 5000 elements and up to 800 different values.

A simple brute force algorithm will not be able to pass the tests. Enjoy it!
"""

from functools import reduce

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def min_special_mult(alist):
    invalid_lst = []
    for i in alist:
        str_i = i
        if str(i)[0]=='-':
            str_i = int(str(i)[1:])
        if isinstance(str_i,str) and not str(str_i).isdigit() and i!=None:
            invalid_lst.append(i)
    if invalid_lst==[]:
        lst2 = [abs(int(i)) for i in alist if i is not None]
        return reduce(lcm,lst2)
    elif len(invalid_lst)==1:
        return 'There is {} invalid entry: {}'.format(str(len(invalid_lst)),str(invalid_lst[0]))
    else:
        return 'There are {} invalid entries: {}'.format(str(len(invalid_lst)), str(invalid_lst))

print(min_special_mult([16, 15, 23,None,'a','b', '-012']))