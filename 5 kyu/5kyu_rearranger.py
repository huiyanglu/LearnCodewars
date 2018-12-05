"""
Rearrangement of Numbers to Have The Minimum Divisible by a Given Factor
https://www.codewars.com/kata/569e8353166da6908500003d/solutions/python

Description:
A function receives a certain numbers of integers n1, n2, n3 ...., np(all positive different from 0) and a factor k, k > 0

The function rearranges the numbers n1, n2, ....., np in such order that generates the minimum number concatenating the digits and this number should be divisible by k.

The order that the function receives their arguments is:

rearranger(k, n1, n2, n3,....,np)
See these examples:

rearranger(4, 32, 3, 34, 7, 12) == "Rearrangement: 12, 3, 34, 7, 32 generates: 12334732 divisible by 4"

rearranger(10, 32, 3, 34, 7, 12) ==  "There is no possible rearrangement"
If there are more than one possible arrengement for the same minimum number, your code should be able to handle those cases.

Let's see:

rearranger(6,19, 32, 2, 124, 20, 22) == "Rearrangements: 124, 19, 20, 2, 22, 32 and 124, 19, 20, 22, 2, 32 generates: 124192022232 divisible by 6"
The arrangements should be in sorted order, as you see: 124, 19, 20, 2, 22, 32 comes first than 124, 19, 20, 22, 2, 32.

"""

import itertools

def rearranger(k,*args):
    lst = [i for i in args]
    rst = [str(i) for i in lst]
    perm_lst1 = []
    perm_lst2 = []
    i = 0
    lowest = 0
    for j in itertools.permutations(rst, len(rst)):
        perm_lst1.append(j)
        perm_lst2.append(''.join(j))
        if int(perm_lst2[i])%k==0:
            if lowest==0 or int(perm_lst2[i])<lowest:
                lowest = int(perm_lst2[i])
        i+=1
    if lowest == 0:
        return "There is no possible rearrangement"
    else:
        rst_index = [i for i,z in enumerate(perm_lst2) if int(z)==lowest]
        if len(rst_index)==1 or (len(rst_index)!=1 and perm_lst1[rst_index[0]]==perm_lst1[rst_index[1]]):
            rst_num = [str(i) for i in perm_lst1[rst_index[0]]]
            return 'Rearrangement: '+', '.join(rst_num)+' generates: '+str(lowest)+' divisible by '+str(k)
        else:
            rst_num1 = [str(i) for i in perm_lst1[rst_index[0]]]
            rst_num2 = [str(i) for i in perm_lst1[rst_index[1]]]
            return 'Rearrangements: '+', '.join(rst_num1)+' and '+', '.join(rst_num2)+'generates: '+str(lowest)+' divisible by '+str(k)

print(rearranger(4, 32, 3, 34, 7, 12))