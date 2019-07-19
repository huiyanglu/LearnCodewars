#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        if len(prices)==0:
            return 0
        min = prices[0]
        for i in range(len(prices)):
            if prices[i] < min:
                min = prices[i]
            if prices[i] - min > maxProfit:
                maxProfit = prices[i] - min
        return maxProfit

