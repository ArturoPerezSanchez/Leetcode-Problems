# https://leetcode.com/problems/merge-strings-alternately

class Solution:
    '''
    Time complexity: O(n), where n is the length of the longer string between word1 and word2. The for loop iterates through the characters of the two strings
                     using the zip function, which takes O(min(len(word1), len(word2))) time. The concatenation of the characters also takes O(1) time.
                     Then, the if-else block after the for loop takes O(max(len(word1), len(word2)) - min(len(word1), len(word2))) time to concatenate the remaining characters.

    Space complexity: O(m + n), where m is the length of word1 and n is the length of word2.
                      Since the "res" variable stores the merged string, it takes up space equivalent to the total length of word1 and word2.
    '''
    def mergeAlternately(self, word1: str, word2: str) -> str:
    # Initialize an empty string to store the merged result
    res = ""
    # Iterate through the characters of word1 and word2 using the zip function
    for i, j in zip(word1, word2):
        # Concatenate the characters from word1 and word2 alternately
        res += i + j
    
    # If word1 is longer than word2, concatenate the remaining characters of word1 to the result
    if(len(word1) > len(word2)): res += word1[len(word2):]

    # Otherwise, if word2 is longer than word1, concatenate the remaining characters of word2 to the result
    elif(len(word2) > len(word1)): res += word2[len(word1):]
    
    # Return the merged string
    return res