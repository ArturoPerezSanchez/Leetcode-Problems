// https://leetcode.com/problems/number-of-zero-filled-subarrays

class Solution {
public:
    long long zeroFilledSubarray(vector<int>& nums) {
        int res = 0;
        long counter = 0;
        long currentsum = 0;

        for (int i : nums) {
            if(i == 0){
                counter +=1;
                currentsum += counter;
            } else {
                res+=currentsum;
                currentsum = 0;
                counter = 0;
            }
        }
        return res+currentsum;

    }
};