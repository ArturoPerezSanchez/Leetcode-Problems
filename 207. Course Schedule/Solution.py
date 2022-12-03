# https://leetcode.com/problems/course-schedule

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Dictionary with the requirements of each course
        global d
        d = {course: [] for course in range(numCourses)}
        for course, required in prerequisites: d[course].append(required)

        # Array of size numCourses where visited_i indicates if we have already taken course i
        visited = [0]*numCourses

        def fillStack():
            global d
            global stack
            toRemove = []
            for course, requirements in d.items():
                if(visited[course] == 1):
                    toRemove.append(course)
                    continue
                canAppend = True
                i = 0
                while i < len(requirements):
                    if(visited[requirements[i]] == 0):
                        canAppend = False
                        i = len(requirements)
                    else:
                        requirements.pop(i)
                if(canAppend): stack.append(course)
            for i in toRemove:
                del d[i]
        # Stack with the next courses to take
        global stack
        stack = deque()
        fillStack()
        while(stack):
            while(stack):
                visited[stack.pop()]=1
            fillStack()
        
        for i in visited:
            if(i == 0):
                return False
        return True
















