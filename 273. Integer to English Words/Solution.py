# https://leetcode.com/problems/integer-to-english-words

class Solution:
    def numberToWords(self, num: int) -> str:
        if(num == 0): return "Zero"
        snum = str(num)
        res = []
        numbers1 = [None,"One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
        numbers2 = [None, None, "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        numbers3 = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        sufixes = [None, None, "Hundred", "Thousand", None, "Hundred", "Million", None, "Hundred", "Billion",None]
        movingZero = False
        for i in range(len(snum)-1, -1, -1):
            multiplier = int(len(snum)-i)
            currentDigit = int(snum[i])
            
            if(currentDigit != 0):
                if(multiplier%3 == 2):
                    if(currentDigit == 1):
                        if(res and res[0] in numbers1): res.pop(0)
                        res.insert(0, numbers3[int(snum[i+1])])
                    else:
                        res.insert(0, numbers2[currentDigit])
                else:
                    if(numbers1[currentDigit] is not None):
                        res.insert(0, numbers1[currentDigit])
            
            if(i!= 0 and sufixes[multiplier] is not None):
                currentSuffix = sufixes[multiplier]
                if (res and res[0] in sufixes):
                    if(res[0] == "Hundred"):
                        res.pop(0)
                    if(res and res[0] == "Thousand"):
                        if(currentSuffix == "Million" or currentSuffix == "Billion"): res.pop(0)
                    if(res and res[0] == "Million"):
                        if(currentSuffix == "Billion"): res.pop(0)
                res.insert(0, currentSuffix)
                   

        return " ".join(res)

            
            