#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int1=int(a,2)+int(b,2)
        return bin(int1)[2:]

