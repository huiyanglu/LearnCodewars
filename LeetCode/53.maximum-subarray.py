#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max,curr=nums[0],0
        for x in nums:
            curr+=x
            #if curr<0:curr=0
            if curr>max:max=curr
        return max

