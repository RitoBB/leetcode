#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ##特殊情况
        n = len(prices)
        if n <=1:
            return 0
        if n == 2:
            count=prices[1]-prices[0]
            return count if count >0 else 0

        ## 定义状态
        having = [0]*n
        not_having = [0]*n

        ## 定义初始化状态
        having[0] = -prices[0]
        having[1] = max(having[0], not_having[0]-prices[1])
        not_having[1] = max(not_having[0], having[0]+prices[1])

        ## 状态转移方程
        for i in range(2,n):
            having[i] = max(having[i-1], not_having[i-2]-prices[i]) ##注意not_having[i-2]为了满足冷冻期
            not_having[i] = max(not_having[i-1], having[i-1]+prices[i])

        return max(having[-1], not_having[-1])






# @lc code=end

