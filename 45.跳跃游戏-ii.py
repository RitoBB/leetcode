#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        step = 0
        max_bound = 0 ##能到达的最远边界
        end = 0 ##上一步到达的边界
        for i in range(len(nums)-1):
            max_bound = max(max_bound, nums[i]+i)
            if i == end:
                step += 1
                end=max_bound
        return step

# @lc code=end

