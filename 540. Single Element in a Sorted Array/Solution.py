# https://leetcode.com/problems/single-element-in-a-sorted-array

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        while(l<r):
            
            mid = (l+r)//2
            if(mid == 0 or mid == len(nums)-1): return nums[mid]

            if(mid%2 == 0):
                if(nums[mid] == nums[mid+1]):
                    l = mid+1
                elif(nums[mid] == nums[mid-1]):
                    r =  mid
                else:
                    return nums[mid]
            else:
                if(nums[mid] == nums[mid-1]):
                    l = mid+1
                elif(nums[mid] == nums[mid+1]):
                    r =  mid
                else:
                    return nums[mid]
        return nums[l]
