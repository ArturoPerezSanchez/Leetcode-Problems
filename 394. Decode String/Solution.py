# https://leetcode.com/problems/decode-string

class Solution:
    def decodeString(self, s: str) -> str:
        @cache
        def rec (text):
            res = ""
            i=0
            while i < (len(text)):
                if text[i] == "[":
                    aux = i-1
                    digit = ""
                    while text[aux].isdigit():
                        digit = text[aux] + digit
                        aux -=1
                    depth = 0
                    for j in range(i,len(text)):
                        if(text[j] == "["): depth+=1
                        if(text[j] == "]"): depth-=1
                        if(depth==0):
                            res += int(digit)*rec(text[i:j])
                            i=j-1
                            break
                else:
                    if(text[i] != "]" and not text[i].isdigit()):
                        res += text[i]
                i+=1      
            return res

        return rec(s)
        
                