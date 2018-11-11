"""
Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....¡Eureka!!

https://www.codewars.com/kata/5626b561280a42ecc50000d1

The number 89 is the first integer with more than one digit that fulfills the property partially introduced in the title of this kata. What's the use of saying "Eureka"? Because this sum gives the same number.

In effect: 89 = 8^1 + 9^2

The next number in having this property is 135.

See this property again: 135 = 1^1 + 3^2 + 5^3

We need a function to collect these numbers, that may receive two integers a, b that defines the range [a, b] (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described above.

Let's see some cases:

sum_dig_pow(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

sum_dig_pow(1, 100) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
If there are no numbers of this kind in the range [a, b] the function should output an empty list.

sum_dig_pow(90, 100) == []
"""

def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    # your code here
    lst = []
    for i in range(a,b+1):
        if if_true(i):
            lst.append(i)
    return lst

def if_true(num):
    num2 = num
    i = len(str(num))
    s = 0
    while num2!=0:
        mod = num2%10
        num2//=10
        s+=mod**i
        i-=1
    if(s==num):
        return True
    else:
        return False
