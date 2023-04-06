#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        substr = ""
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            # strs has more than one entry 
            print(*strs)
            print(list(zip(*strs)))
            for val in list(zip(*strs)):
                if all(element == val[0] for element in val):
                    substr += val[0]
                else:
                    return substr
            return substr
        

        
        
# @lc code=end

