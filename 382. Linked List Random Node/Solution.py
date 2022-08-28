# https://leetcode.com/problems/linked-list-random-node

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution3:
    def __init__(self, head: Optional[ListNode]):
        current = head
        self.vals = []
        while(current):
            self.vals.append(current.val)
            current = current.next

    def getRandom(self) -> int:
        return random.choice(self.vals)


# Constant Space, Linear Time Solution
class Solution2:
    def __init__(self, head: Optional[ListNode]):
        current = head
        self.l = 0
        self.head = head
        while(current):
            current = current.next
            self.l +=1

    def getRandom(self) -> int:
        aux = randint(0, self.l-1)
        current = self.head
        while(aux):
            aux-=1
            current = current.next
        return current.val


# Reservoir Sampling
class Solution:
    
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        
        scope = 1
        res = 0
        current = self.head

        while current:
            if random.random() < 1 / scope: res = current.val
            current = current.next
            scope += 1
        return res
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()