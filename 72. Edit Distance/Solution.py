# https://leetcode.com/problems/edit-distance

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        d = {}
        
        def rec(origin, index):
            if(origin in d): return d[origin]
            while(index<len(origin) and index<len(word2) and origin[index] == word2[index]): index+=1
            if(index>=len(origin) or index>=len(word2)): 
                res = abs(len(origin)-len(word2))
                d[origin] = res
                return res

            # Adding word2[index] in origin[index]
            adding = rec(origin[:index] + word2[index] + origin[index:], index)
            
            # Replacing origin[index] with word2[index]
            replacing = rec(origin[:index] + word2[index] + origin[index+1:], index) 

            # Deleting origin[index]
            deleting = rec(origin[:index] + origin[index+1:], index)


            res = min(adding, deleting, replacing)

            d[origin] = res+1
            return res+1
        
        return rec(word1, 0)
