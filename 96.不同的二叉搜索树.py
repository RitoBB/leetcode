#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0]*(n+1)
        ## 当1为根节点时，也是一棵树哦！
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(i):
                dp[i] += dp[j]*dp[i-j-1]
        return dp[-1]

        


# @lc code=end

