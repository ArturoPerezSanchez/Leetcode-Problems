# https://leetcode.com/problems/subarray-sums-divisible-by-k

class Solution:

    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = {0:1}
        res = 0
        currentSum = 0
        for n in nums:
            currentSum +=n
            currentSum %= k
            if(currentSum not in d):
                d[currentSum] = 1
            else:
                res+= d[currentSum]
                d[currentSum]+=1
        return res


    # Brute force approach (TLE)
    def subarraysDivByK2(self, nums: List[int], k: int) -> int:
        res = 0
        rem = 0
        for i in range(len(nums)):
            rem += nums[i]
            if(rem>=k): rem=rem%k
            if(rem == 0): res+=1
            
            for j in range(i+1, len(nums)):
                if(rem>=k): rem=rem%k
                if(rem == 0): res+=1
        return res