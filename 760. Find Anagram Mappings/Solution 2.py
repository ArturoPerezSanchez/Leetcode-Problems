# https://leetcode.com/problems/find-anagram-mappings

class Solution:
    # 2 Lines solution using list comprehension
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {j:i for i, j in enumerate(nums2)}
        return [d[i] for i in nums1]
