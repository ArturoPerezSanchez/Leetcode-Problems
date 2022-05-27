# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time complexity: O(max(m,n)) where m and n are the lengths of the input linked lists.
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:  
        # create a new linked list to store the result
        res = ListNode(0)
        # create a tail pointer to keep track of the last node in the result list
        res_tail = res
        # initialize the carry to False
        carry = False
        
        # loop until we have processed all the nodes in both linked lists and there is no carry left
        while(l1 != None or l2 != None or carry):
            
            # calculate the sum of the current nodes and the carry (if any)
            carry, val = divmod((l1.val if l1 else 0)+(l2.val if l2 else 0) + carry, 10) 
            
            # create a new node with the calculated value and add it to the result list
            res_tail.next = ListNode(val)            
            # update the tail pointer to the newly added node
            res_tail = res_tail.next
            
            # move to the next nodes in the input linked lists
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
            
        # return the next node of the head of the result list
        return res.next
