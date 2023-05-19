#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
# from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2 #round down

        if len(B) < len(A):
            A, B = B, A
        
        #set the left and right pointer
        lptr, rptr = 0, len(A) - 1

        while True:
            A_part = (lptr + rptr) // 2 
            B_part = half - A_part - 2 # subtract 2 to solve for index
            Aleft =  A[A_part] if A_part >= 0 else float("-infinity")
            Aright = A[A_part + 1] if (A_part + 1) < len(A) else float("infinity")
            Bleft = B[B_part] if B_part >= 0 else float("-infinity")
            Bright = B[B_part + 1] if (B_part + 1) < len(B) else float("infinity")
            if Aleft <= Bright and Aright >= Bleft:
                if total % 2 == 0:
                    # Even
                    max_left = max(Aleft, Bleft) 
                    min_right = min(Aright, Bright)
                    return (max_left + min_right) / 2
                else:
                    return min(Aright, Bright)
            
            if Aright < Bleft:
                #need to move L pointer over by one
                lptr = A_part + 1
            if Aleft > Bright:
                rptr = A_part - 1
                

# s = Solution()
# a = s.findMedianSortedArrays([1,3], [2])
# print(a)
# @lc code=end

