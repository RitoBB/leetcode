#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        # 为了照顾到 0 把左边界设置为 0
         # 为了照顾到 1 把右边界设置为 x // 2 + 1
        left, right = 0, x//2 + 1
        while left < right:
            # 注意：这里一定取右中位数，如果取左中位数，代码可能会进入死循环
            mid = (left+right+1) >> 1
            square = mid*mid
            if square > x:
                right = mid-1
            else:
                left = mid 
        # 因为一定存在，因此无需后处理
        return left


# @lc code=end

