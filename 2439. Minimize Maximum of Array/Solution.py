# https://leetcode.com/problems/minimize-maximum-of-array

class Solution:

    # Using acumulated sum, time complexity: O(n)
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = 0
        currentsum = 0
        for i in range(len(nums)):
            currentsum += nums[i]
            res = max(res, ceil(currentsum/(i+1)))
        return res


    # Using Binary search, time complexity: O(n*log(m)) where n is the length of the list and m the difference between the highest number and the average
    def minimizeArrayValue2(self, nums: List[int]) -> int:
        
        # return True if its possible to distribute the nums array so that the largest value is at most target
        def isPossible(target):
            carry = 0
            for i in range(len(nums)-1, 0, -1):
                carry = max(0, nums[i] - target + carry)
                
            return nums[0] + carry <= target
        
        l = ceil(sum(nums)/len(nums))
        r = max(nums)
        
        while(l<r):
            mid = (l+r)//2
            if(isPossible(mid)):
                r = mid
            else:
                l = mid +1
        return l
