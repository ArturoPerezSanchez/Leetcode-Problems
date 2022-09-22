# https://leetcode.com/problems/binary-tree-postorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iterativa approach
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        sol = []
        current = root
        d = {}
        while(stack or current):
            if current:
                stack.append(current)
                current = current.left
            else:
                if(stack[-1] in d):
                    sol.append(stack.pop().val)
                else:
                    d[stack[-1]] = True
                    current = stack[-1].right


        return sol

    # Recursive approach
    def postorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        def rec(node, sol=[]):
            if not node: return
            rec(node.left, sol)
            rec(node.right, sol)
            sol.append(node.val)
            return sol
        
        return rec(root)