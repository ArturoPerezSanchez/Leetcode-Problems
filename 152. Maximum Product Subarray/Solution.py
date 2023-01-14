# https://leetcode.com/problems/maximum-product-subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        lastind = 0
        currentmult = 0
        res = nums[0]
        c = 0
        for ind in range(len(nums)):
            print(currentmult, lastind, res)
            i = nums[ind]
            if(not currentmult):
                currentmult = i
                lastind = ind
                res = max(res, currentmult)
                continue
            if(i != 0):
                currentmult*= i
                res = max(res, currentmult)

            else:
                while(currentmult < 0 and lastind<ind-1 and nums[lastind] != 0):
                    currentmult/=nums[lastind]
                    lastind+=1
                
                res = max(res, currentmult,0)
                currentmult = 0
                print('aaaa')
                lastind = ind+1
        

        while(currentmult < 0 and lastind<len(nums)-1 and nums[lastind] != 0):
            currentmult/=nums[lastind]
            lastind+=1
        res = max(res, currentmult)
        return int(res)

        