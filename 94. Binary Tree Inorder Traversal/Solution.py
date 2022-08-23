# https://leetcode.com/problems/binary-tree-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Recursive Solution
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if(not root): return []
        def rec(node, res):
            if node.left:
                rec(node.left, res)
            res.append(node.val)
            if node.right:
                rec(node.right, res)
            return res
        res = rec(root, [])
        return res
