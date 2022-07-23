# https://leetcode.com/problems/successful-pairs-of-spells-and-potions

class Solution:


    # Two line solution (using builtins)
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions = sorted(potions)
        return [len(potions) - bisect_right(potions, (success - 1) // x) for x in spells]


    # Time complexity: O((n+m)*log(m))
    def successfulPairs2(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Sort the potions array so we can apply binary search over it later
        potions.sort()

        # Result array
        res = []

        # Binary search modified to search the index of the first element in the potions array that multipled by the given input is at least "success"
        @cache
        def search(spell):
            l = 0
            r = len(potions)
            while(l<r):
                mid = (l+r)//2
                if(potions[mid]*spell >= success): r = mid
                else: l=mid+1
            return l

        # Iteration over the spell adding the number of valid pairs to the result set
        for spell in spells:
            res.append(len(potions) - search(spell))

        return res