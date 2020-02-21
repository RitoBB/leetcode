#
# @lc app=leetcode.cn id=326 lang=python3
#
# [326] 3的幂
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        ## 递归法
        if n == 0:
            return False
        while True:
            if n%3 == 0:
                n//=3
            elif n == 1:
                return True
            else:
                return False

    def isPowerOfThree(self, n: int) -> bool:
        import math
        return n >0 and 3**(round(math.log(n,3))) == n
# @lc code=end

