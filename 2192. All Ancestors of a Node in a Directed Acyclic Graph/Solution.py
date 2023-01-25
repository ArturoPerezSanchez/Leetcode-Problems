# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        res =  [set() for _ in range(n)]
        indegree=[0]*n
        
        d = {i:[] for i in range(n)}
        for i in edges:
            indegree[i[1]] += 1
            d[i[0]].append(i[1])
    
        stack = []

        for i in range(n):
            if(indegree[i] == 0):
                stack.append(i)

        while stack:
            currentNode = stack.pop()
            for nextNode in d[currentNode]:
                res[nextNode].update(res[currentNode])
                res[nextNode].add(currentNode)
                indegree[nextNode]-=1
                if(indegree[nextNode] == 0):
                    stack.append(nextNode)
        return [sorted(x) for x in res]

