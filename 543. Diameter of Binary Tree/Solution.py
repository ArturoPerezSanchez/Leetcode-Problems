# https://leetcode.com/problems/diameter-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        def height(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            left_height = height(root.left)
            right_height = height(root.right)
            self.diameter = max(self.diameter, left_height + right_height)
            return 1 + max(left_height, right_height)
        
        height(root)
        return self.diameter

    def diameterOfBinaryTree2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        
        left_diameter = self.diameterOfBinaryTree(root.left)
        right_diameter = self.diameterOfBinaryTree(root.right)
        
        return max(left_height + right_height, max(left_diameter, right_diameter))
    
    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))