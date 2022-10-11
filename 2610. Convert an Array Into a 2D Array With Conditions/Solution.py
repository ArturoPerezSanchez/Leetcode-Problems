# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:

        d = {}
        nrows = 1
        
        for i in nums:
            d[i] = d.get(i, 0) + 1
            nrows = max(nrows, d[i])

        res = [[] for _ in range(nrows)]

        for i in d:
            currentpos = 0
            for j in range(d[i]):
                res[currentpos].append(i)
                currentpos +=1

        return res
