#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
import copy


class Solution:
    def generate_board(self, n):
        tmp = []
        row = ""
        for index in range(n):
            row = n*'.'
            tmp.append(list(row))
        return tmp

    def solveNQueens(self, n: int) -> List[List[str]]:
        # put queen in top left
        test = []
        for value in range(n):
            newgraph = self.generate_board(n)
            self.searchpaths(newgraph, value, 0, test)
        return test

    def gen_graph(self, graph):
        ret = []
        for row in graph:
            tmp = ""
            for char in row:
                if char == 'q':
                    tmp += 'Q'
                else:
                    tmp += '.'
            ret.append(tmp)
        return ret

    def findpossible(self, graph, i, j):
        # move left from i, j
        # i is the starting point on x axis
        tmpy = copy.copy(j) - 1
        while tmpy >= 0:
            graph[tmpy][i] = 'Q'
            tmpy -= 1

        tmpy = copy.copy(j) + 1
        while tmpy < len(graph[0]):
            graph[tmpy][i] = 'Q'
            tmpy += 1

        tmpx = copy.copy(i) - 1
        while tmpx >= 0:
            graph[j][tmpx] = 'Q'
            tmpx -= 1

        tmpx = copy.copy(i) + 1
        while tmpx < len(graph):
            graph[j][tmpx] = 'Q'
            tmpx += 1

        tmpx = copy.copy(i) + 1
        tmpy = copy.copy(j) + 1
        while tmpx < len(graph) and tmpy < len(graph):
            graph[tmpy][tmpx] = 'Q'
            tmpx += 1
            tmpy += 1

        tmpx = copy.copy(i) - 1
        tmpy = copy.copy(j) - 1
        while tmpx >= 0 and tmpy >= 0:
            graph[tmpy][tmpx] = 'Q'
            tmpx -= 1
            tmpy -= 1
        tmpx = copy.copy(i) + 1
        tmpy = copy.copy(j) - 1
        while tmpy >= 0 and tmpx < len(graph):
            graph[tmpy][tmpx] = 'Q'
            tmpx += 1
            tmpy -= 1
        tmpx = copy.copy(i) - 1
        tmpy = copy.copy(j) + 1
        while tmpx >= 0 and tmpy < len(graph):
            graph[tmpy][tmpx] = 'Q'
            tmpy += 1
            tmpx -= 1

    def testSoln(self, graph, ret):
        count = 0
        for column in graph:
            count += column.count('q')
        if count == len(graph):
            ret.append(self.gen_graph(graph))

    def searchpaths(self, graph, x, y, ret):
        # A queen can go up, down, left, right, diag
        graph[y][x] = 'q'
        self.findpossible(graph, x, y)
        # look to next column for any possible positions:
        if y < len(graph)-1:
            for idx, value in enumerate(graph[y+1]):
                if value == '.':
                    # located empty location next line over,
                    tmp = copy.deepcopy(graph)
                    self.searchpaths(tmp, idx, y+1, ret)
        # Hit end
        else:
            self.testSoln(graph, ret)


# @lc code=end
