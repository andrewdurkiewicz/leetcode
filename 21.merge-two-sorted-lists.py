#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ret = ListNode()
        head = ret
        finished = False
        while ((list1 is not None) or (list2 is not None)) and not finished:
            if list1 is None:
                ret.next = list2
                finished = True
            elif list2 is None:
                ret.next = list1
                finished = True
            elif list1.val <= list2.val:
                ret.next = ListNode(val = list1.val)
                ret = ret.next
                list1 = list1.next
            else:
                ret.next = ListNode(val = list2.val)
                ret = ret.next
                list2 = list2.next

        return head.next
        
# @lc code=end

