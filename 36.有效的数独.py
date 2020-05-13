#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for i in range(9)]
        col = [set() for j in range(9)]
        matrix = [set() for z in range(9)]
        ## check row
        for i in range(9):
            for j in range(9):
                pos = (i//3)*3 + j//3 ##注意这个记录方法
                num = board[i][j]
                if num != '.':
                    if num not in row[i] and num not in col[j] and num not in matrix[pos]:
                        row[i].add(num)
                        col[j].add(num)
                        matrix[pos].add(num)
                    else:
                        return False
        return True
            

# @lc code=end

