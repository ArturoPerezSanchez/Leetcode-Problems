# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer

class Solution(object):
    def subtractProductAndSum(self, n):
        s,p=0,1
        while n>0:
            i=n%10
            s += i
            p *= i
            n = n//10
        return p-s
        
        