# https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/

def findPrefixScore(self, nums: List[int]) -> List[int]:
    # Initialize the current maximum value to the first number in the input list.
    currentmax = nums[0]
    
    # Initialize the result list with the first element twice the value of the first number in the input list.
    res = [2*nums[0]]
    
    # Loop through the remaining elements in the input list.
    for i in range(1, len(nums)):
        # Get the current number from the input list.
        val = nums[i]
        
        # Update the current maximum value if the current number is greater than the current maximum.
        currentmax = max(currentmax, val)
        
        # Compute the score for the current number using the formula and add it to the result list.
        # The score is the sum of the current number, the current maximum, and the previous score in the result list.
        res.append(val + currentmax + res[i-1])
    
    # Return the result list.
    return res