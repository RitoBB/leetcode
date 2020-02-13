#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_prices = prices[0]
        max_profit = 0
        for i in range(1,len(prices)):
            min_prices = min(min_prices,prices[i])
            max_profit = max(max_profit,prices[i]-min_prices)
        return max_profit

        
# @lc code=end

