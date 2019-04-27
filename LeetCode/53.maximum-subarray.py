#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max,curr=-10000000000,0
        for x in nums:
            if curr<0:curr=0
            curr+=x
            if curr>max:max=curr
        return max

