#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: 
            return 0
        row, col = len(grid), len(grid[0])
        count = 0

        def dfs(i,j):
            grid[i][j]= '0'
            for x, y in [[-1,0],[1,0],[0,-1],[0,1]]:
                tmp_i = i + x
                tmp_j = j + y
                if 0 <= tmp_i< row and 0 <= tmp_j < col and grid[tmp_i][tmp_j]=='1':
                    dfs(tmp_i, tmp_j)
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    dfs(i,j)
                    count += 1
        return count 

    



        



# @lc code=end

