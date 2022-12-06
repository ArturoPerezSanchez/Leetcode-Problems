# https://leetcode.com/problems/length-of-last-word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # counter = 0
        # for i in reversed(s.strip()):
        #     if(i!= " "):
        #         counter +=1
        #     else:return counter
        # return counter
        
        
        # counter = 0
        # aux=False
        # for i in range(len(s)-1, -1, -1):
        #     if(s[i]!= " "):
        #         aux=True
        #         counter +=1
        #     elif(aux):
        #         return counter
        # return counter
        s = s.strip()[::-1] + " "
        
        return s.index(" ")