#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#
# https://leetcode.com/problems/count-and-say/description/
#
# algorithms
# Easy (40.07%)
# Total Accepted:    273.6K
# Total Submissions: 681.9K
# Testcase Example:  '1'
#
# The count-and-say sequence is the sequence of integers with the first five
# terms as following:
# 
# 
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 
# 
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# 
# Given an integer n where 1 ≤ n ≤ 30, generate the n^th term of the
# count-and-say sequence.
# 
# Note: Each term of the sequence of integers will be represented as a
# string.
# 
# 
# 
# Example 1:
# 
# 
# Input: 1
# Output: "1"
# 
# 
# Example 2:
# 
# 
# Input: 4
# Output: "1211"
# 
#
import re

class Solution:
    def countAndSay(self, n: int) -> str:
        i = 1
        count_i = self.count_and_say(i)
        if n==1:return "1"
        while i<n-1:
            count_i = self.count_and_say(count_i)
            i+=1
        return count_i
    def count_and_say(self, n:int):
        result = ''
        strn = str(n)
        char = strn[0]
        count = 0
        for each in strn:
            if char==each:
                count+=1
            else:
                result += (str(count)+char)
                char = each
                count = 1
        result += (str(count)+char)
        return result


