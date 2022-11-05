# https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        
        for i in strs:
            a = "".join(sorted(i))
            if (a in d):
                d[a].append(i)
            else:
                d[a] = [i]
        res = []
        for i in d.keys():
            res.append(d[i])
        
        return res