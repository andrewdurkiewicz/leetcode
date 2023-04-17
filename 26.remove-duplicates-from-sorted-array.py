#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = 0 # number of unique index
        index = 0
        while index < len(nums):
            curr_value = nums.pop(index)
            unique+=1
            while index < len(nums) and nums[index] == curr_value:
                nums.pop(index)
            nums.insert(index, curr_value)
            index+=1
        return unique
                

        
# @lc code=end

