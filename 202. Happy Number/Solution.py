# https://leetcode.com/problems/happy-number

class Solution:
    def isHappy(self, n: int) -> bool:
        d= set()
        s = sum([int(x)**2 for x in str(n)])
        while(s!=1 and (s not in d)):
            d.add(s)
            s = sum([int(x)**2 for x in str(s)])
        if(s==1): return True
        return False