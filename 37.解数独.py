#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # Step 1: 把所有没填数字的位置找到
        all_points = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    all_points.append([i,j])
        
        def check(point, k):
            row_i = point[0]
            col_j = point[1]
            ##遍历
            for i in range(9):
                ## 检查行
                if i != row_i and board[i][col_j] == k:
                    return False
                ## 检查列
                if i != col_j and board[row_i][i] == k:
                    return False
            ##检查块
            for i in range(row_i//3*3, row_i//3*3+3):
                for j in range(col_j//3*3,col_j//3*3+3):
                    if i!= row_i and j!=col_j and board[i][j] ==k:
                        return False
            return True
            
        def backTrack(i):
            if i == len(all_points):
                return True
            for j in range(1,10):
                if check(all_points[i],str(j)):
                    ## 先试数
                    board[all_points[i][0]][all_points[i][1]] = str(j)
                    ## 成功即true
                    if backTrack(i+1): ##回溯下一个点
                        return True
                    ## 不成功即改回原来的数字
                    board[all_points[i][0]][all_points[i][1]] ='.'
            return False
        backTrack(0)
    
# @lc code=end




