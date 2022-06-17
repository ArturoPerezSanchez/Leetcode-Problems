# https://leetcode.com/problems/naming-a-company

class Solution:

    # Using hashmap
    def distinctNames(self, ideas: List[str]) -> int:
        d = {}
        res = 0
        for i in ideas:
            if i[0] not in d:  d[i[0]] = set()
            d[i[0]].add(i[1:])

        keys = list(d.keys())
        for i in range(len(keys)):
            for j in range(i+1, len(keys)):
                setA = d[keys[i]]
                setB = d[keys[j]]
                same = len(setA & setB)
                res += (len(setA) - same) * (len(setB) - same)
        return res*2

    # Brute Force approach
    def distinctNames2(self, ideas: List[str]) -> int:
        res = 0
        for i in range(len(ideas)):
            for j in range(i, len(ideas)):
                newName = ideas[j][0] + ideas[i][1:]
                newName2 = ideas[i][0] + ideas[j][1:]
                if (newName not in ideas and newName2 not in ideas):
                    res +=2
        return res