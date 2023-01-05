# https://leetcode.com/problems/reverse-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        if not head:
            return None
        curr = head.next
        prev.next = None
        if not curr:
            return head
        while(curr.next):
            aux = curr.next
            curr.next = prev
            prev = curr
            curr = aux
        curr.next = prev
        return curr
