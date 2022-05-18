# https://leetcode.com/problems/clone-binary-tree-with-random-pointer

# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        if not root: return None
        d = {None:None}
        stack = [root]
        res = None
        while stack:
            current_node = stack.pop()
            d[current_node] = NodeCopy(current_node.val)
            if(current_node.left): stack.append(current_node.left)
            if(current_node.right): stack.append(current_node.right)

        for cur in d.keys():
            if cur is None: continue
            if not res: res = d[cur]
            d[cur].left = d[cur.left]
            d[cur].right = d[cur.right]
            d[cur].random = d[cur.random]
        return res