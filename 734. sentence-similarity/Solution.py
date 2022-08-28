# https://leetcode.com/problems/sentence-similarity

class Solution:
    def areSentencesSimilar(self, s1: List[str], s2: List[str], similarPairs: List[List[str]]) -> bool:
        if(len(s1) != len(s2)): return False
        d = {}
        for i in range(len(s1)):
            if(s1[i] not in d): d[s1[i]] = []
            if(s2[i] not in d): d[s2[i]] = []
        for i in similarPairs:
            if(i[0] in d): d[i[0]].append(i[1])
            if(i[1] in d): d[i[1]].append(i[0])
        for i in range(len(s1)):
            if(s1[i] != s2[i] and s2[i] not in d[s1[i]]): return False 
        return True