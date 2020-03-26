#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        above_row, below_row = 0, n-1
        left_col, right_col = 0, n-1
        num = 1
        res = [[0]*n for _ in range(n)]
        while above_row <= below_row and left_col <= right_col:
            for i in range(left_col, right_col+1):
                res[above_row][i] = num
                num += 1
            above_row += 1

            for i in range(above_row,below_row+1):
                res[i][right_col] = num
                num += 1
            right_col -= 1

            for i in range(right_col,left_col-1, -1):
                res[below_row][i] = num
                num += 1
            below_row -= 1

            for i in range(below_row, above_row-1, -1):
                res[i][left_col] = num
                num += 1
            left_col += 1
        return res


# @lc code=end

