#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
class Solution:
    def mySqrt(self, x: int) -> int:
        left,right = 0,x
        while left<=right:
            mid = left + (right-left)//2
            if mid**2 <= x < (mid+1)**2:
                return mid
            elif x < mid**2:
                right = mid
            else:
                left = mid + 1

