#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def backTrack(idx, tmp):
            res.append(tmp)
            for i in range(idx, n):
                backTrack(i+1,tmp+[nums[i]])
        backTrack(0, [])
        return res
# @lc code=end

