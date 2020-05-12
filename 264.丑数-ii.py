#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1 for _ in range(n)]
        l2 = 0
        l3 = 0
        l5 = 0
        for i in range(1,n):
            min_val = min(dp[l2]*2, dp[l3]*3, dp[l5]*5)
            dp[i] = min_val
            # 找出哪个指针对应的数造出了现在这个最小值，将指针前移一位
            ## 有可能同时存在多个最小值，所以不能用elseif 要用if条件语句。
            if dp[l2]*2 == min_val:
                l2 += 1
            if dp[l3]*3 == min_val:
                l3 += 1
            if dp[l5]*5 == min_val:
                l5 += 1
        return dp[-1]


# @lc code=end

