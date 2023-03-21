// https://leetcode.com/problems/sign-of-the-product-of-an-array/description/

class Solution {
public:
    /*
    Time complexity: O(n), where n is the size of the input vector. The function iterates through each element in the input vector exactly once.

    Space complexity: O(1). The function uses a constant amount of extra space, independent of the size of the input vector.
    */
    int arraySign(vector<int>& nums) {
        // Initialize a variable to keep track of the sign of the product of all elements in the vector
        int res = 1;

        // Iterate through each element in the vector
        for (int i: nums) {
            // If an element is 0, return 0 as the product of all elements will also be 0
            if (i == 0) {
                return 0;
            }
            // If an element is negative, flip the sign of the res variable
            if (i < 0) {
                res *= -1;
            }
        }
        // If the number of negative numbers is even, res will remain 1
        // Otherwise, if the number of negative numbers is odd, res will be -1
        return res;
    }
};