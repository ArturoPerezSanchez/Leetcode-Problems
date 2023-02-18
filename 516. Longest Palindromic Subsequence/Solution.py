# https://leetcode.com/problems/longest-palindromic-subsequence/

class Solution:
    '''
    Time complexity: The time complexity of the algorithm is O(n^2), where n is the length of the input string, due to the recursive calls and memoization.

    Space complexity: The space complexity of the algorithm is also O(n^2), as we use memoization to store the results of subproblems in a cache, which can take up to O(n^2) space.
    '''
    def longestPalindromeSubseq(self, s: str) -> int:
        
        # Define a recursive function rec with memoization using the cache decorator
        @cache
        def rec(l, r):
            # If the left index is greater than the right index, return 0
            if(l>r): return 0
            # If the left and right indices are the same, return 1 (a single character is considered a palindrome of size 1)
            if(l==r): return 1

            # If the characters at the left and right indices are the same, add 2 and perform the recursive call of the function excluding the left and right characters
            if(s[l] == s[r]):
                return 2 + rec(l+1, r-1)

            # Otherwise, return the maximum of the result of recursively call the function excluding the left or right character 
            return max(rec(l+1,r), rec(l, r-1))
        
        # Return the result of calling the recursive function with the whole string
        return rec(0, len(s)-1)
