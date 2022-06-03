# https://leetcode.com/problems/sort-colors

class Solution:
    # Counting colors O(n)
    def sortColors(self, nums: List[int]) -> None:
        reds_num = 0
        whites_num = 0
        for color in nums:
            if(color == 0):
                reds_num +=1
            elif( color == 1):
                whites_num +=1
        
        for red in range(reds_num):
            nums[red] = 0
        
        for white in range(reds_num, reds_num + whites_num):
            nums[white] = 1
        
        for blue in range(reds_num + whites_num, len(nums)):
            nums[blue] = 2


    # Easy solution O(n^2)
    def sortColors2(self, nums: List[int]) -> None:
        ind = 0
        end =  len(nums)
        while ind < end:
            if(nums[ind] == 0):
                nums.insert(0,nums.pop(ind))
            if(nums[ind] == 2):
                nums.append(nums.pop(ind))
                end -= 1
                ind -= 1
            ind +=1