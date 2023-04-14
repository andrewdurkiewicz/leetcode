#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = None
        deltaBest = None
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
                diff = abs(sum - target) # diff from our target
                if result is None:
                    result = sum
                    deltaBest = diff
                else:
                    if diff < deltaBest:
                        result = sum
                        deltaBest = diff
                if sum > target:
                    #greater than what we want, move right over
                    rightIndex-=1
                elif sum < target:
                    # less than what we want, move middle to right 
                    middleIndex+=1
                else: 
                    return sum
        return result
        
# @lc code=end

