#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ## step 1: 定义状态
        ## dp[i]：表示以 nums[i] 结尾的连续子数组的最大和。
        dp = [0]*len(nums)
        ## step 2: 初始状态
        dp[0] = nums[0]
        ## step 3: 状态转移方程
        for i in range(1,len(nums)):
             dp[i] = max(dp[i - 1] + nums[i], nums[i]) 
        return max(dp)

        


        
# @lc code=end

