#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
m = d = c = l = x = v = i = 0
thresh_dict = {'I': 1, 'IV':4, 'V': 5, 'IX': 9, 'X': 10, 'XL':40, 'L': 50, 'XC':90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
thresh_list = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
class Solution:
    def intToRoman(self, num: int) -> str:
        factor_breakdown = []
        for thresh in thresh_list:
            curr_thresh = thresh_dict[thresh]
            print(f'Trying for num: {num} | thresh: {curr_thresh}')
            if num >= curr_thresh:
                factor = num//curr_thresh
                factor_breakdown.append(factor)
                remainder = num % curr_thresh
                print(f'returned factor: {factor}, remainder: {remainder}')

                num = remainder
            else:
                factor_breakdown.append(0)
        print(f'resulting factor: {factor_breakdown}')
        ret = ""
        for index, thresh in enumerate(thresh_list):
            ret+=factor_breakdown[index] * thresh
            #print(f'index: {index} thresh: {thresh} result: {factor_breakdown[index] * thresh}')
        return ret
        #print(np.dot(thresh_list, factor_breakdown))
# @lc code=end

