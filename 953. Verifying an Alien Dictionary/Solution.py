# https://leetcode.com/problems/verifying-an-alien-dictionary

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            for j in range(len(word1)):
                if(j>=len(word2)): return False
                c1 = order.index(word1[j])
                c2 = order.index(word2[j])
                if(c1 > c2): return False
                if(c1 < c2): break
        return True
