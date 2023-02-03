# https://leetcode.com/problems/removing-stars-from-a-string/description/

class Solution:

    '''
    Using a stack and popping last added character when a star is found
    Time Complexity: The function iterates over each character in the input string s exactly once, performing a constant amount of work for each character.
                     The append and pop operations on the stack both take constant time on average. Therefore, the time complexity of this function is O(n),
                     where n is the length of the input string.

    Space Complexity: The function uses a stack data structure to store characters as it iterates over the input string.
                      In the worst case, where there are no stars in the input string, the stack will contain all the characters in the input string.
                      Therefore, the space complexity of this function is also O(n), where n is the length of the input string.
    '''
    def removeStars(self, s: str) -> str:
        stack = []  # create an empty stack

        # iterate over each character in the input string
        for i in s:
            # if the current character is a star remove the last character added to the stack, otherwise add the character to the stack
            if (i == "*"): 
                stack.pop()
            else:
                stack.append(i)
        
        # join the remaining characters in the stack and return as a string
        return ''.join(stack)