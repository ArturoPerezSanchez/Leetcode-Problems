# https://leetcode.com/problems/n-ary-tree-preorder-traversal

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    global res
    def rec(self, node):
        global res
        res.append(node.val)
        for i in node.children:
            self.rec(i)
    def preorder(self, root: 'Node') -> List[int]:
        global res
        res = []
        if not root: return None
        self.rec(root)
        return res


