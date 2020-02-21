#
# @lc app=leetcode.cn id=289 lang=python3
#
# [289] 生命游戏
#

# @lc code=start
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i, j in itertools.product(range(m), range(n)):
            t = 0
            for r, c in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                x, y = i + r, j + c
                if 0 <= x < m and 0 <= y < n:
                    t += board[x][y] % 2
            if board[i][j] and t not in {2, 3} or not board[i][j] and t == 3:
                board[i][j] += 2
        for i, j in itertools.product(range(m), range(n)):
            if board[i][j] > 1:
                board[i][j] = 1 - board[i][j] % 2




# @lc code=end

