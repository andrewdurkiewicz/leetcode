#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
import queue
open_list = ['{', '(', '[']
get_open = {'}':'{', ')':'(', ']':'['}

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 != 0:
            return False
        else:
            for char in s:
                if char in open_list:
                    stack.append(char)
                else:
                    #received a close bracket. if stack is empty, this fails
                    if (len(stack) == 0):
                        return False
                    if get_open[char] == stack[-1]:
                        stack.pop() #remove
                    else:
                        # Got a closure element for wrong match
                        return False
            if len(stack) > 0:
                return False
            return True
        
# @lc code=end

