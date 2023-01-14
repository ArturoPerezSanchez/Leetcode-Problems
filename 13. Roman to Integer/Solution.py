# https://leetcode.com/problems/roman-to-integer

class Solution:
    def romanToInt(self, s: str) -> int:
        res=0
        t=len(s)
        for i in range(t):
            if(s[i]=='M'):res+=1000
            elif(s[i]=='D'):res+=500
            elif(s[i]=='L'):res+=50
            elif(s[i]=='V'):res+=5
            elif(s[i]=='C'):
                if(i+1<t and (s[i+1]=='M'or s[i+1]=='D')):res-=200
                res+=100
            elif(s[i]=='X'):
                if(i+1<t and(s[i+1]=='L'or s[i+1]=='C')):res-=20
                res+=10
            elif(s[i]=='I'):
                if(i+1<t and(s[i+1]=='V'or s[i+1]=='X')):res-=2
                res+=1
            i+=1
        return res