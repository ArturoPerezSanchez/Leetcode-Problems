# https://leetcode.com/problems/validate-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        global output
        output = True
        def rec(node, low, high):
            global output
            if not node: return
            if not (low < node.val < high):
                output = False
                return output
            rec(node.left, low, node.val)
            rec(node.right, node.val, high)
        
        rec(root, -inf, inf)
        return output