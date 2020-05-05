#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    ## Method 1
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.dfs(res,n,n,'')
        return res

    def dfs(self, res, left, right, path):
        if left == 0 and right == 0:
            res.append(path)
            return 
        if left >0:
            self.dfs(res,left-1, right, path+'(')
        if left < right:
            self.dfs(res,left,right-1, path+")")
# @lc code=end

## Method 2
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = ""
        
        def dfs(left,right,path):
            if left == 0 and right == 0:
                res.append(path)
            if left > right:
                return 
            if left >0:
                dfs(left-1, right, path+'(')
            if right >0 :
                dfs(left, right-1, path+")")
        
        dfs(n,n,path)
        return res