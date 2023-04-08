# https://leetcode.com/problems/valid-word-square

class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i in range(len(words)):
            for j in range(len(words[i])):
                if j >= len(words) or i >= len(words[j]): return False
                if words[j][i] != words[i][j]: return False
        return True