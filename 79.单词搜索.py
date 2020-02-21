#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
class Solution:
    directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False
        row = len(board)
        col = len(board[0])
        mark = [[0 for _ in range(col)] for _ in range(row)]
        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0]:
                    mark[r][c] = 1
                    if self.backtrack(board,word[1:],r, c,mark):
                        return True
                    else:
                        mark[r][c] = 0
        return False
        
    def backtrack(self, board, word, r, c,mark):
        if not word:
            return True
        for d in self.directs:
            cur_r = r + d[0]
            cur_c = c + d[1]
            if cur_r >= 0 and cur_r < len(board) and cur_c >=0 and cur_c < len(board[0]) and board[cur_r][cur_c]==word[0]:
                ## 已经遍历过，忽略
                if mark[cur_r][cur_c] == 1:
                    continue 
                # 将该元素标记为已使用
                mark[cur_r][cur_c] = 1
                if self.backtrack(board,word[1:],cur_r, cur_c,mark):
                    return True
                else:
                    mark[cur_r][cur_c] = 0
        return False
        
# @lc code=end

