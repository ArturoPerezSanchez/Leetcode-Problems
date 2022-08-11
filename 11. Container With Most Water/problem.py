class Solution:

    # Time: O(n), Space: O(1)
    def maxArea(self, height: List[int]) -> int:
        l,m=0,0            # set left pointer and max area to 0
        r=len(height)-1    # set right pointer to end of list
        while (l<r):       # repeat until pointers meet or cross each other
            if(height[l] < height[r]):   # if height at left pointer is less than that at right pointer
                s=(r-l)*height[l]        # calculate area
                m=max(m,s)               # update max area
                p=height[l]              # store height at left pointer
                while (l<r and height[l]<=p):  # move left pointer until we find height greater than p
                    l+=1
            else:                        # if height at right pointer is less than or equal to that at left pointer
                s=(r-l)*height[r]        # calculate area
                m=max(m,s)               # update max area
                p=height[r]              # store height at right pointer
                while (l<r and height[r]<=p):  # move right pointer until we find height greater than p
                    r-=1
        return m                        # return max area