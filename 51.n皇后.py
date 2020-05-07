#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ## Step 1: 根据给定的n初始化解法
        res = []
        s = '.' * n
        ## Step 2: 回溯函数
        ## 每一行，列，正对角，负对角 不能有2个以上的Q出现
        def backTrack(i, tmp, col, z_diagonal, f_diagonal):
            if i == n:
                res.append(tmp)
                return
            for j in range(n):
                if j not in col and i+j not in z_diagonal and i-j not in f_diagonal:
                    backTrack(i+1, tmp+[s[:j]+'Q'+s[j+1:]], col|{j}, z_diagonal|{i+j},f_diagonal|{i-j})

        backTrack(0,[], set(),set(),set())
        return res




# @lc code=end

