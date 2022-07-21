# https://leetcode.com/problems/count-good-nodes-in-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode, biggest=-inf) -> int:
        if(biggest>root.val): res=0
        else:
            res=1
            biggest = root.val
        if(root.left): res+=self.goodNodes(root.left, biggest)
        if(root.right): res+=self.goodNodes(root.right, biggest)
        return res