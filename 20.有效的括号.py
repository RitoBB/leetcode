#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        d = ["()","{}","[]"]
        stack = []
        for i in range(len(s)):
            stack.append(s[i])
            if len(stack) >=2 and stack[-2]+stack[-1] in d:
                stack.pop()
                stack.pop()
        return len(stack) == 0
                
        
# @lc code=end

