# https://leetcode.com/problems/asteroid-collision

class Solution:


    # Brute force solution, modifying in place
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        currentdir = "r"
        ind = 0
        while(ind<len(asteroids)):
            rock = asteroids[ind]

            if currentdir == "r":
                if(rock<0 and ind!=0 and asteroids[ind-1]>0):
                    prev = asteroids[ind-1]
                    if(abs(rock) == abs(prev)):
                        asteroids.pop(ind-1)
                        asteroids.pop(ind-1)
                        ind-=2
                    elif(abs(rock) > abs(prev)):
                        asteroids.pop(ind-1)
                        currentdir = "l"
                        ind-=1
                    else:
                        asteroids.pop(ind)
                        ind-=1
            else:
                if(rock>0 and ind!=len(asteroids)-1 and asteroids[ind+1]<0):
                    nex = asteroids[ind+1]
                    if(abs(rock) == abs(nex)):
                        asteroids.pop(ind)
                        asteroids.pop(ind)
                        ind-=2
                    elif(abs(rock) > abs(nex)):
                        asteroids.pop(ind+1)
                        currentdir = "r"
                        continue
                    else:
                        asteroids.pop(ind)
                        continue


            if(currentdir == "l"):
                if(ind <= 0):
                    ind = 0
                    currentdir = "r"
                else:
                    ind-=1
            if(currentdir == "r"):
                ind += 1
        return asteroids

        