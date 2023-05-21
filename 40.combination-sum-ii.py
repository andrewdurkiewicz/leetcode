#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
# from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ret = []
        print(candidates)
        testSet = set()

        def backtrack(currSum, ithIndex, currList):
            newSum = currSum + candidates[ithIndex]
            if newSum <= target:
                currList.append(candidates[ithIndex])
                if newSum == target:
                    ret.append(currList)
                    return
                else:
                    # more work to do
                    thisSet = set()
                    for nextCandidate in range(ithIndex + 1, len(candidates)):
                        if candidates[nextCandidate] not in thisSet:
                            backtrack(newSum, nextCandidate, currList[:])
                            thisSet.add(candidates[nextCandidate])
            else:
                # over the target, leave
                return

        for index in range(len(candidates)):
            if candidates[index] not in testSet:
                backtrack(currSum=0, ithIndex=index, currList=[])
                testSet.add(candidates[index])
        return ret


# @lc code=end
