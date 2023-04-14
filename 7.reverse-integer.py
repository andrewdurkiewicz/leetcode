#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        # get the sign of the integer
        sign = (x > 0) - (x < 0) #returns the sign of the value
        val = int(str(sign*x)[::-1]) #sign * x to force negative to be positive
        return sign*val * (val < 2**31) #sign * x reintroduces the negative if there is one

        
# @lc code=end

