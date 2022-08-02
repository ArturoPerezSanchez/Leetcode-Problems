# https://leetcode.com/problems/longest-common-prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        res = ""
        for i in range(min([len(i) for i in strs])):
            currentChar = strs[0][i]

            for word in (strs):
                if(word[i] != currentChar):
                    return res
            res += currentChar
        return res
            