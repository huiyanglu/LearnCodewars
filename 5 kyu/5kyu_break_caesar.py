"""
Break the Caesar!

https://www.codewars.com/kata/598e045b8c13926d8c0000e8

The Caesar cipher is a notorious (and notoriously simple) algorithm for encrypting a message: each letter is shifted a certain constant number of places in the alphabet. For example, applying a shift of 5 to the string "Hello, world!" yields "Mjqqt, btwqi!", which is jibberish.

In this kata, your task is to decrypt Caesar-encrypted messages using nothing but your wits, your computer, and a set of the 1000 (plus a few) most common words in English in lowercase (made available to you as a preloaded variable named WORDS, which you may use in your code as if you had defined it yourself).

Given a message, your function must return the most likely shift value as an integer.
A few hints:

Be wary of punctuation
Shift values may not be higher than 25

"""

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
