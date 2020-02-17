#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        cur_layer_node = [root]
        res = []
        flag = True ## 偶数层
        while cur_layer_node:
            cur_layer_val = []
            next_layer_node = []
            flag = not flag
            for node in cur_layer_node:
                cur_layer_val.append(node.val)
                if node.left:
                    next_layer_node.append(node.left)
                if node.right:
                    next_layer_node.append(node.right)
            cur_layer_node = next_layer_node
            if flag:
                res.append(cur_layer_val[::-1])
            else:
                res.append(cur_layer_val)
        return res
            
            

        
# @lc code=end

