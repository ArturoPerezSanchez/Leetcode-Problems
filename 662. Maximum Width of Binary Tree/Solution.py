# https://leetcode.com/problems/maximum-width-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
		# Create a deque called level, and add root to it with its index as 1
		level = deque([(root, 1)])
		
		# Initialize res to 0
		res = 0
		
		# While level is not empty
		while(level):
			# Create a new deque called newlevel
			newlevel = deque()

			# Update res to the maximum value of res and the difference between the index of the last and first nodes in level, plus one (which is the width of the current level)
			res = max(res, level[-1][1] - level[0][1] + 1)

			# Iterate through the current level
			while level:
				# Remove the leftmost node and its index from level
				current_node, ind = level.popleft()

				# If the left child of the current node exists, add it to newlevel with an index of twice the index of the current node
				if(current_node.left):
					newlevel.append((current_node.left, 2*ind))
				
				# If the right child of the current node exists, add it to newlevel with an index of twice the index of the current node plus one
				if(current_node.right):
					newlevel.append((current_node.right, 2*ind + 1))

			# Replace level with newlevel
			level = newlevel

		# Return the result
		return res