#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #create dictionary for comparison
        if len(s1) > len(s2):
            return False
        s1Count = [0] * 26 #26 characters

        for char in s1:
            s1Count[ord(char) - ord('a')]+=1
        
        # Make a window of len(s1)

        def getArray(stringIn):
            tmp = [0] * 26
            for char in stringIn:
                tmp[ord(char) - ord('a')]+=1
            return tmp
        
        lptr = 0
        rptr = lptr + len(s1)

        while rptr <= len(s2):
            if s1Count == getArray(s2[lptr:rptr]):
                return True
            else:
                lptr+=1
                rptr=lptr + len(s1)
        return False


# s = Solution()
# print(s.checkInclusion("adc", "dcda"))
# @lc code=end

