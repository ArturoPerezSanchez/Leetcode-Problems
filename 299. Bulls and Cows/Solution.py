# https://leetcode.com/problems/bulls-and-cows

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        d = {}
        for i in range(len(secret)):
            if(secret[i] == guess[i]):
                bulls +=1
            d[secret[i]] = d.get(secret[i],0)+1
        
        for i in range(len(guess)):
            if d.get(guess[i],0) > 0:
                d[guess[i]]-=1
                cows +=1
        return str(bulls) + "A" + str(cows-bulls) + "B"
        
