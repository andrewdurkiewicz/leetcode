#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) 
        for i in range(1, len(nums)): # from left to right we multiply 
            print("-----------")
            print(res)
            res[i] = res[i-1] * nums[i-1]
            print(res)
            print("-------------")
        tmp = 1
        for i in range(len(nums)-2, -1, -1): # from right to left
            tmp *= nums[i+1]
            res[i] *= tmp
        return res

S = Solution()
print(S.productExceptSelf([2,3,4,5]))
        
# @lc code=end

