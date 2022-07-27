# https://leetcode.com/problems/maximum-difference-by-remapping-a-digit

class Solution:
    def minMaxDifference(self, num: int) -> int:
        num = str(num)
        firstC = num[0]
        firstNotNine = None
        
        for i in num:
            if(int(i) != 9):
                firstNotNine = i
                break
        minimum = num.replace(firstC, "0")
        if(firstNotNine): maximum = num.replace(firstNotNine, "9")
        else: maximum=num
        
        return int(maximum) - int(minimum)