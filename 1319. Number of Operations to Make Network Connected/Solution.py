# https://leetcode.com/problems/number-of-operations-to-make-network-connected

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if (len(connections) < n-1): return -1
        d = {i:[] for i in range(n)}

        for i, j in connections:
            d[i].append(j)
            d[j].append(i)
        
        visited = [False]*n
        res = -1

        for i in range(n):
            stack = deque()
            if(not visited[i]):
                stack.append(i)
                visited[i] = True
                res +=1
            while(stack):
                current_node = stack.pop()
                for child in d[current_node]:
                    if(not visited[child]):
                        visited[child] = True
                        stack.append(child)
        return res