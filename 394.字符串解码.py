#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack, multi, res = [], 0, ''
        for c in s:
            if '0' <= c <= '9':
                multi = multi*10 + int(c)
            elif c == '[':
                stack.append([multi,res])
                multi, res = 0, ''
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            else:
                res += c
        return res

    ##解法二
    def decodeString(self, s: str) -> str:
        def dfs(s,i):
            res, multi = '', 0
            while i < len(s):
                if '0' <= s[i] <= '9':
                    multi = multi*10 + int(s[i])
                elif s[i] == '[':
                    i, tmp = dfs(s,i+1)
                    res += multi * tmp
                    multi = 0
                elif s[i] == ']':
                    return i, res ## 终止递归
                else:
                    res += s[i]
                i += 1
            return res
        return dfs(s,0)
                
# @lc code=end

