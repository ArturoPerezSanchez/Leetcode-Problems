# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head: return None
        current = head
        l = []
        while(current):
            l.append(TreeNode(val=current.val))
            current = current.next
        

        def rec(l1, r1):
            if(r1-l1 == 1): return l[l1]
            mid = (l1+r1)//2
            node = l[mid]
            if(mid>l1): node.left = rec(l1,mid)
            if(mid+1<r1): node.right = rec(mid+1,r1)
            return node
        

        return rec(0, len(l))



