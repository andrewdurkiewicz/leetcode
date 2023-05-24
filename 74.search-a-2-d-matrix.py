#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(nums: List[int], target: int) -> int:
            lptr, rptr = 0, len(nums)-1

            while lptr <= rptr:
                middleIndex = (lptr+rptr) // 2
                if nums[middleIndex] > target:
                    rptr = middleIndex - 1
                elif nums[middleIndex] < target:
                    lptr = middleIndex + 1
                else:
                    #must be equal
                    return True
            return False
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        if not (top <= bot):
            return False
        
        new_matrix = matrix[(top + bot)//2]
        return search(new_matrix, target)
# @lc code=end

