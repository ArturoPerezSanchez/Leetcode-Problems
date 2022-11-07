# https://leetcode.com/problems/task-scheduler

class Solution:
    # Solution 2: counting O(n)
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}
        for task in tasks: d[task] = d.get(task, 0) + 1
        
        biggestFrequency = 0
        occurences = 0
        for i in d.values():
            if(i>biggestFrequency):
                biggestFrequency = i
                occurences = 1
            elif(i==biggestFrequency):
                occurences +=1
        return max((biggestFrequency-1)*(n+1)+occurences, len(tasks))


    # Solution 1: counting and sorting O(nlog(n))
    def leastInterval2(self, tasks: List[str], n: int) -> int:
        d = {}
        for task in tasks:
            d[task] = d.get(task, 0) + 1
        
        sortedValues = sorted(d.values(), reverse=True)
        mostRepeatedTask = sortedValues[0]
        extra = 0
        while(extra<len(sortedValues)):
            if(sortedValues[extra] == mostRepeatedTask):
                extra+=1
            else:
                break
        return max((mostRepeatedTask-1)*(n+1)+extra, len(tasks))
