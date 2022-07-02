# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique

class Solution:
    def minDeletions(self, s: str) -> int:
        d = {}
        ans = 0
        for ch in s:
            d[ch] = d.get(ch, 0) + 1
        
        freqList = list(sorted(d.values()))

        for i in range(len(freqList)-2, -1, -1):
            if (freqList[i] >= freqList[i+1] and freqList[i] > 0):
                eliminiations = min(freqList[i], freqList[i]-freqList[i+1]+1)
                ans += eliminiations
                freqList[i] -= eliminiations
        return ans
        