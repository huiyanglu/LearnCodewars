#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_rst = [str(i) for i in digits]
        int_rst = int(''.join(str_rst))+1
        rst = [int(i) for i in str(int_rst)]
        return rst

