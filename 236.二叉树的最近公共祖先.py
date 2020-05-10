#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ## 从根节点开始遍历树
        if not root:
            return None
        if root ==p or root == q:
            return root
        ## 如果节点p和q都在左子树上，那么以右孩子为节点继续1的操作
        left = self.lowestCommonAncestor(root.left, p, q)
        ## 如果节点p和q都在右子树上，那么以右孩子为节点继续1的操作
        right = self.lowestCommonAncestor(root.right, p,q)
        ## 如果上面两种情况都不满足，说明我们已经找到了他的最近公共祖先。
        if left and right:
            return root
        return left if left else right
        
# @lc code=end

