# https://leetcode.com/problems/symmetric-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iterative Approach
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        stack = deque([root.left, root.right])
        while (stack):
            l = stack.popleft()
            r = stack.pop()
            if(not l and not r): continue
            if(not (r and l) or l.val != r.val): return False
            stack.extendleft([l.left,l.right])
            stack.extend([r.right, r.left])
        return True


    # Recursive approach
    def isSymmetric2(self, root: Optional[TreeNode]) -> bool:
        def rec(l, r):
            if(not l and not r): return True
            if(not r or not l or l.val != r.val): return False
            return rec(l.left, r.right) and rec(l.right, r.left)
        
        return rec(root.left, root.right)
            
            





