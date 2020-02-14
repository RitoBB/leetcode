#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: 
            return 0
        row = len(matrix)
        col = len(matrix[0])
        ## 用left_j记录第i行为底, 第j列左边第一个小于height_j[j]的位置
        left_j = [-1] * col
        ## 用right_j记录第i行为底, 第j列右边第一个小于height_j[j]的位置
        right_j = [col] * col
        ## 用height_j记录第i行为底,第j列高度是多少.
        height_j = [0] * col
        res = 0
        for i in range(row):
            cur_left = -1
            cur_right = col
            for j in range(col):
                if matrix[i][j] == "1":
                    height_j[j] += 1
                else:
                    height_j[j] = 0
            for j in range(col):
                if matrix[i][j] == "1":
                    left_j[j] = max(left_j[j], cur_left)
                else:
                    left_j[j] = -1
                    cur_left = j
            for j in range(col - 1, -1, -1):
                if matrix[i][j] == "1":
                    right_j[j] = min(right_j[j], cur_right)
                else:
                    right_j[j] = col
                    cur_right = j
            for j in range(col):
                res = max(res, (right_j[j] - left_j[j] - 1) * height_j[j])
        return res

# @lc code=end

