#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
# from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        od = {}
        for num in nums:
            if num in od.keys():
                od[num]+=1
            else:
                od[num] = 1
        array = sorted(od.items(), key= lambda x: x[1])
        ret = array[len(array)-k:]
        a = [val[0] for val in ret]
        return a


# s = Solution()
# array = [1,1,1,2,2,3]
# k = 2
# print(s.topKFrequent(array,k))
        
# @lc code=end

