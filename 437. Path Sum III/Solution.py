# https://leetcode.com/problems/path-sum-iii

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        global res
        res = 0

        def rec(node, path):
            if not node: return
            global res

            path.append(0)

            for i in range(len(path)):
                path[i] += node.val
                if(path[i] == targetSum):
                    res+=1
            
            rec(node.left, path.copy())
            rec(node.right, path.copy())
        
        rec(root, [])
        return res
            

