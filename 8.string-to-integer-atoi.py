#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        bounds = [-1*2**31, 2**(31) - 1]
        s = s.strip(" ") #Read in and ignore any leading whitespace
        sign = 1
        if len(s) == 0:
            return 0
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s= s[1:]
        
        processString = ""
        for char in s:
            if char.isnumeric():
                processString+=char
            else:
                break

        if processString == "":
            return 0
        tmp = sign*int(processString)
        if tmp >= bounds[1]:
            return bounds[1]
        elif tmp <= bounds[0]:
            return bounds[0]
        return tmp
        
# a = Solution()
# tmp = a.myAtoi(" -9 8")
# print(tmp)      
# @lc code=end

