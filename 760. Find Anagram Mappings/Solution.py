# https://leetcode.com/problems/find-anagram-mappings

class Solution:
	'''
    Time complexity: O(N), where n is the length of the input lists, because the dictionary d is created in O(n) time by iterating over the elements of nums2
                     The lookup operation in the dictionary d for each element in nums1 takes O(1) time, so the overall time complexity is O(n) for the entire code.

    Space complexity: O(N), because the dictionary d is created to store n key-value pairs and the output list also has n elements.
	'''
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