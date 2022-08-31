# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)

        prev = dummy
        current = head

        while (current and current.next):
            if(current.val != current.next.val):
                prev.next = current
                prev = current
            else:
                while(current.next and current.next.val == current.val):
                    current = current.next
            current = current.next
        if(current): prev.next = current
        else: prev.next = None
        return dummy.next
