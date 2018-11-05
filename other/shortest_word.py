s = input("Input the words:")

l_split = s.split(' ')
shortest = 100
for word in l_split:
    if len(word)<shortest:
        shortest = len(word)
print(shortest)
