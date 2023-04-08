#
# @lc app=leetcode id=2086 lang=python3
#
# [2086] Minimum Number of Food Buckets to Feed the Hamsters
#

# @lc code=start
class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        if "HHH" in hamsters:
            # Middle Hampster is stuck, unable to eat
            return -1
        if hamsters[:2] == 'HH' or hamsters[-2:] == 'HH':
            # Edge hampsters unable to feed
            return -1
        if hamsters.count('.') == 0:
            return -1
        hamsters = list(hamsters)
        #first we look at the edges. If, H look to adjacent cell for place for food. 
        # if a place exists, replace the . with a + to indicate food is there.
        # from there on out we look with a size 3 window for a food 
        # 
        if hamsters[0] == 'H':
            hamsters[1] = '+'
        if hamsters[-1] == 'H':
            hamsters[-2] ='+'
        for i in range(1, len(hamsters)):
            if hamsters[i] == 'H':
                #found a hampster, are we fed?
                if hamsters[i-1] == '+' or hamsters[i+1] == '+':
                    continue
                else:
                    #Need to feed. prioritize to the right.
                    if hamsters[i+1] == '.':
                        hamsters[i+1] = '+'
                    elif hamsters[i-1] == '.':
                        hamsters[i-1] = '+'
                    else:
                        print("error")

        return hamsters.count('+')
        
        
# @lc code=end

