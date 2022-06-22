# https://leetcode.com/problems/binary-search

class Solution:

    def search(self, s: List[int], t: int) -> int:
        l = 0
        r = len(s)
        while(l<r):
            mid = (l+r)//2
            if(s[mid] > t): r = mid
            elif(s[mid] < t): l=mid+1
            else: return mid
        
        return -1

    # def search(self, s: List[int], t: int) -> int:
    #     l=len(s)
    #     p=int(l/2)

    #     while(l>1):
    #         if s[p] == t:
    #             return p 
    #         l = int((l+1)/2)
    #         if(s[p]>t):
    #             p = max(0,p-l)
    #         else:
    #             p=min(len(s)-1,p+l)
    #     if s[p] == t:
    #         return p
    #     return -1