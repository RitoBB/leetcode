#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 第k个排列
#

# @lc code=start
import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = ''
        num = [str(i) for i in range(1,n+1)]
        ## 找规律
        n -= 1

        while n > -1:
            t = math.factorial(n)
            loc = math.ceil(k/t)-1 ## 要减一，因为loc记录的是index
            res += num[loc]
            num.pop(loc)
            k %= t
            n -= 1
        return res












        # @lc code=end

