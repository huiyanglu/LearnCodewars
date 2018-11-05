def change(x):
    h1 = x // 3600
    m1 = (x - 3600 * h1) // 60
    s1 = x - 3600 * h1 - 60 * m1
    return h1,m1,s1

def stat(strg):
    if strg =='':
        return ''
    else:
        s = strg.split(',')
        lst = []
        sum = 0
        l = len(s)
        try:
            int('')
        except ValueError:
            pass
        for i in range(0,l):
            b1 = s[i].split('|')  # 数列的第一个数将数字分隔开
            c1 = int(b1[0]) * 3600 + int(b1[1]) * 60 + int(b1[2])
            lst.append(c1)
            sum += lst[i]
        avg = sum//l
        rge = max(lst)-min(lst)
        if l%2 == 0:
            lst.sort()
            med = (lst[l//2]+lst[l//2-1])/2
        else:
            lst.sort()
            med = lst[l//2]
        avgr = change(avg)
        rger = change(rge)
        medr = change(med)
        return "Range: %02d|%02d|%02d "%rger+"Average: %02d|%02d|%02d "%avgr+"Median: %02d|%02d|%02d"%medr

