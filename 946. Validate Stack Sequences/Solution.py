# https://leetcode.com/problems/validate-stack-sequences

class Solution:
    '''
        Time complexity: O(n), where n is the length of the pushed list. The code loops through each element
                         of the pushed list once and performs constant time operations on each iteration.

        Space complexity: O(n), where n is the length of the pushed list. The code uses a stack to keep track of the pushed elements,
                          and in the worst case scenario, the stack will contain all n elements of the pushed list.
    '''
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        # If the pushed list is empty, return True if the popped list is also empty, otherwise return False
        if not pushed: return len(popped) == 0

        # Create an empty stack
        st = []

        # Set the variables i and j to 0
        i = 0
        j = 0

        # Loop through the pushed list
        while(i<len(pushed)):
            
            # Append the current element of the pushed list to the stack
            st.append(pushed[i])
            
            # Loop while the stack is not empty and the current element of the popped list is equal to the top element of the stack
            while(st and popped[j] == st[-1]):
                
                # Increment j and pop the top element from the stack
                j+=1
                st.pop()
            
            # Increment i
            i += 1

        # If the stack is empty, return True, otherwise return False
        return len(st) == 0