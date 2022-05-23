# https://leetcode.com/problems/minimum-distance-between-bst-nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        stack = [root]
        values_list = []
        while stack:
            current_node = stack.pop()
            bisect.insort(values_list,current_node.val)
            if(current_node.left): stack.append(current_node.left)
            if(current_node.right): stack.append(current_node.right)

        result = values_list[1]-values_list[0]
        
        for i in range(2, len(values_list)):
            result = min(result, values_list[i] - values_list[i-1])
        
        return result
        