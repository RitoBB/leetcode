#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        ## claim全局变量
        self.res = float('-inf')

        def findLargest(root):
            if not root:
                return 0
            ## 左边最大值
            left = findLargest(root.left)
            ##找右边最大值
            right = findLargest(root.right)
            ## 更新最大和
            self.res = max(self.res, left+right+root.val)
            ## 对比左右两边较大的值加上根节点值，再和0对比，如果大于0说明这里可以增加最大和。
            return max(0, max(left,right)+root.val)
        
        findLargest(root)
        return self.res      
# @lc code=end

