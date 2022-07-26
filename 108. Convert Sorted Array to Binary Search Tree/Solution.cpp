// https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {

        int middle = nums.size() / 2;
        TreeNode* root = new TreeNode(nums[middle]);
        vector<int> l(nums.begin(), nums.begin() + middle);
        vector<int> r(nums.begin() + middle + 1, nums.end());
        if (!l.empty()) {
            root->left = sortedArrayToBST(l);
        }
        if (!r.empty()) {
             root->right = sortedArrayToBST(r);
        }
       
        return root;
    }
};