// https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

class Solution {
public:
    /*
    Time complexity: O(n), where n is the number of nodes in the binary tree, because each node is visited by the "rec" function only once.
    
    Space complexity: O(n), where n is the number of nodes in the binary tree, because the maximum depth of the recursive call stack is equal to
                      the height of the binary tree and the function uses a constant amount of extra space.
    */

    int res = 0; // Initialize result variable as 0


    /**
     * Recursive function to calculate the length of the longest zigzag path in a binary tree
     * @param node: Pointer to the current node
     * @param direction: String indicating the current direction ("right" or "left")
     * @param score: Current score of the zigzag path
     * @return: Length of the longest zigzag path
     */
    int rec(TreeNode* node, string direction, int score){
        // Base case: If node is null, update the result with the current score
        if(node == NULL){ 
            if(score > this->res){
                this->res = score;
            }
            return 0;
        }

        // Recursive case:
        // If current direction is "right", Explore the right subtree incrementing 1 the score and explore the left subtree resetting the score to 0
        if(direction == "right"){
            rec(node->right, "left", score + 1); // Explore right subtree with direction "left" and increment score
            rec(node->left, "right", 0); // Explore left subtree with direction "right" and reset score

        // If current direction is "left", Explore the left subtree incrementing 1 the score and explore the right subtree  resetting the score to 0
        } else {
            rec(node->right, "left", 0);
            rec(node->left, "right",  score + 1); 
        }
        return 0;
    }

    /**
     * Main function to calculate the length of the longest zigzag path in a binary tree
     * @param root: Pointer to the root of the binary tree
     * @return: Length of the longest zigzag path
     */
    int longestZigZag(TreeNode* root) {
        rec(root, "right", -1); // Start exploring from root with direction "right" and initial score -1
        rec(root, "left", -1);  // Start exploring from root with direction "left" and initial score -1
        
         // Return the final result
        return this->res;
    }
};