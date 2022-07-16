# https://leetcode.com/problems/palindrome-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def isPalindrome(self, head):
        rev = None
        slow = head
        fast = head
        # Slow: traverses the list
        # Fast: traverses the list twice as fast
        # Rev: Same as Slow but in each step cheanges the next Node to the previous so at the end its reversed
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        # If fast is not None, the string length is odd, so we skip the middle character
        if fast:
            slow = slow.next
        
        # Comparing rev (wich now contains the first half reversed) with slow (which is in the middle and keeps moving forward)
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        
        # If rev is None we iterated through the whole list, which means is a Palinfrome
        return not rev

    #Brute Force Solution
    def isPalindrome2(self, head: Optional[ListNode]) -> bool:
        a = getLength(head)
        aux = ""
        while head:
            aux+=str(head.val)
            head = head.next
        odd = len(aux)%2
        if(odd):
            return aux[:int(len(aux)/2)] == "".join(reversed(aux[int(len(aux)/2)+1:]))
        else:
            return aux[:int(len(aux)/2)] == "".join(reversed(aux[int(len(aux)/2):]))