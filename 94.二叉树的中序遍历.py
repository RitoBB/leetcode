#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        return self.inOrder(root,res)
    def inOrder(self,root,res):
        if not root:
            return []
        self.inOrder(root.left,res)
        res.append(root.val)
        self.inOrder(root.right,res)
        return res

         
        
# @lc code=end

