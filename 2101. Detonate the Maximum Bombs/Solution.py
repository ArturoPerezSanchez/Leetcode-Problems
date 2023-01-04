# https://leetcode.com/problems/detonate-the-maximum-bombs

class Solution:
    # Solution 1: storing the direct detonations in a hashmap
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def detonates(bomb1, bomb2):
            x1, y1, r = bomb1
            x2, y2, _ = bomb2
            return math.dist([x1, y1], [x2,y2])<=r

        nExplosions = 0
        d = {}

        for i in range(len(bombs)):
            currentBomb = bombs[i]
            d[i] = []
            for j in range(len(bombs)):
                if (j==i): continue
                if(detonates(currentBomb, bombs[j])):
                    d[i].append(j)
        
        d2 = {}
        for i in range(len(bombs)):
            stack = [i]
            detonated = set()
            while(stack):
                currentBomb = stack.pop()
                if (currentBomb not in detonated):
                    if(currentBomb in d2):
                        detonated.update(d2[currentBomb])
                    else:
                        detonated.add(currentBomb)
                        stack.extend(d[currentBomb])
            d2[i] = detonated
            nExplosions = max(nExplosions, len(detonated))

        return nExplosions

    # Solution 2, brute Force
    def maximumDetonation2(self, bombs: List[List[int]]) -> int:

        def detonates(bomb1, bomb2):
            x1, y1, r = bomb1
            x2, y2, _ = bomb2
            return abs((x2-x1)**2 + (y2-y1)**2)**0.5<=r
        

        nExplosions = []

        for i in range(len(bombs)):
            detonated = set([i])
            stack = [i]
            while stack:
                idx = stack.pop()
                currentBomb = bombs[idx]
                for j in range(len(bombs)):
                    if(j in detonated): continue
                    if(detonates(currentBomb, bombs[j])):
                        detonated.add(j)
                        stack.append(j)
            nExplosions.append(len(detonated))
        
        return max(nExplosions)



