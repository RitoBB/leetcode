#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        n = str(n)
        visited = set()
        while 1:
            n = str(sum(int(i)**2 for i in n))
            if n == '1':
                return True
            if n in visited:
                return False
            visited.add(n)
        
# @lc code=end

