#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        ## 第一个位置
        dp[0][0] = 1 if obstacleGrid[0][0]!=1 else 0
        if dp[0][0]==0:
            return 0
        ## 第一行：
        for i in range(1, n):
            if obstacleGrid[0][i]!=1:
                dp[0][i] = dp[0][i-1]
        ## 第一列
        for i in range(1,m):
            if obstacleGrid[i][0]!=1:
                dp[i][0] = dp[i-1][0]
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]!=1:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]

        
# @lc code=end

