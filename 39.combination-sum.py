#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
# from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        def backtrack(currSum, ithValue, currList = []):
            if ithValue >= len(candidates):
                return
            #This function basically will look at next value and 
            #append it to list if the sum is less than or equal to target
            newSum = candidates[ithValue] + currSum

            if newSum <= target:
                currList.append(candidates[ithValue])
                if newSum == target:
                    #we reached the end, append to ret and return
                    ret.append(currList)
                    return
                else:
                    #we have more work to do
                    for ithCandidate in range(ithValue, len(candidates)):
                        backtrack(newSum, ithCandidate, currList[:])
            else:
                # breached target, break out
                return
        for index in range(len(candidates)):
            backtrack(currSum=0, ithValue=index, currList=[])
        return ret
            
# s = Solution()
# print(s.combinationSum([2], 1))     
# @lc code=end

