abc = 'abcdefghijklmnopqrstuvwxyz'

def caesar(s, k):
    trans = str.maketrans(abc, abc[k:] + abc[:k])
    return s.translate(trans)

def break_caesar(message):
    message = ''.join(c if c.isalpha() else ' ' for c in message).lower()
    hits = []
    for k in range(26):
        dec = caesar(message, -k)
        cnt = 0
        for word in dec.split():
            if word in WORDS:
                cnt += 1
        hits.append(cnt)

    return hits.index(max(hits))

# 自己运行判断单词 可用enchant
# import enchant
# d = enchant.Dict("en_US")
# d.check("Hello")
# True/False