def alphabet_position(text):
    lst = []
    court = 0
    txt = text.lower()
    for i in range(0,len(text)):
        if txt[i].isalpha():
            b = ord(txt[i])-96
            lst.append(b)
            i+=1
        else:
            i+=1
    return ' '.join(str(x) for x in lst)