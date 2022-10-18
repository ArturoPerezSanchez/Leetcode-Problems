# https://leetcode.com/problems/minimize-deviation-in-array

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = set()
        mi = inf
        for i in nums:
            if(i%2): i *= 2
            heap.add(-i)
            mi = min(i, mi)
        heap = list(heap)
        heapify(heap)
        ma = -heap[0]
        res = ma - mi
        while heap[0] % 2 == 0:
            newval = heappop(heap) // 2
            heappush(heap, newval)
            ma, mi = -heap[0], min(mi, -newval)
            res = min(res, ma - mi)
        return res
               


