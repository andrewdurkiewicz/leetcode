#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        nlen = len(needle)
        trackIndex = 0 #index to track position in relation to haystack
        index = haystack.find(needle[0]) #look for first char in needle
        trackIndex+=index
        while index != -1 and len(haystack) >= nlen:
            if haystack[index:index+nlen] == needle:
                return trackIndex
            else:
                # Not a match remove front of haystack
                haystack = haystack[index+1:] 
                trackIndex+=1
            index = haystack.find(needle[0])
            trackIndex+=index
        return -1

# @lc code=end

