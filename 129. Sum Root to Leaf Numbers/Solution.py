# https://leetcode.com/problems/sum-root-to-leaf-numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        global res
        res = 0
        if not root: return res

        def rec(node, num):
            num = num*10 + node.val
            if not node.left and not node.right:
                global res
                res += num
            else:
                if(node.left): rec(node.left, num)
                if(node.right): rec(node.right, num)
        
        rec(root, 0)
        return res

