#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, str: str) -> int:
        import re
        ## 规则
        re_str = '\s*[-|+]?\d+'
        ## 匹配
        result = re.match(re_str,str)
        try:
            result = int(result[0].strip(' '))
        except:
             return 0
        else:
            return max(min(result, 2**31-1),-2**31)
# @lc code=end

