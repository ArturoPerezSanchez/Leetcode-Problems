# https://leetcode.com/problems/course-schedule-ii

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses
        adj = {i: [] for i in range(numCourses)}
        stack = []
        res = []

        for i, j in prerequisites:
            indegree[i] +=1
            adj[j].append(i)
        
        for i in range(numCourses):
            if(indegree[i] == 0):
                stack.append(i)
        
        while stack:
            currentCourse = stack.pop()
            for nextCourse in adj[currentCourse]:
                indegree[nextCourse] -=1
                if(indegree[nextCourse] == 0):
                    stack.append(nextCourse)
            res.append(currentCourse)
        if(sum(indegree) != 0): return []
        return res

                