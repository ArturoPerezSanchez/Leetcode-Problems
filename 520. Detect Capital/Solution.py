# https://leetcode.com/problems/detect-capital

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cap = word[0].isupper()
        if (cap == True and len(word)>1):
            cap = word[1].isupper()
        for i in word[1:]:
            if (cap != i.isupper()):
                return False
        return True