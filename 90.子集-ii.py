#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(num, index):
            if num not in res:
                res.append(num)
            for i in range(index, len(nums)):
                backtrack(num+[nums[i]], i+1)
        backtrack([],0)
        return res

        
# @lc code=end

