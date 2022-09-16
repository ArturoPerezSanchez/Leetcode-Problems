# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero

class Solution:

    def sumZero(self, n: int) -> List[int]:

        if n%2: res = [0]
        else: res = []
        for i in range(1, n//2+1):
            res.append(i)
            res.append(-i)
        return res

    def sumZero2(self, n: int) -> List[int]:
        if(n%2): return list(range(n//2 +1)) + list(range(-1, -n//2, -1))
        return list(range(1, n//2 +1)) + list(range(-1, -n//2-1, -1))