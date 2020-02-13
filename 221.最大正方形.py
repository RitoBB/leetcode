#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        ## 注意：初始化的时候行列不要搞反了。这里要加一。
        dp = [[0]*(n+1) for _ in range(m+1)]
        res = 0
        ## 以正方形右下脚为dp[i][j]， 对比左边，左上角，正上方是否满足。
        for i in range(1,m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1
                res = max(res, dp[i][j])
        return res*res
# @lc code=end

