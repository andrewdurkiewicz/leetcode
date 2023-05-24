#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
               
        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += ceil(p / k)
            if totalTime <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res

        
# @lc code=end

