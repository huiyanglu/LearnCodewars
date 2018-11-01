import itertools
from functools import reduce

def count_find_num(primesL,limit):
    prod_base = reduce(lambda x,y:x*y,primesL)
    rst = [1]+[i for i in primesL]
    count = 0
    for num in range(2,25):
        each_comb = [i for i in itertools.combinations_with_replacement(primesL, num)]
        for j in range(0,len(each_comb)):
            changetoint = [int(i) for i in each_comb[j]]
            prod_each_comb = reduce(lambda x,y:x*y,changetoint)
            rst.append(prod_each_comb)
    sorted_prod_lst = sorted(rst)
    for num2 in range(0,len(sorted_prod_lst)):
        final_rst = sorted_prod_lst[num2]*prod_base
        if final_rst<=limit:
            count+=1
        elif limit<prod_base:
            return []
        else:
            return [count,prod_base*(sorted_prod_lst[count-1])]

print(count_find_num([2, 181, 277, 449],183207235273926))

