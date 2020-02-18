#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """

        def preorder(root, res):
            if root is None:
                res += 'null'
            else:
                res += str(root.val)+','
                res = preorder(root.left,res)
                res = preorder(root.right,res)
            return res
        return preorder(root,'')
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def buildtree(vals):
            if not vals: 
                return None
            # val = vals.pop()
            if vals[0] == 'None':
                vals.pop(0)
                return None
            
            root = TreeNode(vals[0])
            vals.pop(0)
            root.left = buildtree(vals)
            root.right = buildtree(vals)
            return root
        return buildtree(data.split(','))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

