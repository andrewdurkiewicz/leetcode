#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = defaultdict(list)

        for string in strs:
            charcount = [0] * 26
            for char in string:
                charcount[ord(char) - ord('a')]+=1
            ret[tuple(charcount)].append(string)
        return ret.values()
        







s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# @lc code=end

