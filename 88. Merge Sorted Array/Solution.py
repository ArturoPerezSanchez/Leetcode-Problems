# https://leetcode.com/problems/merge-sorted-array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if(nums2 == []): return nums1
        j = 0
        i = 0
        nums1[m:] = []
        while(i<len(nums1) and j < len(nums2)):
            if(nums1[i] > nums2[j]):
                nums1.insert(i, nums2[j])
                j+=1
            else:
                i+=1
        nums1 += nums2[j:]