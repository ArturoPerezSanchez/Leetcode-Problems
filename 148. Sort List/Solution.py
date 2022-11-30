# https://leetcode.com/problems/sort-list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        d = {}
        while(head):
            if(head.val not in d): 
                d[head.val] = [head]
            else:
                d[head.val].append(head)
            aux = head
            head = head.next
            aux.next = None
        
        valList = sorted(d.keys())

        res = d[valList[0]][0]
        
        for i in range(len(valList)-1):
            currentValNodes = d[valList[i]]
            currentNode = currentValNodes[0]
            for j in range(len(currentValNodes)-1):
                currentNode.next = currentValNodes[j+1]
                currentNode = currentNode.next
            currentNode.next = d[valList[i+1]][0]
        
        currentValNodes = d[valList[-1]]
        currentNode = currentValNodes[0]
        for j in range(len(currentValNodes)-1):
            currentNode.next = currentValNodes[j+1]
            currentNode = currentNode.next
        return res
