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
        n = len(nums)
        def backTrack(idx, tmp):
            if tmp not in res:
                res.append(tmp)
            for i in range(idx, n):
                backTrack(i+1,tmp + [nums[i]])
        backTrack(0, [])
        return res

        
# @lc code=end

