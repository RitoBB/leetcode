#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(num,middle):
            if not num:
                res.append(middle)
                return 

            for i in range(len(num)):
                backtrack(num[:i]+num[i+1:], middle+[num[i]])
        backtrack(nums, [])
        return res
            
        
# @lc code=end

