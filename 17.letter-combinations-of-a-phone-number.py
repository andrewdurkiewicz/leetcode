#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
digit_dict = {
    2 : ["a", "b", "c"],
    3 : ["d", "e", "f"],
    4 : ["g", "h", "i"],
    5 : ["j", "k", "l"],
    6 : ["m", "n", "o"],
    7 : ["p", "q", "r", "s"],
    8 : ["t", "u", "v"],
    9 : ["w", "x", "y", "z"]
}

# from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        curr = [""]
        for digit in digits:
            asInt = int(digit)
            Options = digit_dict[asInt]
            tmp = curr
            curr = []
            for val in tmp:
                for addthis in Options:
                    curr.append(val+addthis)
        return curr

                
# s = Solution() 
# print(s.letterCombinations(""))
# @lc code=end

