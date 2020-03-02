#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur_str = ''

        def dfs(cur_str, left, right):
            if left ==0 and right == 0:
                res.append(cur_str)
            if left > right:
                return 
            if left > 0 :
                dfs(cur_str + '(', left - 1, right)
            if right > 0 :
                dfs(cur_str + ')', left, right - 1)
        dfs(cur_str,n,n)
        return res


# @lc code=end

