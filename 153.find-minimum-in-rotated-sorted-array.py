#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        currMin = nums[0]
        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] < nums[r]:
                currMin = min(currMin, nums[l])
                break
            middle = (l+r)//2
            currMin = min(currMin, nums[middle])
            if nums[middle] >= nums[l]:
                l = middle+1
            else:
                r = middle-1
        return currMin

# @lc code=end

