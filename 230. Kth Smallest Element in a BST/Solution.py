# https://leetcode.com/problems/kth-smallest-element-in-a-bst

# Definition for a binary tree node.
# class Treenode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [TreeNode(val=None, right=root)]
        while True:
            current_node = stack.pop()
            k -= 1
            if k == -1: return current_node.val
            if(current_node.right):
                stack.append(current_node.right)
                current_node = current_node.right
                while current_node.left:
                    stack.append(current_node.left)
                    current_node = current_node.left


