# https://leetcode.com/problems/check-completeness-of-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:

        stack = deque([root])
        end = False
        while(stack):
            current_node = stack.popleft()
            if(current_node.left and current_node.right):
                if(end): return False
                stack.extend([current_node.left, current_node.right])
            elif(current_node.left and not current_node.right):
                if(end): return False
                end = True
                stack.append(current_node.left)
            elif(not current_node.left and current_node.right):
                return False
            else:
                end = True
        return True