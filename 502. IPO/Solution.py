# https://leetcode.com/problems/ipo

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capital, profits = zip(*sorted(zip(capital,profits)))
        pointer = 0
        h = []

        for _ in range(k):
            while(pointer<len(capital) and capital[pointer]<=w):
                heapq.heappush(h, -profits[pointer])
                pointer+=1
            if (not h): return w
            w -= heapq.heappop(h)
        return w