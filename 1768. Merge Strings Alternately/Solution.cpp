// https://leetcode.com/problems/merge-strings-alternately

class Solution{
    /*
    Time complexity: O(n), where n is the length of the longer string between word1 and word2. The for loop iterates through the characters of the two strings
                     using the zip function, which takes O(min(len(word1), len(word2))) time. The concatenation of the characters also takes O(1) time.
                     Then, the if-else block after the for loop takes O(max(len(word1), len(word2)) - min(len(word1), len(word2))) time to concatenate the remaining characters.

    Space complexity: O(m + n), where m is the length of word1 and n is the length of word2.
                      Since the "res" variable stores the merged string, it takes up space equivalent to the total length of word1 and word2.
    */
    public:
    string mergeAlternately(string word1, string word2) {
        string res; // Empty string to store the result
        int i = 0;  // Counter for the current position in the input strings
        
        // start an infinite loop that will be broken out of when both strings have been fully processed
        while(true){ 
            
            // if there are more characters to process in 'word1', add the character at the current position to the result string
            if(i<word1.size()){ 
                res.push_back(word1[i]);
            // if 'word1' has been fully processed, process the remaining characters in 'word2'
            } else { 
                while(i<word2.size()){
                    res.push_back(word2[i]);
                    i++;
                }

                // break the main loop
                break;
            }

            // if there are more characters to process in 'word2', add the character at the current position to the result string
            if(i<word2.size()){
                res.push_back(word2[i]); 
            // if 'word2' has been fully processed, process the remaining characters in 'word1'
            } else {
                i++;
                while(i<word1.size()){
                    res.push_back(word1[i]);
                    i++;
                }
                // break the main loop
                break;
            }

            // increment the counter
            i++; 
        }

        // After the main loop ends, return the result string
        return res;
    }

};