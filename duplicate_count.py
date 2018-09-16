from collections import Counter
def duplicate_count(n):
    nn = n.lower()
    dct = dict(Counter(nn))
    del_1 = dict((key,value)for key,value in dct.items()if value!=1)
    return len(del_1)

print(duplicate_count('aabbcCc1'))