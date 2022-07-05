# https://leetcode.com/problems/fruit-into-baskets

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        f1 = None
        f2 = None
        currentCount = 0
        currentStreak = 0
        ans = 0
        for i in fruits:
            if(f1 is None and i!=f2):
                f1 = i
            elif(f2 is None):
                f2 = i
            if(i == f1):
                f2, f1 = f1, f2
                currentCount+=1
                currentStreak = 1
            elif(i == f2):
                currentCount+=1
                currentStreak +=1
            else:
                f1, f2 = f2, i
                if(currentCount>ans): ans = currentCount
                currentCount = currentStreak+1
                currentStreak = 1
        if(currentCount>ans): ans = currentCount
        return ans
                

