# https://leetcode.com/problems/license-key-formatting

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        res = ""
        rem = k
        for i in range(len(s)-1, -1, -1):
            if(s[i] == "-"): continue
            res += s[i].upper()
            rem-=1
            if(rem<=0):
                rem = k
                res += "-"
        if(len(res)>1 and res[-1] == "-"): return res[:-1][::-1]
        return res[::-1]