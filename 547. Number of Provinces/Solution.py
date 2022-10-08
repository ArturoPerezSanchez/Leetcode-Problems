# https://leetcode.com/problems/number-of-provinces

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        d = defaultdict(list)
        tovisit = set([i for i in range(len(isConnected))])

        for r in range(len(isConnected)):
            for c in range(r):
                if(isConnected[r][c]):
                    d[r].append(c)
                    d[c].append(r)
        
        provinces = 0
        visited = set()
        while(tovisit):
            for city in tovisit: break
            inprovince = [city]
            while(inprovince):
                city = inprovince.pop()
                if city in tovisit:
                    tovisit.remove(city)
                    visited.add(city)
                    inprovince.extend(d[city])
            provinces +=1


        return provinces

        