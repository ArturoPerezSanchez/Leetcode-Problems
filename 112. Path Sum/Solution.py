# https://leetcode.com/problems/path-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        def rec(node, target):
            if(not(node.left or node.right)): return target == node.val
            return node.right and rec(node.right, target-node.val) or node.left and rec(node.left, target-node.val)
        return rec(root, targetSum)