#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache=[[0 for _ in range(n)] for _ in range(m)]
        cache[-1][-1] = 1
        def getPaths(i, j):
            #for a given location on the matrix with i,j coord
            # this returns the number of paths
            sum = 0
            if j+1 < n:
                sum+=cache[i][j+1]
            if i+1 < m:
                sum+=cache[i+1][j]
            cache[i][j] += sum
        for y in range(m-1,-1,-1):
            for x in range(n-1, -1,-1):
                getPaths(y,x)
        return cache[0][0]

# s = Solution()
# a = s.uniquePaths(3,2)
# print(a)     
        
# @lc code=end

