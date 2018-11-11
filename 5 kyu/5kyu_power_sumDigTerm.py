"""
Numbers that are a power of their sum of digits

https://www.codewars.com/kata/55f4e56315a375c1ed000159

The number 81 has a special property, a certain power of the sum of its digits is equal to 81 (nine squared). Eighty one (81), is the first number in having this property (not considering numbers of one digit). The next one, is 512. Let's see both cases with the details

8 + 1 = 9 and 92 = 81

512 = 5 + 1 + 2 = 8 and 83 = 512

We need to make a function, power_sumDigTerm(), that receives a number n and may output the n-th term of this sequence of numbers. The cases we presented above means that

power_sumDigTerm(1) == 81

power_sumDigTerm(2) == 512

"""


def power_sumDigTerm(n):
    m = [0]

    for a in range(2,99):
        for b in range(2,42):
            cc = a**b
            i2 = str(cc)
            c = [int(i2[i]) for i in range(0, len(i2))]
            sum1 = sum(c)
            if a == sum1:
                m.append(cc)

    return sorted(m)[n]

print(power_sumDigTerm(6))



