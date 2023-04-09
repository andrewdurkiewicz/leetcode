#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_dict = {}
        returnSet = set()
        for idx, val in enumerate(nums):
            nums_dict[val] = idx
        for idc, c in enumerate(nums):
            negative_c = -1 * c
            # Just do the two sum for this
            for idb, b in enumerate(nums):
                if (idc == idb):
                    continue
                # a + b + c = 0, thus a = 0 - b - c a = -c-b
                a = negative_c - b
                if (ida := nums_dict.get(a)) and (ida != idb) and (ida != idc):
                    tmp = [a, b, c]
                    tmp.sort()
                    returnSet.add(tuple(tmp))
                
        return list(returnSet)
        
# @lc code=end

