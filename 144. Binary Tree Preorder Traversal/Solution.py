# https://leetcode.com/problems/binary-tree-preorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        current = root
        stack = []
        res = []
        while (current or stack):
            if (not current): current = stack.pop()
            if(current.right): stack.append(current.right)
            res.append(current.val)
            current = current.left
        return res
