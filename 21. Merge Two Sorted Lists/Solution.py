# https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        resHead = res
        while (True):
            if(list1 == None):
                res.next = list2
                break
            elif(list2 == None):
                res.next = list1
                break
            else:
                if(list1.val < list2.val):
                    res.next = list1
                    list1 = list1.next
                else:
                    res.next = list2
                    list2 = list2.next
                res = res.next

        return resHead.next