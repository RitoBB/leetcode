#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        ## 方法一： 中序遍历
        res = []
        self.inOrder(root,res)
        for i in range(1,len(res)):
            if res[i]<=res[i-1]:
                return False
        return True

    def inOrder(self,root,res):
        if root:
            self.inOrder(root.left,res)
            res.append(root.val)
            self.inOrder(root.right, res)
        return res
## 方法二：递归
    def isValidBST(self, root: TreeNode) -> bool:
        def isBST(root, min_val, max_val):
            if root == None:
                return True
            if min_val >= root.val or max_val <= root.val:
                return False
            return isBST(root.left, min_val, root.val) and isBST(root.right,root.val,max_val)
        return isBST(root,float('-inf'),float('inf'))

        
        
# @lc code=end

