// https://leetcode.com/problems/find-anagram-mappings

class Solution {
public:
    vector<int> anagramMappings(vector<int>& nums1, vector<int>& nums2) {
        // Create a map that maps integer keys to integer values
        map<int, int> hm;
        // Create a vector to store the results
        vector<int> res;
        // Initialize a counter variable i to 0
        int i = 0;

        // Loop through all the elements in nums2
        while(i < nums2.size()) {
            // Add an entry to the map with the key as the element and the value as its index in nums2
            hm[nums2[i]] = i;
            i++; // Increment the counter variable
        }

        // Loop through all the elements in nums1
        for(int j=0; j < nums1.size(); j++){
            // Add to the results vector the value in the map corresponding to the key in nums1
            res.push_back(hm[nums1[j]]);
        }

        return res; // Return the results vector
    }
};