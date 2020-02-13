#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(num,index):
            res.append(num)
            for i in range(index, len(nums)):
                backtrack(num+[nums[i]],i+1)
        backtrack([],0)
        return res
# @lc code=end

