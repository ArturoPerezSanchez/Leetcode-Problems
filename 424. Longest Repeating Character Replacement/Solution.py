# https://leetcode.com/problems/longest-repeating-character-replacement

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        d = {}

        for i in range(len(s)):
            d[s[i]] = d.get(s[i],0) + 1
            subslen = i-l+1
            if(k< subslen-max(d.values())):
                d[s[l]] -=1
                l+=1
            else:
                res = max(res, subslen)
            
        
        return res
                    
                    

                
