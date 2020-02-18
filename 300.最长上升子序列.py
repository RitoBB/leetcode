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
                ## 注意限制条件tmp<dp[j],
                # 如果tmp>dp[j]说明dp[j]之前还有更长的上升子序列，就不用管他，继续遍历。
                ##如果没有，就更新为dp[j]
                if nums[j]<nums[i] and tmp <dp[j]:
                    tmp = dp[j]
            dp[i] = tmp +1
        return max(dp)
        
# @lc code=end

