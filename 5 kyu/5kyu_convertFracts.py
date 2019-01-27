"""
Common Denominators

https://www.codewars.com/kata/54d7660d2daf68c619000d95

You will have a list of rationals in the form

 { {numer_1, denom_1} , ... {numer_n, denom_n} }
or

 [ [numer_1, denom_1] , ... [numer_n, denom_n] ]
or

 [ (numer_1, denom_1) , ... (numer_n, denom_n) ]
where all numbers are positive ints.

You have to produce a result in the form

 (N_1, D) ... (N_n, D)
or

 [ [N_1, D] ... [N_n, D] ]
or

 [ (N_1', D) , ... (N_n, D) ]
or

{{N_1, D} ... {N_n, D}}
depending on the language (See Example tests)

in which D is as small as possible and

 N_1/D == numer_1/denom_1 ... N_n/D == numer_n,/denom_n.
Example:

convertFracs [(1, 2), (1, 3), (1, 4)] `shouldBe` [(6, 12), (4, 12), (3, 12)]
Note for Bash
input is a string, e.g "2,4,2,6,2,8"

output is then "6 12 4 12 3 12"

"""


from functools import reduce
from math import gcd

def get_lcm(lst):
    return reduce(lambda a,b: a * b // gcd(a, b),lst)

def convertFracts(lst):
    my_gcd = reduce(gcd,[i[0]+i[1] for i in lst])
    my_lcm = get_lcm([i[1]//my_gcd for i in lst])
    return [[i[0]*my_lcm//i[1],my_lcm] for i in lst]

a = [[2,4], [2, 6], [2, 8]]
print(convertFracts(a))
