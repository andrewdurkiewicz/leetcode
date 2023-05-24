#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def pop(array):
            tmp = array[0]
            del array[0]
            return tmp
        if not root:
            return 0
        maxDepth = 0
        q = [root]
        while q:
            for i in range(len(q)):
                node = pop(q)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            maxDepth+=1
        return maxDepth
# @lc code=end

