# https://leetcode.com/problems/profitable-schemes/


class Solution:
    
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        
        # Create a list of tuples (group, profit) sorted by group
        l = sorted(zip(group, profit))

        # Define a recursive function
        #   remaining_members: int representing the members that havent commited a crime yet
        #   currentProfit: int representing the accumulated profit (if its bigger than minProfit, we simply pass minProfit as parameter)
        #   ind: int index that iterates through the l previously created list of tuples
        # the cache decorator its used to avoid the execution of the function with the same parameters more than once
        @cache
        def rec (remaining_members, currentProfit, ind):
            
            # Base case: If we have iterated through the whole list or the group members required for current element of the list is bigger than the remaining members.
            # 			 Return 1 if accumulated profit is greater or equal than minProfit, otherwise return 0
            if (ind>=len(l) or l[ind][0] > remaining_members):
                return 1 if (currentProfit >= minProfit) else 0
            

            # Recursive Case: Call the function selecting the ind and not selecting it, for better performance, when selecting the current crime
            # 				  check if we have reached the required minProfit, if so simply set it as the currentProfit parameter
            r1 = rec(remaining_members - l[ind][0], min(currentProfit + l[ind][1], minProfit), ind+1)
            r2 = rec(remaining_members, currentProfit, ind+1)

            # add the result of the 2 recursive calls and return it
            return r1 + r2
        
        # Call the recursive function rec() with initial parameters n, 0, and 0 and return the result modulo 10^9+7
        return rec(n, 0, 0)%(10**9+7)