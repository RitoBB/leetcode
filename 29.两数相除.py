#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = 0
        sign = 1 if dividend^divisor >=0 else -1
        divd = abs(dividend)
        divor = abs(divisor)
        while divd>= divor:
            tmp, i = divor, 1
            while divd >= tmp:
                res += 1
                divd -= tmp
                i <<= 1
                tmp <<= 1
        res = res*sign
        return min(max(-2**31, res),2**31-1)
# @lc code=end

