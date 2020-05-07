#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        def backTrack(i, col, z_diagonal, f_diagonal):
            if i == n:
                return True
            for j in range(n):
                if j not in col and i+j not in z_diagonal and i-j not in f_diagonal:
                   if backTrack(i+1, col | {j}, z_diagonal|{i+j}, f_diagonal|{i-j}):
                       self.res += 1
            return False
        backTrack(0,set(),set(),set())
        return self.res

# @lc code=end

