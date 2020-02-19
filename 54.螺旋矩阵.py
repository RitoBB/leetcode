#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            if not matrix:
                break
            matrix = self.turnMatrix(matrix)
        return res
    
    def turnMatrix(self,matrix):
        newmat = []
        row = len(matrix)
        col = len(matrix[0])
        for c in range(col-1,-1,-1):
            tmp_mat = []
            for r in range(row):
                tmp_mat.append(matrix[r][c])
            newmat.append(tmp_mat)
        return newmat
            



        
        
# @lc code=end

