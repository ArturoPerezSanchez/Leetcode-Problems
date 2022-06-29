# https://leetcode.com/problems/sum-of-prefix-scores-of-strings

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        d = {}
        res = []

        for word in words:
            for i in range(1,len(word)+1):
                suf = word[:i]
                d[suf] = d.get(suf, 0)+1

        for word in words:
            aux = 0
            for i in range(1,len(word)+1):
                suf = word[:i]
                aux+=d[suf]
            res.append(aux)
        
        return res