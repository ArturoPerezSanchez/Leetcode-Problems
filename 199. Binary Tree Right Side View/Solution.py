# https://leetcode.com/problems/binary-tree-right-side-view

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Using dequeue
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if(not root): return res

        q = deque([root])
        while q:
            res.append(q[-1].val)
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res


    # Using List
    def rightSideView2(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if(not root): return res
        
        level = [root]
        while(level):
            res.append(level[-1].val)
            newLevel = []
            for i in level:
                if(i.left is not None): newLevel.append(i.left)
                if(i.right is not None): newLevel.append(i.right)
            level = newLevel
        return res