// https://leetcode.com/problems/removing-stars-from-a-string/description/

class Solution {
public:
    /*
    Time Complexity: The function iterates over each character in the input string s exactly once, performing a constant amount of work for each character.
                     The add and pop_back operations on the string res take constant time on average. Therefore, the time complexity of this function is O(n),
                     where n is the length of the input string.

    Space Complexity: The function uses a string to store characters as it iterates over the input string.
                      In the worst case, where there are no stars in the input string, the new string will contain all the characters in the input string.
                      Therefore, the space complexity of this function is also O(n), where n is the length of the input string.
    */

    string removeStars(string s) {
        string res; // creates an empty string

        // loops through each character in s
        for (char c : s) {

            // If the character is a star removes the last character from res, otherwise adds the character to res
            if (c == '*') { 
                res.pop_back();
            } else {
                res += c;
            }
        }

        return res; // returns the modified string
    }
};