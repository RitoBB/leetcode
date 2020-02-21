#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'IV': -1, 'V': 5, 'IX': -1,
             'X': 10, 'XL': -10, 'L': 50, 'XC': -10,
             'C': 100, 'CD': -100, 'D': 500, 'CM': -100,
             'M': 1000}
        thesum = 0
        for i in range(len(s)):
            if s[i:i+2] in d:
                thesum += d[s[i:i+2]]
            else:
                thesum += d[s[i]]
        return thesum

    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
        isjump = thesum = 0
        for i in range(len(s)):
            ## 判断是否是遍历过的小大组合中的数。
            if isjump == s[i]:
                continue
            twoliteral = s[i:i+2]
            ## 判断是不是小大组合
            if twoliteral in d:
                thesum += d[twoliteral]
                isjump = twoliteral[-1]
            else: ## 只有大
                thesum += d[twoliteral[0]]
        return thesum


# @lc code=end

