# https://leetcode.com/problems/cousins-in-binary-tree-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # If the root is empty, return it as is
        if not root: 
            return root

        # Create an empty stack
        stack = []
        
        # Set the value of the root node to 0
        root.val = 0
        
        # Calculate the sum of the sibling nodes
        sibling_sum = 0 if not root.left else root.left.val + 0 if not root.right else root.right.val 
        
        # If the left child exists, append it and the sibling sum to the stack
        if root.left: 
            stack.append((root.left, sibling_sum))
        
        # If the right child exists, append it and the sibling sum to the stack
        if root.right: 
            stack.append((root.right, sibling_sum))
        
        # Set the sum of all cousins to the sibling sum
        allcousins = sibling_sum
        
        # While the stack is not empty
        while stack:
            
            # Create a new empty stack
            newstack = []
            
            # Set the sum of all cousins to 0
            newAllCousins = 0
            
            # While the current stack is not empty
            while stack:
                
                # Pop the current node and its sibling sum from the stack
                current_node, s = stack.pop()
                
                # Set the sibling sum to 0
                sibling_sum = 0
                
                # If the left child exists, add its value to the sibling sum
                if current_node.left: 
                    sibling_sum += current_node.left.val
                    
                # If the right child exists, add its value to the sibling sum 
                if current_node.right: 
                    sibling_sum += current_node.right.val 
                    
                # Add the sibling sum to the sum of all cousins
                newAllCousins += sibling_sum
                
                # Set the value of the current node to the sum of all cousins minus the sibling sum
                current_node.val = allcousins - s
                
                # If the left child exists, append it and the sibling sum to the new stack
                if current_node.left: 
                    newstack.append((current_node.left, sibling_sum))
                    
                # If the right child exists, append it and the sibling sum to the new stack
                if current_node.right: 
                    newstack.append((current_node.right, sibling_sum))
                
            # Set the sum of all cousins to the new sum of all cousins
            allcousins = newAllCousins
            
            # Set the stack to the new stack
            stack = newstack
        
        # Return the root node
        return root
