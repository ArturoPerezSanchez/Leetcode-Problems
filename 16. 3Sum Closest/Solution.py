# https://leetcode.com/problems/3sum-closest

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        t=0
        closest = None
        while(t<len(nums)):
            rp = len(nums)-1
            if(t>0):
                while(nums[t] == nums[t-1] and t<rp):
                    t+=1
            lp = t+1

            while (lp<rp):

                threesum = nums[t] + nums[lp] + nums[rp]
                if (closest == None or (abs(closest-target) > abs(threesum - target))):

                    closest = threesum
                if(threesum < target):
                    while(lp<rp and nums[lp] == nums[lp+1]):
                        lp +=1
                    lp+=1
                elif(threesum > target):
                    while(lp<rp and nums[rp] == nums[rp-1]):
                        rp -=1
                    rp-=1
                else:
                    break
            t+=1
        return closest