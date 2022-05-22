# https://leetcode.com/problems/backspace-string-compare

class Solution:
    # BruteForce Solution
    def backspaceCompare2(self, s: str, t: str) -> bool:
        i = 0
        while i<(len(s)):
            if(s[i] == "#"):
                if(i== 0):
                    s = s[1:]
                else:
                    s = s[:i-1] + s[i:]
                    s = s[:i-1] + s[i:]
                    i-=1
            else:
                i+=1
        i = 0
        while i<(len(t)):
            if(t[i] == "#"):
                if(i== 0):
                    t = t[1:]
                else:
                    t = t[:i-1] + t[i:]
                    t = t[:i-1] + t[i:]
                    i-=1
            else:
                i+=1
        return s==t
    
    # Using stack
    def backspaceCompare3(self, s: str, t: str) -> bool:
        s2 = []
        t2 = []

        for i in range(max(len(s), len(t))):
            if(i<len(s)):
                if(s[i] == "#"):
                    if(s2): s2.pop()
                else:
                    s2.append(s[i])
            if(i<len(t)):
                if(t[i] == "#"):
                    if(t2): t2.pop()
                else:
                    t2.append(t[i])
        
        t2= "".join(t2)
        s2 = "".join(s2)
        return t2==s2
    
    def backspaceCompare(self, s: str, t: str) -> bool:
        s2, t2 = [], []

        for i in range(len(s)):
            if(s[i] != "#"):
                s2.append(s[i])
            elif(s2): s2.pop()
        for i in range(len(t)):
            if(t[i] != "#"):
                t2.append(t[i])
            elif(t2): t2.pop() 
        return t2==s2









