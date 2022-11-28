# https://leetcode.com/problems/n-th-tribonacci-number

class Solution:
    def tribonacci(self, n: int) -> int:
        if(n==0): return 0
        if(n==1): return 1
        if(n==2): return 1
        aux0, aux1, aux2, res = 0, 1, 1, 1
        for i in range(2,n):
            res += aux0 + aux1
            aux0, aux1, aux2 = aux1, aux2, res
        return res