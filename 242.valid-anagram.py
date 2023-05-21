#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sHash = {}
        for char in s:
            if char not in sHash.keys():
                #Add to it
                sHash[char] = 1
            else:
                sHash[char] += 1
        for char in t:
            if char not in sHash.keys():
                #found char that isn't in keys, return false
                return False
            else:
                sHash[char]-=1
                if sHash[char] == 0:
                    del sHash[char]
        if len(sHash.keys()) > 0:
            return False
        else:
            return True
        
# s = Solution()
# print(s.isAnagram("rat", "car"))
# @lc code=end

