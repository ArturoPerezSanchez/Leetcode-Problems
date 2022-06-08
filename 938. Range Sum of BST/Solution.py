# https://leetcode.com/problems/range-sum-of-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]
        res = 0

        while(stack):
            current_node = stack.pop()
            if(current_node.val >=low and current_node.val <= high):
                res += current_node.val
                if(current_node.left): stack.append(current_node.left)
                if(current_node.right): stack.append(current_node.right)
            else:
                if(current_node.val >=low and current_node.left): stack.append(current_node.left)
                elif(current_node.val <= high and current_node.right): stack.append(current_node.right)

        return res