#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len, p_len = len(s), len(p)
        s_idx = p_idx = 0
        star_idx = s_tmp_idx = -1

        while s_idx < s_len:
            ## 1. 当 pattern的字符 = string的字符
            ##     或者 pattern的字符 = ‘？’
            if p_idx < p_len and p[p_idx] in ['?',s[s_idx]]:
                s_idx += 1
                p_idx += 1
            ## 2. 当 pattern的字符 = ‘*’时：
            elif p_idx < p_len and p[p_idx] == '*':
                star_idx = p_idx
                s_tmp_idx = s_idx
                p_idx += 1
            ## 3. 当pattern没有‘*’ 或者 pattern的字符！= string的字符
            elif star_idx == -1:
                return False
            ##4. 当pattern的字符 ！= string的字符 
            ##      或者pattern用完了 并且 pattern曾经有*字符
            else:
                ## 回溯, 当*匹配了一个或多个字符
                p_idx = star_idx +1
                s_idx = s_tmp_idx + 1
                s_tmp_idx = s_idx
            
        return all(x=='*' for x in p[p_idx:])



        # @lc code=end

