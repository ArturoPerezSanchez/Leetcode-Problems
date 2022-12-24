# https://leetcode.com/problems/top-k-frequent-words

class Solution:
    # O(Nlog(K)) Using heap
    def topKFrequent2(self, words: List[str], k: int) -> List[str]:
        d = {}
        for word in words: d[word] = d.get(word, 0) - 1 # O(N)
        return heapq.nsmallest(k, d.keys(), key=lambda x: (d[x],x)) # O(Nlog(K))

    # O(Nlog(N)) not using heap
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        for word in words: d[word] = d.get(word, 0) - 1 # O(N)
        keys = list(d.keys())

        keys.sort(key=lambda x: (d[x],x))
        return keys[:k]
