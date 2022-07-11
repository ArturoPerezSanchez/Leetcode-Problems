# https://leetcode.com/problems/bus-routes


class Solution:
    # Auxiliary class, combining a list and a set to get a list with unique values
    class UniqueList:
        def __init__(self):
            self.l = []
            self.set = set()

        def __getitem__(self, item):
                return self.l[item]

        def add(self, item):
            if item not in self.set:
                self.l.append(item)
                self.set.add(item)


    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if(source == target): return 0
        d = defaultdict(list)
        stack = self.UniqueList()
        for i in range(len(routes)):
            route = routes[i]
            for j in route:
                if(j == source): stack.add(i)
                d[j].append(i)
        
        jumps = 1
        i = 0
        while (i<len(stack.l)):
            for j in range(i, len(stack.l)):
                currentBus = stack[j]
                for city in routes[currentBus]:
                    if(city == target): return jumps
                    for bus in d[city]: stack.add(bus)
            
            i = j+1
            jumps +=1
        return -1



    # Simple BFS solution (TLE)
    def numBusesToDestination2(self, routes: List[List[int]], source: int, target: int) -> int:
        d = defaultdict(list)

        for route in routes:
            for i in range(len(route)):
                for j in range(i+1, len(route)):
                    d[route[i]].append(route[j])
                    d[route[j]].append(route[i])
        
        stack = deque([source])
        jumps = 0
        visited = set()
        while stack:
            for i in range(len(stack)):
                currentCity = stack.popleft()
                if(currentCity == target): return jumps
                if(currentCity not in visited):
                    visited.add(currentCity)
                    stack.extend(d[currentCity])
            jumps +=1

        return -1
