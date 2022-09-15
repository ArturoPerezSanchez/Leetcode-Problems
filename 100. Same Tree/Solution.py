# https://leetcode.com/problems/same-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res = True
        stack1 = [p]
        stack2 = [q]
        while(stack1 and stack2):
            n1 = stack1.pop()
            n2 = stack2.pop()
            if(n1 and n2):
                if(n1.val != n2.val):
                    res = False
                    break
                stack1.append(n1.left)
                stack2.append(n2.left)
                stack1.append(n1.right)
                stack2.append(n2.right)
            elif(n1 or n2):
                res = False
                break
        return res