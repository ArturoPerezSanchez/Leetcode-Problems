class Solution:

    # Time complexity: O(n), where n is the length of the input list "nums"
    def twoSum(self, nums, target):
        complements = {}  # dictionary to store the complements
        
        # iterate over the input list
        for i in range(len(nums)):
            complement = target - nums[i]  # calculate the complement for the ith element of the list
            
            # if the ith element is already in the complements dictionary return i and the index of the complement
            if nums[i] in complements: return [complements[nums[i]], i]

            # add the complement and its index to the dictionary
            complements[complement] = i