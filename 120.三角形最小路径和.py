#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ## 自底向上
        ## dp 的长度为最后一行的长度，记录了最短路径和，最后dp[0]就是要反回的最短的路径和。
        ## 注意：该三角形的三边相等。

        row = len(triangle)
        dp = [0] * row
        for i in range(len(triangle[-1])):
            dp[i] = triangle[-1][i]
        for i in range(row-2, -1, -1):
            for j in range(i+1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
        return dp[0]


# @lc code=end

