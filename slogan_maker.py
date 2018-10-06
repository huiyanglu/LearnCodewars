import itertools
a1 = ['super','hot','b']
a1s = list(set(a1))
a1s.sort(key=a1.index)
x = list(itertools.permutations(a1s,3))

print(a1s)


