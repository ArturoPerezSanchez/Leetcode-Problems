# https://leetcode.com/problems/minimum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        stack = deque([root])
        res = 0
        while stack:
            res +=1
            for i in range(len(stack)):
                currentNode = stack.popleft()
                if not (currentNode.left or currentNode.right): return res
                if (currentNode.left): stack.append(currentNode.left)
                if (currentNode.right): stack.append(currentNode.right)