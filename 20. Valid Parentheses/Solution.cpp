// https://leetcode.com/problems/valid-parentheses

class Solution {
public:
    /*
    Time complexity: O(n), where n is the length of the input string s. 
    We iterate over each character in the string once, and each stack operation takes O(1) time.
    
    Space complexity: O(n), where n is the length of the input string s.
    In the worst case, we may need to store all opening brackets on the stack.
    */
    bool isValid(string s) {
        // create an empty stack to store opening brackets
        stack<char> st; 

        // iterate over each character in the input string
        for (char c : s) { 

            // push the character onto the stack if is an opening bracket
            if (c == '(' || c == '{' || c == '[') {
                st.push(c);
            
            // if its a closing bracket, check whether the top of the stack contains the corresponding opening bracket
            } else if (st.empty() || ( 
                      (c == ')' && st.top() != '(') ||
                      (c == '}' && st.top() != '{') ||
                      (c == ']' && st.top() != '[')
                      )) {

                // if there is no matching opening bracket or the brackets do not match, return false
                return false; 
            } else {
                // otherwise, remove the top element from the stack
                st.pop(); 
            }
        }
        // if the stack is empty, then all opening brackets have been matched and the string is valid
        return st.empty(); 
    }

};