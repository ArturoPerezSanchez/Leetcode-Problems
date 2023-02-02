# https://leetcode.com/problems/removing-stars-from-a-string/description/

class Solution:

    #Using a stack and popping last added character when a star is found
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