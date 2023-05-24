#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lptr, rptr = 0, len(nums)-1

        while lptr <= rptr:
            middleIndex = (lptr+rptr) // 2
            if nums[middleIndex] > target:
                rptr = middleIndex - 1
            elif nums[middleIndex] < target:
                lptr = middleIndex + 1
            else:
                #must be equal
                return middleIndex
        return -1
                
# @lc code=end

