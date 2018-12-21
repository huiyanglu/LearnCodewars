"""
Integers: Recreation One

https://www.codewars.com/kata/55aa075506463dac6600010d/solutions/python

Description:
Divisors of 42 are : 1, 2, 3, 6, 7, 14, 21, 42. These divisors squared are: 1, 4, 9, 36, 49, 196, 441, 1764. The sum of the squared divisors is 2500 which is 50 * 50, a square!

Given two integers m, n (1 <= m <= n) we want to find all integers between m and n whose sum of squared divisors is itself a square. 42 is such a number.

The result will be an array of arrays or of tuples (in C an array of Pair) or a string, each subarray having two elements, first the number whose squared divisors is a square and then the sum of the squared divisors.

#Examples:

list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
list_squared(42, 250) --> [[42, 2500], [246, 84100]]
The form of the examples may change according to the language, see Example Tests: for more details.

Note

In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use dynamically allocated character strings.

"""
import math

def list_squared(m,n):
    lst = []
    for num in range(m,n+1):
        rst = getDivisor(num)
        if (rst**0.5)%1==0:
            lst.append([num,rst])
        else:
            num+=1
    return lst

def getDivisor(num):
    sum1 = 0
    sq_num = int(math.sqrt(num))
    for i in range(1, sq_num + 1):
        if num % i == 0:
            sum1 += i ** 2
            if int(num/i)!=i:
                sum1 += int(num/i)**2
    return sum1