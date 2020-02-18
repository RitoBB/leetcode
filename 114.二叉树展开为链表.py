#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
     ## 思路一：前序遍历，再设置箭头指向
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        d = []
        def preorder(root):
            if not root:
                return 
            d.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        i =1
        root.left = None
        p = root ## 设置p来重新构造链表。
        while i < len(d):
            p.right = TreeNode(d[i]) ##注意这里TreeNode
            p = p.right
            i += 1
        return p


    
    ##思路二： 递归
    def flatten(self, root: TreeNode) -> None:
        def helper(root,pre):
            if not root:
                return pre
            pre = helper(root.right,pre)
            pre = helper(root.left, pre)
            root.right = pre
            root.left = None
            return root
        return helper(root,None)
               
# @lc code=end

