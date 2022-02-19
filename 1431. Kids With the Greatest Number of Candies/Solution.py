# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        # Calculate the maximum number of candies any kid currently has,
        # then subtract the extra candies that we have to distribute.
        # This gives us the maximum number of candies that any kid could have
        # if they were given the extra candies.
        m = max(candies) - extraCandies 
        
        # Create a list of Boolean values, where each value corresponds to a kid.
        # The value is True if the number of candies that the kid would have after
        # receiving the extra candies is greater than or equal to the maximum number
        # of candies that any kid could have, and False otherwise.
        return [i >= m for i in candies]