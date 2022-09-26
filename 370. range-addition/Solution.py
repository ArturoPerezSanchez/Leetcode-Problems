# https://leetcode.com/problems/range-addition

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:

        arr = [0]*(length+1)

        for i in updates:
            arr[i[0]] += i[2]
            arr[i[1]+1] -= i[2]

        currentSum = 0

        for i in range(length):
            currentSum += arr[i]
            arr[i] = currentSum
        arr.pop()
        return arr