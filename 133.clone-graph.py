#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        def genGraph(refNode: 'Node', orgNode:'Node'):
            #given some node, check if neighbors are already there
            for neighbor in orgNode.neighbors:
                if neighbor.val in nodeDict.keys():
                    refNode.neighbors.append(nodeDict[neighbor.val])
                else:
                    #node doesn't exist. create and add
                    newNode = Node(neighbor.val)
                    nodeDict[neighbor.val] = newNode
                    refNode.neighbors.append(nodeDict[neighbor.val])
                    genGraph(nodeDict[neighbor.val], neighbor)

        nodeDict = {}
        newRoot = Node(node.val)
        genGraph(newRoot, node)
        for neighbor in newRoot.neighbors:
            print(neighbor.val)
        return newRoot


        
# @lc code=end

