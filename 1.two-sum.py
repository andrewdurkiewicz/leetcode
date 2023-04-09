#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for idx, val in enumerate(nums):
            mydict[val] = idx
        for idx, val in enumerate(nums):
            if (tmp := mydict.get(target-val)) and tmp != idx:
                return [idx, tmp]    

# @lc code=end

