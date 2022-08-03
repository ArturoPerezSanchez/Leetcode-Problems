# https://leetcode.com/problems/majority-element

class Solution:
    # Storing count of occurences O(n)
    def majorityElement1(self, nums: List[int]) -> int:
        d = {}
        res = None
        occurences = 0
        for num in nums:
            d[num] = d.get(num, 0) + 1
            if(d[num] > occurences):
                res = num
                occurences = d[num]
        return res
    
    # Storing count of occurences O(n)
    def majorityElement(self, nums: List[int]) -> int:
        res = None
        occurences = 0
        for num in nums:
            if(occurences == 0):
                res = num
                occurences = 1
                continue
            if(num==res): occurences +=2
            occurences -=1
        return res

    # sorting, O(nlog(n))
    def majorityElement2(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

    # One line solution, sorting, O(nlog(n))
    def majorityElement3(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]
    
    # One line solution, using mode from statistic package O(n)
    def majorityElement4(self, nums: List[int]) -> int:
        return mode(nums)