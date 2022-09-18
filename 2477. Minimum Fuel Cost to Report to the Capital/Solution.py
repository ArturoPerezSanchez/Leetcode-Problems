# https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int: 
        if(len(roads)<2): return len(roads)
        d = {}
        for i in roads:
            if i[0] not in d:
                d[i[0]] = [i[1]]
            else:
                d[i[0]].append(i[1])
            if i[1] not in d:
                d[i[1]] = [i[0]]
            else:
                d[i[1]].append(i[0])
            
        # The total fuel needed, it will be updated in the dfs.
        global res
        res = 0

        # The graph has no cycles, but it is undirected,
        # so we need to pass in the parent node here to make sure it is not traveling backward.
        def dfs(node,parent):
            global res
            # Count how many people arrived at the current node.
            # Start with 1 because each node initially has one people.
            totalPeople = 1

            for child in d[node]:
            	# Make sure to not travel backward.
                if child != parent:

                    people, car = dfs(child,node)
                    
                    # Adding the people arraving the current node
                    totalPeople += people
                    
                    # Add the number of cars going from the child node to the current node to the result
                    # Since each car traveled on edge, number of cars == number of fuel used
                    res += car

            # Based on the number of people arrived at the current node, we can calcualte the cars actually needed.
            # In other words, we try to rearrange the people in the minimum number of cars possible bease on the seats each car has.
            cars = ceil(totalPeople/seats)
            
            # If this is at a leaf node, totalPeople=1, and cars=1 
            return totalPeople,cars

        dfs(0,None)
        return res