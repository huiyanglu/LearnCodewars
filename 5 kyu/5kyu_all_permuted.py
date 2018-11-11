"""
Shuffle It Up

https://www.codewars.com/kata/shuffle-it-up/python

We have an array of unique elements. A special kind of permutation is the one that has all of its elements in a different position than the original.

Let's see how many of these permutations may be generated from an array of four elements. We put the original array with square brackets and the wanted permutations with parentheses.

arr = [1, 2, 3, 4]
      (2, 1, 4, 3)
      (2, 3, 4, 1)
      (2, 4, 1, 3)
      (3, 1, 4, 2)
      (3, 4, 1, 2)
      (3, 4, 2, 1)
      (4, 1, 2, 3)
      (4, 3, 1, 2)
      (4, 3, 2, 1)
      _____________
A total of 9 permutations with all their elements in different positions than arr
The task for this kata would be to create a code to count all these permutations for an array of certain length.

Features of the random tests:

l = length of the array
10 ≤ l ≤ 5000

"""

def all_permuted(n):
    a,b = 0, 1
    for i in range(1,n):
        a,b = b, (i+1)*(a+b)
    return a

print(all_permuted(4))
