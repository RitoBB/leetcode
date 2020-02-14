#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [0]*len(nums)
        dp[0] = 1
        for i in range(1,len(nums)):
            tmp = 0
            for j in range(i):
                if nums[j]<nums[i] and tmp <dp[j]:
                    tmp = dp[j]
            dp[i] = tmp +1
        return max(dp)
        
# @lc code=end

