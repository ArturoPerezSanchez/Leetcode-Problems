# https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        r,l=head,head
        for i in range(n): r=r.next
        if not r: return head.next
        r=r.next
        while r: l,r =l.next,r.next
        l.next=l.next.next
        return head