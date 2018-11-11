"""
Factorial decomposition

https://www.codewars.com/kata/5a045fee46d843effa000070

The aim of the kata is to decompose n! (factorial n) into its prime factors.

Examples:

n = 12; decomp(12) -> "2^10 * 3^5 * 5^2 * 7 * 11"
since 12! is divisible by 2 ten times, by 3 five times, by 5 two times and by 7 and 11 only once.

n = 22; decomp(22) -> "2^19 * 3^9 * 5^4 * 7^3 * 11^2 * 13 * 17 * 19"

n = 25; decomp(25) -> 2^22 * 3^10 * 5^6 * 7^3 * 11^2 * 13 * 17 * 19 * 23
Prime numbers should be in increasing order. When the exponent of a prime is 1 don't put the exponent.

Notes

the function is decomp(n) and should return the decomposition of n! into its prime factors in increasing order of the primes, as a string.
factorial can be a very big number (4000! has 12674 digits, n will go from 300 to 4000).
In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use dynamically allocated character strings.

"""

def decomp(num):
    ans = []
    for i in range(2, num + 1):
        ans += primeFactor(i)
    sorted_myset = sorted(set(ans))
    ones = []
    single_ones = []
    for item in sorted_myset:
        if ans.count(item)>1:
            each_one = str("%d^%d" %(item, ans.count(item)))
            ones.append(each_one)
        else:
            single_ones.append(str(item))
        ones2 = ones + single_ones
    return ' * '.join(ones2)

def primeFactor(n):
    lst = []
    i = 2
    while n > 1:
        while n % i == 0: #如果能被i整除
            n /= i
            lst.append(i) #在list里加入i的值
        i += 1 #如果不能被整除，则i+1
    return lst
