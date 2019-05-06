#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split(' ')
        l2=[]
        for each in l:
            if each!='':
                l2.append(each)
        if l2:return len(l2[-1])
        else:return 0

