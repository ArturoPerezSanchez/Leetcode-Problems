# https://leetcode.com/problems/n-ary-tree-postorder-traversal

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def rec(node, sol=[]):
            if not node: return
            for child in node.children:
                rec(child, sol)

            sol.append(node.val)
            return sol
        
        return rec(root)