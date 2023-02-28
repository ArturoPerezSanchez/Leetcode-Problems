// https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/

class Solution {
    /*
    Time Complexity: O(n), where n is the length of the input list. There is a single for loop that iterates through each element in the input list once,
                     Within the loop, there is only constant time operations like accessing elements in a list, comparing values, and appending to a list.

    
    Space Complexity: O(n), where n is the length of the input list. The function uses constant space for storing the current maximum value (currentmax) and a few integer
                      variables used within the for loop. The size of the result list is equal to the length of the input list, so the space complexity of the code is O(n).
    */
    public:
        vector<long long> findPrefixScore(vector<int>& nums) {
            // Initialize the current maximum value to the first number in the input vector.
            int currentmax = nums[0];
            
            // Initialize the result vector with the first element twice the value of the first number in the input vector.
            vector<long long> ans(nums.size());
            ans[0] = 2*currentmax;
            
            // Loop through the remaining elements in the input vector.
            for (int i=1; i<nums.size(); i++){
                // Get the current number from the input vector.
                int val = nums[i];
                
                // Update the current maximum value if the current number is greater than the current maximum.
                if (val > currentmax){
                    currentmax = val;
                }
                
                // Compute the score for the current number using the formula and add it to the result vector.
                // The score is the sum of the current number, the current maximum, and the previous score in the result vector.
                ans[i] = val + currentmax + ans[i-1];
            }
            
            // Return the result vector.
            return ans;
        }
    };
