# https://leetcode.com/problems/can-place-flowers

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if(len(flowerbed) == 1): return True if (n==1 and flowerbed[0] == 0) or n==0 else False
        i = 1
        if(flowerbed[0]== 0 and flowerbed[1] == 0):
            flowerbed[0] = 1
            n-=1
            i=2
        if(flowerbed[-1]== 0 and flowerbed[-2] == 0):
            flowerbed[-1] = 1
            n-=1
        if n <= 0: return True
        
        while(i<len(flowerbed)-1):
            if(not flowerbed[i+1]):
                if(not flowerbed[i]):
                    if(not flowerbed[i-1]):
                        n-=1
                        if n == 0: return True
                        i+=1
                else:
                    i+=1
            else:
                i+=2
            i+=1

        return n == 0