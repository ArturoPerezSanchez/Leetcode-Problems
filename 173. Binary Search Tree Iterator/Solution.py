# https://leetcode.com/problems/binary-search-tree-iterator

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):

        def rec(node):
            aux = []
            if not node: return aux

            if(node.left):
                aux += rec(node.left)
            aux += [node.val]
            if(node.right):
                aux += rec(node.right)
            return aux

        self.l = rec(root)
        self.p = 0


    def next(self) -> int:
        self.p +=1
        return self.l[self.p-1]
        
        

    def hasNext(self) -> bool:
        return self.p < len(self.l)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()