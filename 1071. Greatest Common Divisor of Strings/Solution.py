# https://leetcode.com/problems/greatest-common-divisor-of-strings

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        count = 0
        for i in range(min(len(str1), len(str2))):
            if str1[i] == str2[i]:
                count+=1
            else: break

        while(True):
            while(count>0 and (len(str1)%count != 0 or len(str1)%count != 0)):
                count-=1
            if (count == 0): return ""
            subs = str1[0:count]
            
            if(subs*int(len(str1)/count) == str1 and subs*int(len(str2)/count) == str2):
                return subs
            count-=1

        
