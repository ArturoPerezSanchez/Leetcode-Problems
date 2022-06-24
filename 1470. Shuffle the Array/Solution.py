# https://leetcode.com/problems/shuffle-the-array

class Solution:
    # Option 1: Creating a new List O(n)
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = [0] * len(nums)
        for i in range(n):
            res[2*i], res[2*i+1] = nums[i], nums[i+n]
        return res
    
    # Option 2: In place O(n^2)
    def shuffle2(self, nums: List[int], n: int) -> List[int]:
        for i in range(n):
            nums.insert(2*i+1, nums.pop(n+i))
        return nums
    
    #Option 3: Using numpy
    def shuffle3(self, nums: List[int], n: int) -> List[int]:
        import numpy as np
        return np.array([[i, j] for i, j in zip(nums[:n], nums[n:])]).ravel()
    
    #Option 4: Using functools
    def shuffle4(self, nums: List[int], n: int) -> List[int]:
        from functools import reduce
  
        return reduce(operator.add, zip(nums[:n], nums[n:]))