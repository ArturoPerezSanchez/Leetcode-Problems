# https://leetcode.com/problems/is-subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer = -1
        for i in s:
            while pointer<len(t)-1:
                pointer +=1
                if t[pointer]==i:
                    break
            else:
                return False
        return True