#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ## 递归，先遍历右子树再遍历中间再左子树。
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.total = 0
        return self.depthFirstSearch(root)

    def depthFirstSearch(self, root):
        if not root:
            return None
        self.depthFirstSearch(root.right)
        self.total += root.val
        root.val = self.total
        self.depthFirstSearch(root.left)
        return root

        
            
# @lc code=end

