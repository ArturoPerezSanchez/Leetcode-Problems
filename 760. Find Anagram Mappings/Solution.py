# https://leetcode.com/problems/find-anagram-mappings

class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
    # Create an empty dictionary called d
    d = {}
    
    # For each element j in nums2, create a key-value pair in dictionary d where the key is j and the value is its index
    for i, j in enumerate(nums2):
        d[j] = i
    
    # Create an empty list called res
    res = []
    
    # For each element i in nums1, append the value corresponding to the key i in dictionary d to the list res
    for i in nums1:
        res.append(d[i])
    
    # Return the list res
    return res