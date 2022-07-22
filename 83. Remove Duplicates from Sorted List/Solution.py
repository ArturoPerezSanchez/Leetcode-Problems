# https://leetcode.com/problems/remove-duplicates-from-sorted-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        if(head): current = head.next
        else: current = None
        while (current):
            if(prev.val != current.val):
                prev.next = current
                prev = current
            current = current.next
        if(prev): prev.next = None
        return head
    # def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     prev = head
    #     if(head): current = head.next
    #     else: current = None
    #     while (current):
    #         while(prev.val == current.val):
    #             current = current.next
    #             if(not current):
    #                 prev.next = current
    #                 return head
    #         prev.next = current
    #         prev = current
    #         current = current.next
    #     return head