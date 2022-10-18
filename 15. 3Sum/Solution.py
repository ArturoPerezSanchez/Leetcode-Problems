# https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if(len(nums) < 3):
            return []
        nums = sorted(nums)
        res = []
        t=0
        while(t<len(nums) and nums[t]<=0):
            rp = len(nums)-1
            if(t>0):
                while(nums[t] == nums[t-1] and t<rp):
                    t+=1
            lp = t+1

            while (lp<rp):
                threesum = nums[t] + nums[lp] + nums[rp]
                if(threesum < 0):
                    while(lp<rp and nums[lp] == nums[lp+1]):
                        lp +=1
                    lp+=1
                elif(threesum > 0):
                    while(lp<rp and nums[rp] == nums[rp-1]):
                        rp -=1
                    rp-=1
                    if(nums[rp]<0):
                        break
                else:
                    res.append([nums[t], nums[lp], nums[rp]])
                    while(lp<rp and nums[lp] == nums[lp+1]):
                        lp +=1
                    while(lp<rp and nums[rp] == nums[rp-1]):
                        rp -=1
                    lp+=1
                    rp-=1
                    if(nums[rp]<0):
                        break
            t+=1
        return res