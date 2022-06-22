class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        res = ''
        while(i<len(s) and s[i] == ' '):
            i+=1
        if(i<len(s)):
            if(s[i] == '-'):
                res = '-'
                i+=1
            elif(s[i] == '+'):
                i+=1

        while(i<len(s) and s[i].isdigit()):
            res+=s[i]
            i+=1
        if(len(res) == 0 or res=='-'): return 0
        res = int(res)

        return max(-2**31, min(2**31-1, res))