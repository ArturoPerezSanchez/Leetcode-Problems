# https://leetcode.com/problems/invert-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Solution 1: Iterative, Using stack
    def invertTree2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.extend([node.left, node.right])
        return root

    # Solution 2: Recursive
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if (not root): return root
        def revert(node):
            node.left, node.right = node.right, node.left
            if(node.left): revert(node.left)
            if(node.right): revert(node.right)
        revert(root)
        return root