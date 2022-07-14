# https://leetcode.com/problems/kth-missing-positive-number

class Solution:
    # Using binary search
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if(arr[-1]-len(arr)<k): return arr[-1]+(k-(arr[-1]-len(arr)))
        l = 0
        r = len(arr)
        while(l<r):
            mid = (l+r)//2
            if(arr[mid] - mid -1< k):
                l = mid
            else:
                if(arr[mid-1] - (mid-1) <= k):
                    return arr[mid]+k-(arr[mid]-mid)
                else:
                    r = mid
        return arr[r]+k-(arr[r]-r)




    # Counting the missing numbers one by one, O(n+k)
    def findKthPositive2(self, arr: List[int], k: int) -> int:
        missing_counter = 0
        i = 0
        while(True):
            if(i<len(arr)):
                if(missing_counter+i+1<arr[i]):
                    missing_counter+=1
                    if(missing_counter==k):
                        return missing_counter+i
                else:
                    i+=1
            else:
                return arr[-1]+k-missing_counter

