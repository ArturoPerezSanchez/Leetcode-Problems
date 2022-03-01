# https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        p, c, l = 0, 0, 0
        curr = []
        for i in s:
            if(i == '('): 
                p +=1
                curr.append(i)
            elif(i == "{"): 
                l += 1
                curr.append(i)
            elif(i == "["): 
                c += 1
                curr.append(i)
            elif(i == ")"):
                if(p<1 or curr.pop() != '('): return False
                p-= 1
            elif(i == "}"):
                if(l<1 or curr.pop() != '{'): return False
                l-= 1
            elif(i == "]"):
                if(c<1 or curr.pop() != '['): return False
                c -= 1
                
        if(p == 0 and c == 0 and l == 0): return True
        return False
        