// https://leetcode.com/problems/maximum-width-of-binary-tree/

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
	/*
		Time complexity: O(N), where N is the number of nodes in the binary tree, because each node is visited once.

		Space complexity: O(M), where M is the maximum number of nodes that can be present at a single level in the binary tree. This is because, at most, all the nodes at the maximum level can be stored in the "level" deque at the same time.
	*/
    int widthOfBinaryTree(TreeNode* root) {
        // Create a deque to store nodes at each level along with their corresponding index
        deque<tuple<TreeNode*,long long>> level;
        level.push_back({root, 1});

        // Initialize the result variable to store the maximum width of the binary tree
        int res = 0;

        // Continue processing levels until there are no more nodes
        while (!level.empty()){
            // Create a new deque to store nodes at the next level
            deque<tuple<TreeNode*,long long>> newlevel;

            // Calculate the width of the current level by subtracting the index of the first node
            // from the index of the last node, and update the result if necessary
            if(get<1>(level.back()) - get<1>(level.front()) + 1 > res){
                res = get<1>(level.back()) - get<1>(level.front()) + 1;
            }

            // Process nodes at the current level
            while (!level.empty()){
                // Get the current node and its index
                TreeNode* current_node = get<0>(level.front());
                int ind = get<1>(level.front());
                level.pop_front();

                // Add the left child of the current node to the newlevel deque, along with its updated index
                if(current_node->left != NULL){
                    newlevel.push_back({current_node->left, (long long) 2*ind});
                }

                // Add the right child of the current node to the newlevel deque, along with its updated index
                if(current_node->right != NULL){
                    newlevel.push_back({current_node->right, (long long) 2*ind + 1});
                }
            }

            // Update the level deque with the nodes at the next level
            level = newlevel;
        }

        // Return the maximum width of the binary tree
        return res;
    }
};
