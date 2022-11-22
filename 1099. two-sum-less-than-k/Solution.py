# https://leetcode.com/problems/two-sum-less-than-k

class Solution:

    # Solution 1: Sorting the list and using 2 pointers
    def twoSumLessThanK1(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = len(nums)-1
        res = -1
        while(l<r):
            s = nums[l] + nums[r]
            if(s < k):
                res = max(res, s)
                l+=1
            else:
                r-=1
        return res

    # Solution 2: Counting 
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        d = {}
        
        for num in nums:
            if(num in d): d[num] = True
            else: d[num] = False

        values = sorted(list(d.keys()))
        l, r = 0, len(values)-1
        res = -1
        while(l < r):
            if(values[l] + values[r] >= k): 
                r -= 1
                continue
            res = max(res, values[l] + values[r])
            l += 1
        if(d[values[l]] and values[l]*2<k): return max(res, values[l]*2)
        return res