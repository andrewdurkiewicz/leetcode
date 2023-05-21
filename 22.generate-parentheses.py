#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
# from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        def backTrack(currStr, numL, numR):
            if numR > numL:
                return
            if numL > n:
                return
            if len(currStr) == 2*n:
                #We have hit the end
                if (numL == n) and (numR == n):
                    ret.append(currStr)
            else:
                backTrack(currStr + "(", numL+1, numR)
                backTrack(currStr + ")", numL, numR+1)
        backTrack("", 0, 0)

        return ret
                

# s = Solution()
# print(s.generateParenthesis(3))
# @lc code=end

