#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        longest = 0
        output = 0
        for index, char in enumerate(s):
            if char not in seen.keys():
                output = max(output,index-longest+1)
            else:
                # Found a previously seen character 
                if seen[char] < longest:
                    output = max(output,index-longest+1)
                else:
                    longest = seen[char] + 1
            seen[char] = index
        return output
# @lc code=end

