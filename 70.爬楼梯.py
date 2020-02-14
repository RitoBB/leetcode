#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        res = [1,2]
        if n ==1 or n ==2:
            return n
        while len(res)<n:
            res.append(res[-1]+res[-2])
        return res[-1] 
# @lc code=end

