#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
from typing import List 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        currMax = nums[0] #start of on the left
        currSum = 0
        for val in nums:
            if currSum < 0:
                currSum = 0
            currSum+=val 
            currMax = max(currMax, currSum)
        return currMax


        
        

        
# @lc code=end

