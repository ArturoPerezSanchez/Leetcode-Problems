# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        d = defaultdict(list)
        d2 = defaultdict(lambda: float('inf'))
        
        for road in roads:
            d2[road[0]] = min(road[2], d2[road[0]])
            d2[road[1]] = min(road[2], d2[road[1]])

            d[road[0]].append(road[1])
            d[road[1]].append(road[0])
        
        res = d2[1]

        stack = set(d[1])

        visited = {1}

        while(stack):
            origin = stack.pop()
            visited.add(origin)
            tovisit = d[origin]
            res = min(res, d2[origin])
            for i in tovisit:
                if(i not in visited):
                    stack.add(i)
        return res


