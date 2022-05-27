class Solution:
    # The time complexity of this code is O(n), where n is the length of the input string s. This is because the code iterates over the string s only once, performing constant time operations at each iteration.
    # The space complexity is also O(n), as the dictionary d can hold up to n key-value pairs, one for each character in the string.
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}                  # A dictionary to keep track of characters and their indices
        res = 0                 # The final result to be returned
        currentcount = 0        # The length of the current substring without repeating characters
        lastr = 0               # The index of the last repeated character encountered
        for i in range(len(s)):
            if(s[i] in d):                  # If the current character is repeated, update variables
                res = max(res, currentcount)
                lastr = max(lastr, d[s[i]])
                currentcount = i - (lastr + 1)
            d[s[i]] = i                     # Add the current character to the dictionary
            currentcount +=1                # Increase the length of the current substring
        return max(res, currentcount)       # Return the maximum length found




