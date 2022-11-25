# https://leetcode.com/problems/shortest-word-distance-iii

class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:

        res = len(wordsDict)
        lastword1 = None
        lastword2 = None

        if(word1 != word2):
            for i in range(len(wordsDict)):
                word = wordsDict[i]
                if(word == word1):
                    lastword1 = i
                    if(lastword1 is not None and lastword2 is not None):
                        res = min(res, abs(lastword2-lastword1))
                elif(word == word2):
                    lastword2 = i
                    if(lastword1 is not None and lastword2 is not None):
                        res = min(res, abs(lastword2-lastword1))
        else:
            lastOccurence = None
            for i in range(len(wordsDict)):
                if wordsDict[i] == word1:
                    if(lastOccurence is not None):
                        res = min(res, i-lastOccurence)
                    lastOccurence = i
        return res

            

