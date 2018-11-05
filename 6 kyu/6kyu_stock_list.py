def stock_list(listOfArt, listOfCat):
    if listOfArt == [] or listOfCat == []:
        return ''
    cnt = 0
    rst = ''
    for i in listOfCat:
        for j in listOfArt:
            if i == j[0]:
                sum = ''
                for m in j:
                    if m.isdigit():
                        sum += m
                cnt += int(sum)
        rst += '(' + i + ' : ' + str(cnt) + ') - '
    return rst[:-3]

b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]
print(stock_list(b, c))
