# https://leetcode.com/problems/minimum-time-to-repair-cars

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        h = [(i, i, 1) for i in ranks]
        heapify(h)

        for i in range(cars-1):
            time, rank, ncars = heappop(h)
            ncars+=1
            heappush(h, (rank*ncars*ncars, rank, ncars))
        return heappop(h)[0]