# https://leetcode.com/problems/balanced-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        global ans
        
        ans= True
        
        def rec(node):
            global ans

            l = 1+rec(node.left) if node.left else 0
            r = 1+rec(node.right) if node.right else 0

            if(l-r < -1 or l-r>1):
                ans = False
                return 0
            return max(l,r)
        
        rec(root)
        return ans