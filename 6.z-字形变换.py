#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <2:
            return s
        ## 设置一个flag, 
        flag = -1
        i = 0
        res = ["" for _ in range(numRows)]
        for c in s:
            res[i] += c
            if i == 0 or i == numRows-1: ## 当i到达开头或者结尾的时候，利用flag转向。
                flag = -flag
            i += flag
        return "".join(res)


# @lc code=end

