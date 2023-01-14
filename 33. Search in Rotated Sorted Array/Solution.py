# https://leetcode.com/problems/search-in-rotated-sorted-array

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        if(len(nums) == 1): return 0 if nums[0] == target else -1
        
        rotationInd = len(nums)-1
        while(l<r):
            mid = (l+r)//2
            if(nums[mid] > nums[mid + 1]):
                rotationInd = mid
                break
            elif(nums[mid]>nums[l]):
                l = mid+1
            else:
                r = mid

        if(target == nums[rotationInd]): return rotationInd

        if(target >= nums[0]):
            l = 0
            r = rotationInd
        else:
            l = rotationInd +1
            r = len(nums)
        
        while(l<r):
            mid = (l+r)//2
            if(nums[mid] == target): return mid
            if(nums[mid] > target):
                r = mid
            else:
                l = mid+1

        return -1

