#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for leftIndex, leftValue in enumerate(nums): # renamed this to left because this will always be the leftmost pointer in the triplet
            if leftIndex >= len(nums) - 2:
                # Need room for middle and right
                continue
            if leftIndex > 0 and nums[leftIndex] == nums[leftIndex - 1]: 
                #Hit a duplicate Value
                continue 
            middleIndex = leftIndex + 1 # renamed this to mid because this is the pointer that is between the left and right pointers
            rightIndex = len(nums) - 1
            while middleIndex < rightIndex:
                middleValue = nums[middleIndex]
                rightValue = nums[rightIndex]
                sum = leftValue + middleValue + rightValue
                if sum < 0:
                    middleIndex += 1 
                elif sum > 0:
                    rightIndex -= 1
                else:
                    result.append([leftValue, middleValue, rightValue])
                    while middleIndex < rightIndex and nums[middleIndex] == nums[middleIndex + 1]: # Another conditional for not calculating duplicates
                        middleIndex += 1
                    while middleIndex < rightIndex and nums[rightIndex] == nums[rightIndex - 1]: # Avoiding duplicates check
                        rightIndex -= 1
                    middleIndex += 1
                    rightIndex -= 1
        return result

            # @lc code=end
