# https://leetcode.com/problems/race-car

class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 0, 1)])
        while queue:
            time, pos, vel = queue.popleft()

            if pos == target: return time
            time +=1
            npos = pos+vel
            queue.append((time, npos, 2 * vel))
 
            if (npos > target and vel > 0):
                queue.append((time, pos, -1))
            elif(npos < target and vel < 0):
                queue.append((time, pos, 1))