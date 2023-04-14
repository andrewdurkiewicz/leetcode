#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def printZigZag(self, matrix):
        str = ""
        for i in matrix:
            for j in i:
                if j != '-':
                    str+=j
        return str

    def convert(self, s: str, numRows: int) -> str:
        ret = []
        if numRows > 1:
            for i in range(numRows):
                ret.append((-(len(s)//-2))*['-'])
            horizontal = 0
            vertical = 0
            zigzag = False
            for char in s:
                if vertical == 0:
                    zigzag = False

                ret[vertical][horizontal] = char
                
                if vertical+1 >= numRows or zigzag:
                    zigzag = True
                    vertical-=1
                    horizontal+=1
                
                else:
                    zigzag = False
                    vertical+=1
        else:
            ret = [char for char in s]
        out = self.printZigZag(ret)
        return out


            


        
# @lc code=end
# s = "AB"
# rows = 1
# val = Solution()
# val.convert(s=s, numRows=rows)
