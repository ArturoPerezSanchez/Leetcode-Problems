# https://leetcode.com/problems/find-duplicate-subtrees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        res = []
        d = {}

        def serialize(node, data):
            if not node:
                data.append('#,')
                return
            # preorder serialization
            data.append(str(node.val))
            data.append(',')
            serialize(node.left, data)
            serialize(node.right, data)

        def find(node, d, res):
            if not node:
                return

            find(node.left, d, res)
            find(node.right, d, res)

            data = []
            serialize(node, data)
            data = ''.join(data)

            if d.get(data, 0) == 1:
                res.append(node)

            d[data] = d.get(data, 0) + 1
        
        find(root, d, res)
        return res

