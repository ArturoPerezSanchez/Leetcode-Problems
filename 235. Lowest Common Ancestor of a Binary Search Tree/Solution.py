# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        def rec(node,q,p):
            global res
            if(not node): return False

            l = rec(node.left,q,p)
            r = rec(node.right,q,p)
            cur = node == q or node == p
            if (cur and l) or (l and r) or (cur and r):
                self.ans = node
                return
            return l or r or cur
        rec(root, p,q)
        return self.ans
