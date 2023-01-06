# https://leetcode.com/problems/swap-nodes-in-pairs

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if(not head): return None
        if(not head.next): return head
        if(not head.next.next):
            res = head.next
            res.next = head
            head.next = None
            return res
        if(not head.next.next.next):
            res = head.next
            aux = res.next
            res.next = head
            head.next = aux
            return res
        
        current = head
        head2 = head.next
        
        while (current.next and current.next.next and current.next.next.next):
            aux =  current.next.next
            current.next.next = current
            current.next = aux.next
            current = aux
        
        if(not current.next): return head2
        res = current.next
        aux = res.next
        res.next = current
        current.next = aux
        return head2
        