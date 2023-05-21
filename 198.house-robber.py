#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
# from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        bestPossible = [0 for _ in range(len(nums))]
        currHouseIndex = 0
        while currHouseIndex < len(nums):
            previousHouseIndex = currHouseIndex-1
            skipPreviousIndex = currHouseIndex-2
            maxSkipRob = 0
            maxRob = nums[currHouseIndex]
            if previousHouseIndex >= 0:
                maxSkipRob+=bestPossible[previousHouseIndex]
            if skipPreviousIndex >= 0:
                maxRob+=bestPossible[skipPreviousIndex]
            bestPossible[currHouseIndex] = max(maxRob, maxSkipRob)
            currHouseIndex+=1
        return bestPossible[-1]
# s = Solution()
# print(s.rob([2,7,9,3,1]))
# @lc code=end

