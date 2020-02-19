#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        ## 方法一： 翻转
        n = len(matrix)
        # Step 1: reverse
        matrix[:] = matrix[::-1]
        # Step 2: diagonal flip
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ## 方法二： 找规律
        n = len(matrix)
        for i in range(n//2):
            for j in range(i, n-i-1):
                matrix[i][j],matrix[j][n-i-1],matrix[n-i-1][n-j-1],matrix[n-j-1][i] =\
                     matrix[n-j-1][i], matrix[i][j],matrix[j][n-i-1],matrix[n-i-1][n-j-1]
        return matrix
        


# @lc code=end

