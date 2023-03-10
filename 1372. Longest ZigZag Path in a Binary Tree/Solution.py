# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # Define a global variable to store the result.
        global res
        res = 0

        # This is a recursive function that traverses the binary tree in a zigzag manner and computes the score.
        # 'node' is the current node, 'direction' is the direction of traversal (either 'left' or 'right'), and 'score' is the current score.
        def rec(node, direction, score):
            # Base case: If the node is None, Update the global variable 'res' with the maximum score.
            if (not node):
                global res
                if(score > res):
                    res = score
                return

            # Recursive case: Traverse the right and left sub-trees in adding 1 to score if it keeps the zigzag or setting it to 0 otherwise
            rec(node.right, "left", score + 1 if direction == "right" else 0)
            rec(node.left, "right",  score + 1 if direction == "left" else 0)

        # Call the 'rec' function twice to cover both the left and right directions.
        rec(root, "right", -1)
        rec(root, "left", -1)
        
        # Return the result.
        return res
