# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return []
        from collections import deque
        res = []
        stack = deque()
        stack.append(root)
        going_left = True
        
        while stack:
            level = deque()
            for i in range(len(stack)):
                current_node = stack.popleft()
                if(current_node.left): stack.append(current_node.left)
                if(current_node.right): stack.append(current_node.right)
                if(going_left): level.append(current_node.val)
                else: level.appendleft(current_node.val)
                

            going_left = not going_left

            res.append(level)
        return res 