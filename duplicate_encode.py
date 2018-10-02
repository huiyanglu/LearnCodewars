from collections import Counter
import re

def duplicate_encode(n):
    nn = n.lower()
    dct = dict(Counter(nn))
    del_1 = dict((key,value)for key,value in dct.items()if value!=1)
    b = [i for i in del_1.keys()]
    nn.split(',')
    a = []
    for i in range(0, len(nn)):
        if nn[i] in b:
            num = re.sub(r'\D', ")", nn[i])
        else:
            num = re.sub(r'[0-9a-zA-Z\s\_\@\(\)\*\:\!\'\"]', "(", nn[i])
        a.append(num)
        i += 1
    return ''.join(a)
