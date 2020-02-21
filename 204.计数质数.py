#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [1]*n
        res = 0
        for i in range(2,n):
            if isPrime[i] == 1:
                res += 1
            j = i
            while i*j < n:
                isPrime[i*j] = 0
                j += 1
        return res
# @lc code=end

