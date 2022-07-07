# https://leetcode.com/problems/longest-palindrome

class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        #d =  {e:s.count(e) for e in set(s)}
        d = Counter(s)
        aux = False
        res = 0

        for i in d.values():
            if(i%2):
                aux = True
                res+=i-1
            else:
                res+=i
        return res + aux
