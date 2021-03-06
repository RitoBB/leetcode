#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        row, col = len(matrix), len(matrix[0])
        i, j = 0, col-1
        while i <row and j >=0:
            if matrix[i][j]>target:
                j-=1
            elif matrix[i][j]<target:
                i+=1
            else:
                return True
        return False

# @lc code=end

