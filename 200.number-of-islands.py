#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def search(i, j):
            if i > 0:
                if grid[i-1][j] == "1":
                    #look left
                    grid[i-1][j] = "0"
                    search(i-1, j)
            if i < len(grid) - 1:
                if grid[i+1][j] == "1":
                    #look right
                    grid[i+1][j] = "0"
                    search(i+1, j)
            if j > 0:
                if grid[i][j-1] == "1":
                    #look down
                    grid[i][j-1] = "0"
                    search(i,j-1)
            if j < len(grid[0]) - 1:
                if grid[i][j+1] == "1":
                    grid[i][j+1] = "0"
                    search(i,j+1)
        found = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == "1":
                    grid[row][column] = "0"
                    found+=1
                    search(row,column)
        return found

# s=Solution()
# grid = [["0","1","0"],["1","0","1"],["0","1","0"]]

# print(s.numIslands(grid))
# @lc code=end

