# https://leetcode.com/problems/maximum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Iterative Solution
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        res = 0
        stack = [[root]]
        while(stack):
            currentLevel = stack.pop()
            nextLevel = []
            for currentNode in currentLevel:
                if(currentNode.left): nextLevel.append(currentNode.left)
                if(currentNode.right): nextLevel.append(currentNode.right)
            if (nextLevel): stack.append(nextLevel)
            res+=1

        return res

    # Recursive solution
    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        global res
        res = 0
        def rec(node, val):
            global res
            if not node: res = max(val, res)
            else:
                val += 1
                rec(node.left, val)
                rec(node.right, val)
        
        rec(root, 0)
        return res