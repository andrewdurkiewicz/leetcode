#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        split = len(nums) // 2
        if target <= nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        elif target < nums[-1]:
            #split in half
            return self.searchInsert(nums[0:split], target) + self.searchInsert(nums[split:], target)
        else:
            # Target must be equal to the end. return len(nums) - 1 for index
            return len(nums) - 1
# @lc code=end

        


