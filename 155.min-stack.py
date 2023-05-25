#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:


    class stackValue:
        def __init__(self, value):
            self.value = value
            self.currMin = None

    def __init__(self):
        self.array = []


    def push(self, val: int) -> None:
        #is this value less than our currMin? 
        #First entry
        if len(self.array) == 0:
            newEntry = self.stackValue(val)
            newEntry.currMin = val
        else:
            #more than one entry
            newEntry = self.stackValue(val)
            currentMin = self.array[-1].currMin
            if val < currentMin:
                #replace the min
                newEntry.currMin = val
            else:
                #maintain current min
                newEntry.currMin = currentMin
        self.array = self.array + [newEntry]

    def pop(self) -> None:
        del self.array[-1]

    def top(self) -> int:
        return self.array[-1].value
        

    def getMin(self) -> int:
        return self.array[-1].currMin
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

