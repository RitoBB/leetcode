#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    ## 简洁版

    ## 第一版
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        while numRows:
            tmp = [1]
            if not res:
                res.append(tmp)
            else:
                n = len(res[-1]) ##上一层的长度，用于遍历
                for i in range(n-1):
                    tmp.append(res[-1][i]+res[-1][i+1])
                tmp.append(1)
                res.append(tmp)
            numRows -= 1
        return res




        
# @lc code=end

