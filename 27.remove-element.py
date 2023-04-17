#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        while idx < len(nums):
            if nums[idx] == val:
                nums[:] = nums[:idx] + nums[idx+1:]
            else:
                idx +=1
        return len(nums)

# @lc code=end

