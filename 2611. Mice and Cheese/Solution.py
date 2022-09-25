# https://leetcode.com/problems/mice-and-cheese

class Solution:

    # Time complexity O(n*log(n))
    # Space complexity O(n)
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:

        diffs = sorted([(reward1[i], reward2[i]) for i in range(len(reward1))], key=lambda t: t[1] - t[0])

        return sum([i[0] for i in diffs[:k]]) + sum([i[1] for i in diffs[k:]])
