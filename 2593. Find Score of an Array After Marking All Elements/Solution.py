# https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements

class Solution(object):
    def findScore(self, nums):

        n = len(nums)
        marked = [False] * n
        score = 0

        # Create a priority queue of unmarked elements
        unmarked = [(nums[i], i) for i in range(n)]
        heapq.heapify(unmarked)

        while unmarked:
            # Get the smallest unmarked number
            smallest_val, smallest_idx = heapq.heappop(unmarked)

            # If the smallest number is already marked, skip it
            if marked[smallest_idx]:
                continue

            # Add the value of the smallest unmarked number to score
            score += smallest_val

            # Mark the smallest unmarked number and its two adjacent elements
            marked[smallest_idx] = True
            if smallest_idx > 0:
                heapq.heappush(unmarked, (nums[smallest_idx-1], smallest_idx-1))
                marked[smallest_idx-1] = True
            if smallest_idx < n-1:
                heapq.heappush(unmarked, (nums[smallest_idx+1], smallest_idx+1))
                marked[smallest_idx+1] = True

        return score
            
        