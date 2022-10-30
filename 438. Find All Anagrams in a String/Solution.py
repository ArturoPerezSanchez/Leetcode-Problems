# https://leetcode.com/problems/find-all-anagrams-in-a-string

class Solution:
   def findAnagrams(self, s: str, p: str) -> List[int]:
        hm = {}
        res = []
        
        if len(p) > len(s): return []

        # build hashmap
        for ch in p: hm[ch] = hm.get(ch,0) + 1

        # initial full pass over the window
        for i in range(len(p)):
            if s[i] in hm: hm[s[i]] -= 1
            
        # slide the window with stride 1
        for i in range(len(s) - len(p)):
            # check whether we encountered an anagram
            if all(v == 0 for v in hm.values()): res.append(i)

            if s[i] in hm: hm[s[i]] += 1
            if s[len(p) + i] in hm: hm[s[len(p) + i]] -= 1
        
        if all(v == 0 for v in hm.values()): 
            res.append(len(s) - len(p))

                
        return res