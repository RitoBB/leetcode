#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        ## 一天结束时，可能有持股、可能未持股、可能卖出过1次、可能卖出过2次、也可能未卖出过
        ## 所以定义状态转移数组dp[天数][当前是否持股][卖出的次数]
        ## 未持股：1
        n = len(prices)
        dp = [[[0,0,0],[0,0,0]] for i in range(n)]
        #初始化第一天所有可能状态
        ##第一天休息
        dp[0][0][0] = 0
        ##第一天买入股票
        dp[0][1][0] =- prices[0]
        ##第一天不可能已经有卖出
        dp[0][0][1] = float('-inf')
        dp[0][0][2] = float('-inf')
        #第一天不可能已经卖出
        dp[0][1][1]= float('-inf')
        dp[0][1][2] = float('-inf')
        for i in range(1,n):
            #未持股，未卖出过，说明从未进行过买卖
            dp[i][0][0] = 0
            #未持股，卖出过1次，可能是今天卖的，可能是之前卖的
            dp[i][0][1] = max(dp[i-1][1][0]+prices[i],dp[i-1][0][1])
            #未持股，卖出过2次，可能是今天卖的，可能是之前卖的
            dp[i][0][2] = max(dp[i-1][1][1]+prices[i], dp[i-1][0][2])
            #持股，未卖出过，可能是今天买的，可能是之前买的
            dp[i][1][0] = max(dp[i-1][0][0]-prices[i], dp[i-1][1][0])
            #持股，卖出过1次，可能是今天买的，可能是之前买的
            dp[i][1][1] = max(dp[i-1][0][1]-prices[i],dp[i-1][1][1])
            #持股，卖出过2次，可能是今天卖的，可能是之前卖的
            dp[i][1][2] = float('-inf')
        return max(dp[n-1][0][1], dp[n-1][0][2],0)

# @lc code=end

