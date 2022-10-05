# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        d = {val:ind for ind, val in enumerate(inorder)} 
        def rec(l, r):
            if l > r: return None
            
            val = postorder.pop()
            node = TreeNode(val)
            ind = d[val]
 
            node.right = rec(ind + 1, r)
            node.left = rec(l, ind - 1)
            return node

        return rec(0, len(inorder) - 1)