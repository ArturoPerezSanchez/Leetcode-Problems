# https://leetcode.com/problems/last-stone-weight

class Solution:
    # 0(Nlog(n)) Sorting and inserting
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones) # O(log(N))
        while(len(stones)>1): # O(N)
            newStone = stones.pop()-stones.pop() # O(1)
            if(newStone != 0): bisect.insort(stones, newStone) #O(log(N))
        
        if(stones): return stones[0]
        return 0
    
    # O(Nlog(N)) Using heap
    def lastStoneWeight2(self, stones: List[int]) -> int:
        stones = [-x for x in stones] # O(N)
        heapq.heapify(stones) # O(N)
        while(len(stones)>1): # O(N)
            newStone = heapq.heappop(stones) - heapq.heappop(stones) # O(2*log(N)) = O(log(N))
            if(newStone != 0): heapq.heappush(stones,newStone) # O(log(N))
        
        if(stones): return -stones[0]
        return 0
        


