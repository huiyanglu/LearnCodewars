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