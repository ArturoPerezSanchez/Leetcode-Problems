# https://leetcode.com/problems/delete-columns-to-make-sorted

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        for col in range(len(strs[0])):
            curr = "a"
            for row in strs:
                if(curr>row[col]):
                    res +=1
                    break
                curr = row[col]
        return res
