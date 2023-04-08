#
# @lc app=leetcode id=1020 lang=python3
#
# [1020] Number of Enclaves
#

# @lc code=start
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # h is horizontal , v is vertical
        n = len(grid[0])
        m = len(grid)

        # print(f'height: {h}, width: {w}')

        # This will work by performing DFS for all land values connecting to the boundary

        for i in range(m):
            # print(f'Testing at x: {i}, y:{h-1}')
            self.depth_first_search(grid, i, n-1) # Bottom edge
            self.depth_first_search(grid, i, 0)  # top edge
        for j in range(n):
            self.depth_first_search(grid, m-1, j)  # right most
            self.depth_first_search(grid, 0, j)  # left edge

        # now any 1 left over is an enclave:
        ret = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ret += grid[i][j]
        return ret

    def depth_first_search(self, graph, i, j):
        # First thing, set up our boundaries for x and y:
        if i < 0 or i >= len(graph):
            return
        if j < 0 or j >= len(graph[0]):
            return

        # So now that we know that where we are is in fact valid, we need to check
        # if we are in the ocean or on land, if we are on ocean we can't visit.
        # But we also can't visit if we have already visited. Thus -1 and 0 are return states
        
        if graph[i][j] != 1:
            return
        else:
            # Visit his node as we must be on land:
            graph[i][j] = -1
            # perform DFS on left and right squares
            self.depth_first_search(graph, i-1, j)
            self.depth_first_search(graph, i+1, j)
            self.depth_first_search(graph, i, j-1)
            self.depth_first_search(graph, i, j+1)

# @lc code=end
