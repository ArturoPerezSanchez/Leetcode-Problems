# https://leetcode.com/problems/permutation-in-string

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = {}
        if(len(s1)>len(s2)): return False
        for i in s1:
            d1[i] = d1.get(i, 0) + 1
        
        d2 = d1.copy()
        counter = 0
        i = 0

        while(i<len(s2)):
            if(counter == len(s1)): return True
            if(s2[i] not in d2):
                d2=d1.copy()
                counter = 0
            elif(d2[s2[i]] == 0):
                aux = i
                i-= counter
                while(d2[s2[aux]] == 0 and i<aux and counter>0):
                    d2[s2[i]] +=1
                    i+=1
                    counter -= 1
                i=aux
                d2[s2[i]] -=1
                counter+=1
            else:
                d2[s2[i]] -=1
                counter+=1
            i+=1

        if(counter == len(s1)): return True
        return False
