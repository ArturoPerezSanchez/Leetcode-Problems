# https://leetcode.com/problems/minimum-number-of-keypresses

class Solution:
    def minimumKeypresses(self, s: str) -> int:
        counts = Counter(s)
        ans = count = 0
        for i, freq in enumerate(sorted(counts.values(), reverse = True)):
            if i % 9 == 0:
                count+=1
            ans += (count * freq)
        return ans
