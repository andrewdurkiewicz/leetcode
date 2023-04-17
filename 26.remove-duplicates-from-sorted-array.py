#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
from collections import OrderedDict
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numbers = OrderedDict()
        for val in nums:
            numbers[val] = 1
        nums[:] = list(numbers.keys())
        return len(nums)
      
# @lc code=end

