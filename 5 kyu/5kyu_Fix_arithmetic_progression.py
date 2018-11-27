"""
https://www.codewars.com/kata/5b77b030f0aa5c9114000024/solutions/python

Description:
In this Kata, we define an arithmetic progression
as a series of integers in which the differences
between adjacent numbers are the same.
You will be given an array of ints of length > 2
and your task will be to convert it into an arithmetic progression
by the following rule:

For each element there are exactly three options:
an element can be decreased by 1, an element can be increased by 1
or it can be left unchanged.

Return the minimum number of changes
needed to convert the array to an arithmetic progression.
If not possible, return -1.

For example:
solve([1,1,3,5,6,5]) == 4 because [1,1,3,5,6,5] can be changed to [1,2,3,4,5,6] by making 4 changes.
solve([2,1,2]) == 1 because it can be changed to [2,2,2]
solve([1,2,3]) == 0  because it is already a progression, and no changes are needed.
solve([1,1,10) == -1 because it's impossible.
solve([5,6,5,3,1,1]) == 4. It becomes [6,5,4,3,2,1]
"""
def solve(arr):
    rst = []
    for x0 in (arr[0],arr[0]-1,arr[0]+1):
        for x1 in (arr[1],arr[1]-1,arr[1]+1):
            delta = x1 - x0
            diff = [x0 != arr[0]] + [abs(x0 + i*delta - arr[i]) for i in range(1,len(arr))]
            if all(each_dif <= 1 for each_dif in diff):
                rst.append(sum(diff))
    return min(rst) if rst else -1

print(solve([24,21,14,10]))