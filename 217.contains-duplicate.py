#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniqueSet = set()
        for val in nums:
            if val in uniqueSet:
                return True
            else:
                uniqueSet.add(val)
        return False
# @lc code=end

