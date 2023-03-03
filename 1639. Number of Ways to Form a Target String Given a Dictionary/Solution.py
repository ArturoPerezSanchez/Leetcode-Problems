# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/


def numWays(self, words: List[str], target: str) -> int:      
    # Find the length of each word in the input list and store it in 'n'
    n = len(words[0])
    # Create an empty list 'arr'
    arr = []

    # Iterate through each index of a word and count the frequency of each character in that index
    # Store these counts in a dictionary and append the dictionary to the 'arr' list
    for i in range(n):
        d = {} 
        for word in words:
            d[word[i]] = d.get(word[i], 0) + 1
        arr.append(d)

    # Create an empty dictionary 'visited'
    visited = {}

    # Define a recursive function 'rec' that takes in two parameters: the index of the target string and 
    # the index of the source string, and returns an integer value
    def rec(targetInd, sourceInd):
        # Base Case:
        # If the current combination of 'targetInd' and 'sourceInd' has been visited before, return the 
        # value stored in 'visited' for that combination
        if((targetInd, sourceInd) in visited): return visited[(targetInd, sourceInd)]
        # If we have reached the end of the target string, we have found a valid combination, so return 1
        if(targetInd >= len(target)): return 1
        # If the remaining length of the target string is greater than the remaining length of the source string,
        # we cannot find a valid combination, so return 0
        if(len(target) - targetInd > n-sourceInd): return 0

        # Recursive Case:
        # Get the current character of the target string and the counts of characters in the current index
        # of the source string
        s = target[targetInd]
        d = arr[sourceInd]
        aux = 0
        # If the current character of the target string is present in the current index of the source string,
        # calculate the number of valid combinations that can be formed by including the current character 
        # and move to the next index of both strings
        if(s in d):
            aux = d[s] * rec(targetInd + 1, sourceInd + 1)

        # Calculate the number of valid combinations that can be formed by excluding the current character
        # from the source string and moving to the next index of the source string
        aux += rec(targetInd, sourceInd + 1)
        # Store the result of the current combination in 'visited' for future reference
        visited[(targetInd, sourceInd)] = aux%(10**9 + 7)
        # Return the result of the current combination
        return visited[(targetInd, sourceInd)] 

    # Call the recursive function with the initial index values of 0
    return rec(0, 0)
