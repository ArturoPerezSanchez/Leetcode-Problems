# https://leetcode.com/problems/consecutive-numbers-sum

class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        res = 0
        for i in range(1,int(((1+8*n)**0.5)/2)+1):
            if(i%2): res+=(n/i)%1 == 0
            else: res+=(n/i)%1 == .5
            
            
        
        return res