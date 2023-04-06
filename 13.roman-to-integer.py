#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
convert = {"I":1,"V":5,"X":10,"L":50,\
           "C":100,"D":500,"M":1000}
class Solution:
    def romanToInt(self, s: str) -> int:
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        total = 0
        for val in s:
            total+=convert[val]
        return total

        
# @lc code=end

