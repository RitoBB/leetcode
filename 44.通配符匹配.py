#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#

# @lc code=start
from functools import lru_cache
class Solution:
    @lru_cache(1800)
    def isMatch(self, s: str, p: str) -> bool:
        lenS = len(s)
        lenP = len(p)
        if '?' not in p and '*' not in p:
            return lenS == lenP and s == p
        if lenS == 0:
            return self.isMatch(s,p[1:]) if p[0] == '*' else False
        if p[0] == '?':
            return self.isMatch(s[1:],p[1:])
        if p[0] == '*':
            return self.isMatch(s,p[1:]) or self.isMatch(s[1:],p)
        return self.isMatch(s[1:],p[1:]) if s[0] == p[0] else False

        
        # @lc code=end


