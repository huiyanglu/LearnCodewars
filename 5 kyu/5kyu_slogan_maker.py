"""
All Star Code Challenge #19

https://www.codewars.com/kata/5865a407b359c45982000036

This Kata is intended as a small challenge for my students

All Star Code Challenge #19

You work for an ad agency and your boss, Bob, loves a catchy slogan. He's always jumbling together "buzz" words until he gets one he likes. You're looking to impress Boss Bob with a function that can do his job for him.

Create a function called sloganMaker() that accepts an array of string "buzz" words. The function returns an array of all possible UNIQUE string permutations of the buzz words (concatonated and separated by spaces).

Your boss is not very bright, so anticipate him using the same "buzz" word more than once, by accident. The function should ignore these duplicate string inputs.

sloganMaker(["super", "hot", "guacamole"]);
//[ 'super hot guacamole',
//  'super guacamole hot',
//  'hot super guacamole',
//  'hot guacamole super',
//  'guacamole super hot',
//  'guacamole hot super' ]

sloganMaker(["cool", "pizza", "cool"]); // => [ 'cool pizza', 'pizza cool' ]
Note:
There should be NO duplicate strings in the output array The input array MAY contain duplicate strings, which should STILL result in an output array with all unique strings An empty string is valid input
The order of the permutations in the output array does not matter

"""

import itertools

def slogan_maker(a):
    a2 = list(set(a))
    a2.sort(key=a.index) # 字符串去重后按原顺序排列
    x = []
    result = list(itertools.permutations(a2, len(a2))) # 字符串排列组合考虑顺序
    for i in range(0,len(result)):
        x.append(' '.join(result[i]))
    return x 
