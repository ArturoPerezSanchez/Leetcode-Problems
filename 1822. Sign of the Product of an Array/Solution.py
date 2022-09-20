# https://leetcode.com/problems/sign-of-the-product-of-an-array

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = 1
        for i in nums:
            if(i==0): return 0
            if(i<0): res*=-1
        return res

    # Brute force solution
    def arraySign2(self, nums: List[int]) -> int:
        def signFunc(x):
                if(x==0): return 0
                if(x>0): 
                    return 1
                return -1
            
        prod = 1
        for i in nums:
            print(i)
            prod = prod*i
        
        return signFunc(prod)