# https://leetcode.com/problems/merge-k-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def getmin(values):
            min_val = None
            min_index = None
            for i in range(len(values)):
                if values[i] != None and (min_val== None or values[i]<min_val):
                    min_val = values[i]
                    min_index = i
            return min_index
        
        values = [ i.val if(i) else None for i in lists]
        min_index = getmin(values)
        if (min_index is None): return None
        head = lists[min_index]
        cur = head

        while(True):
            #Update lists
            lists[min_index] = lists[min_index].next
            #Update values
            values[min_index] = lists[min_index].val if lists[min_index] else None
            min_index = getmin(values)
            if(min_index is None): return head
            cur.next = lists[min_index]
            cur = cur.next

    # Unfair solution using a list with all nodes
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        values = []

        for i in lists:
            cur = i
            while(cur is not None):
                nodes.append(cur)
                values.append(cur.val)
                cur = cur.next

        res = [x for _, x in sorted(zip(values, nodes), key=lambda pair: pair[0])]
        
        if(not res): return None
        head = res[0]
        cur = head

        for i in res[1:]:
            cur.next = i
            cur = cur.next
        return head




        