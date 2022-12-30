# https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string

class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        res = 0
        currentSum = 0
        countingZeroes = True
        for i in s:
            if i == "0":
                if(countingZeroes):
                    currentSum +=1
                else:
                    countingZeroes = True
                    currentSum = 1
            else:
                if(countingZeroes):
                    currentCount = 1
                    countingZeroes = False
                    currentSum -= 1
                else:
                    currentCount +=1
                    currentSum -= 1

                if(currentSum >= 0):
                    res = max(res, currentCount*2)
        
        return res