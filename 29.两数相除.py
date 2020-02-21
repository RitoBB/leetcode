#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = 0
        sign =  1 if dividend ^ divisor >= 0 else -1
        #print(sign)
        divd = abs(dividend)
        dior = abs(divisor)
        while divd >= dior:
            tmp, i = dior, 1
            while divd >= tmp:
                divd -= tmp
                res += i
                i <<= 1
                tmp <<= 1
        res = res * sign 
        return min(max(-2**31, res), 2**31-1)

        # @lc code=end

