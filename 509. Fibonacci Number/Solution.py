# https://leetcode.com/problems/fibonacci-number

class Solution:
    def fib(self, n: int) -> int:
        if(n==0): return 0
        if(n==1): return 1
        aux0, aux1, res = 0, 1, 1
        for i in range(1,n):
            res += aux0
            aux0, aux1 = aux1, res
        return res
