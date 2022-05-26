# https://leetcode.com/problems/shortest-path-with-alternating-colors

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        redHM = {}
        blueHM = {}

        for i in redEdges:
            if (i[0] not in redHM):
                redHM[i[0]] = [(i[1], "r")]
            else:
                redHM[i[0]].append((i[1], "r"))
        
        for i in blueEdges:
            if (i[0] not in blueHM):
                blueHM[i[0]] = [(i[1], "b")]
            else:
                blueHM[i[0]].append((i[1], "b"))


        visited = {}
        ans = [-1]*n
        counter = 0
        stack = deque()
        stack.extend([(0, "r"), (0, "b")])
        while(stack):
            for i in range(len(stack)):
                currentNode, currentColor = stack.popleft()
                if((currentNode, currentColor) not in visited):
                    visited[(currentNode, currentColor)] = True
                    if(ans[currentNode] == -1): ans[currentNode] = counter
                    if(currentColor == "r"):
                        stack.extend(blueHM.get(currentNode, []))
                    else:
                        stack.extend(redHM.get(currentNode, []))
            counter +=1
        return ans

