# https://leetcode.com/problems/minimum-time-to-complete-trips

class Solution(object):
    def minimumTime(self, time, totalTrips):
        """
        :type time: List[int]
        :type totalTrips: int
        :rtype: int
        """

        # Initialize the search range for minimum completion time
        x = min(time)
        l = x
        r = x * totalTrips

        # Binary search for minimum completion time
        while l < r:
            # Calculate the midpoint of the search range
            m = (l + r) // 2
            # Count the number of tasks that can be completed within m time
            if sum(m // t for t in time) >= totalTrips:
                # If enough tasks can be completed within m time, search for smaller time
                r = m
            else:
                # If not enough tasks can be completed within m time, search for larger time
                l = m + 1

        # Return the minimum completion time
        return l