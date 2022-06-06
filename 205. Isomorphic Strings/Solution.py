# https://leetcode.com/problems/isomorphic-strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1 = {}
        for i in range(len(s)):
            if (s[i] in d1):
                if(d1[s[i]] != t[i]):
                    return False
            else:
                if(t[i] in d1.values()):
                    return False
                d1[s[i]] = t[i]

        return True
