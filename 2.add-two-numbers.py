#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        returnNode = None
        while True:
            if l1 is not None or l2 is not None:
                if returnNode is None:
                    # Create first return Node:
                    returnNode = ListNode()
                    first = returnNode
                else:
                    # Have a return Node already, add to it
                    if returnNode.next is None:
                        # Need another node, one hasn't been made yet
                        returnNode.next = ListNode()
                    returnNode = returnNode.next
                # created the next return node, add to it
                addVal = returnNode.val
                if l1 is None:
                    addVal += l2.val
                    l2 = l2.next
                elif l2 is None:
                    addVal += l1.val
                    l1 = l1.next
                else:
                    addVal += l1.val + l2.val
                    l1 = l1.next
                    l2 = l2.next

                if addVal >= 10:
                    remainder = addVal % 10
                    returnNode.val = remainder
                    returnNode.next = ListNode(val = 1)
                else:
                    returnNode.val = addVal
            else:
                return first

            

# @lc code=end

