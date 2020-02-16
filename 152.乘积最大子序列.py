#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子序列
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = nums[0]
        pre_max = nums[0]
        pre_min = nums[0]
        for i in range(1, len(nums)):
            cur_max = max( pre_max * nums[i], pre_min * nums[i], nums[i])
            cur_min = min( pre_min * nums[i], pre_max * nums[i], nums[i])
            res = max( cur_max, res)
            pre_max = cur_max
            pre_min = cur_min
        return res

# @lc code=end

