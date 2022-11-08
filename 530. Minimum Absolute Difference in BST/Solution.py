# https://leetcode.com/problems/minimum-absolute-difference-in-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        values_list = []
        while stack:
            current_node = stack.pop()
            values_list.append(current_node.val)
            if(current_node.left): stack.append(current_node.left)
            if(current_node.right): stack.append(current_node.right)
        
        values_list = sorted(values_list)
        result = values_list[1]-values_list[0]
        
        for i in range(2, len(values_list)):
            result = min(result, values_list[i] - values_list[i-1])
        
        return result
        