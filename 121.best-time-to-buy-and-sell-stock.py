#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock I
#

# @lc code=start
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #find where to start on left
        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit,profit)
            else:
                l = r
            r+=1
        return maxProfit

# @lc code=end