# https://leetcode.com/problems/unique-paths

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        @cache
        def recursive(m, n):
            if(m==1): return 1
            if(n==1): return 1
            return recursive(m-1, n) + (recursive(m,n-1))
        
        return recursive(m,n)
