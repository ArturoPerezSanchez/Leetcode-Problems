# https://leetcode.com/problems/find-anagram-mappings

class Solution:
    ''' 
    2 Lines solution using list comprehension
    
    Time complexity: O(N), where n is the length of the input lists, because the dictionary d is created in O(n) time by iterating over the elements of nums2
                     The lookup operation in the dictionary d for each element in nums1 takes O(1) time, so the overall time complexity is O(n) for the entire code.

    Space complexity: O(N), because the dictionary d is created to store n key-value pairs and the output list also has n elements.
    '''
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {j:i for i, j in enumerate(nums2)}
        return [d[i] for i in nums1]
