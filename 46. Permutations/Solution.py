# https://leetcode.com/problems/permutations

class Solution:    
    def permute(self, nums: List[int]) -> List[List[int]]:
        global res
        res = []
        def rec(f, n):
            if(len(n) == 1):
                res.append(f + n)
            for i in range(len(n)):
                f.append(n[i])
                rec (f,n[:i] + n[i+1:])
                f.pop()
        rec([], nums)
        return res
