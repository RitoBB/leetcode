#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n <=1:
            return 0
        res = 0
        dp = [0]*n
        for i in range(1,n):
            if s[i] == ')':
                if s[i-1]=='(':
                    dp[i] = dp[i-2]+2
                ## 当为‘））‘的情况，dp[i-1]代表左边‘）’的有效括号长度，
                ##所以用i-dp[i-1]-1为右边‘）’的对应有效括号位置。
                if s[i-1]==')' and i-dp[i-1]-1>=0 and s[i-dp[i-1]-1]=='(':
                    ## dp[i-1]代表之前的最长长度，dp[i-dp[i-1]-2]+2代表这个括号的最长长度。
                    dp[i] = dp[i-1]+ dp[i-dp[i-1]-2]+2  
            res = max(res, dp[i])
        return res




# @lc code=end

