// https://leetcode.com/problems/validate-stack-sequences
class Solution {
public:
    /*
        Time complexity: O(n), where n is the length of the pushed list. The code loops through each element
                         of the pushed list once and performs constant time operations on each iteration.

        Space complexity: O(n), where n is the length of the pushed list. The code uses a stack to keep track of the pushed elements,
                          and in the worst case scenario, the stack will contain all n elements of the pushed list.
    */
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        // Create an empty stack
        stack<int> st;

        // Set the variables i and j to 0
        // the i will be a pointer to the pushed vector
        // the j will be a pointer to the popped vector
        int i = 0;
        int j = 0;

        // Loop through the pushed list
        while(i < pushed.size()){
            // Add the current element of the pushed vector to the stack
            st.push(pushed[i]);

            // While the number pointed by j in the popped list matches the top of the stack, pop that element from the stack and update j
            while(st.size() > 0 && popped[j] == st.top()){
                j++;
                st.pop();
            }

            // Update i
            i++;
        }

        // If the stack is empty return True, otherwise there are unpopped elements so return False
        return st.size() == 0;
    }
};
