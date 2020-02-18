#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        symbol = {'+','-','*','/'}
        stack = []
        for i in tokens:
            if i in symbol:
                a, b = stack.pop(), stack.pop()
                stack.append(str(int(eval(b+i+a)))) ##注意这里要转为int做完运算操作，再转为str.
            else:
                stack.append(i)
        return stack.pop()
        
# @lc code=end

