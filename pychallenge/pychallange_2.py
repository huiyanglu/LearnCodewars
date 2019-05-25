def ans():
    text1 = open('hint.txt','r')
    text2 = text1.read()
    rst = []
    for each in text2:
        if each.isalpha():
            rst.append(each)
    return ''.join(rst)
print(ans())