# https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/

class Solution:
    '''
    Time complexity: O(n * k^2), where n is the number of piles and k is the maximum weight.
                     This is because we iterate through each pile and each weight up to k in the nested loops.

    Space complexity: O(n * k), since we create a 2D dp array of size n x k, as well as arrays of size n and count.
    '''
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        
        # Get the number of piles and increment k
        n = len(piles)
        k += 1
        
        # Initialize previous array and the counter
        prev = [0]
        count = 0
        
        # Loop through each pile
        for i in range(n):
            
            # Get the current pile
            pile = piles[i]
            acum = 0
            
            # Loop through each coin in the pile
            for j in range(len(pile)):
                
                # Get the value of the current coin and update the pile
                val = pile[j]
                pile[j] = acum
                acum +=val
                
                # Increment the counter
                count +=1
            
            # Add the accumulated value of the pile to the end of the pile
            pile.append(acum)
            # Add the current count to the previous array
            prev.append(count)

        # Initialize the dp array
        dp = [[0]*k for i in range(count+1)]
        
        # Loop through each pile
        for i in range(n):
            
            # Loop through each coin in the pile
            for j in range(1, len(piles[i])):
                
                # Get the profit and weight of the current coin
                profit = piles[i][j]
                wt = j
                
                # Get the level of the current coin
                lvl = prev[i]+j
                
                # Loop through each weight
                for w in range(1, k):
                    
                    # Update the dp array based on the weight and profit
                    if wt > w:
                        dp[lvl][w] = dp[lvl-1][w]
                    else:
                        dp[lvl][w] = max(dp[lvl-1][w], profit+dp[prev[i]][w-wt])

        # Return the last element of the last row of the dp array
        return dp[-1][-1]