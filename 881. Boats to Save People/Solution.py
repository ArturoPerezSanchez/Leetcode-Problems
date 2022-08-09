# https://leetcode.com/problems/boats-to-save-people

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l = 0
        r = len(people)-1
        res = 0
        
        while(l<=r):
            if (people[r] + people[l] <= limit):
                l+=1
            res +=1
            r-=1
        return res