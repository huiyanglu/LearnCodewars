def who_eats_who(zoo):
    a = [['grass','antelope'],
    ['little-fish', 'big-fish'],
    ['leaves','bug'],
    ['big-fish', 'bear'],
    ['bug', 'bear'],
    ['chicken','bear'],
    ['cow','bear'],
    ['leaves','bear'],
    ['sheep','bear'],
    ['bug','chicken'],
    ['grass', 'cow'],
    ['chicken', 'fox'],
    ['sheep','fox'],
    ['leaves','giraffe'],
    ['antelope','lion'],
    ['cow', 'lion'],
    ['leaves','panda'],
    ['grass','sheep']]
    init = zoo.split(',')
    rst = []
    j = 0
    while j<len(init):
        if j > 0 and [init[j-1],init[j]] in a:
            rst.append(init[j]+' eats '+init[j-1])
            init.pop(j-1) # pop可以，用remove就报错
            j = 0
        elif j<len(init)-1 and [init[j+1],init[j]] in a:
            rst.append(init[j] + ' eats ' + init[j + 1])
            init.pop(j+1)
            j = 0
        else:
            j+=1
    return [zoo]+rst + [",".join(init)]

print(who_eats_who('fox,bug,chicken,grass,sheep'))



