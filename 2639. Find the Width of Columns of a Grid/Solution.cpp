// https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/

class Solution {
    /*
    Time complexity: O(m*n), The function loops through each element in the grid once, so the time complexity of this function is O(m*n),
                 where m is the number of rows in the grid and n is the number of columns in the grid.


    Space complexity: O(n), To keep track of the maximum length of integers in each column, the function uses a list of length equal to the number of columns in the grid.
    */
    // Solution counting the the length of the numbers converting it to string first
    public:
        vector<int> findColumnWidth(vector<vector<int>>& grid) {
            vector<int> ans(grid[0].size());
            
            // loop through each row and column in the input grid
            for (int r = 0; r<grid.size(); r ++){
                for (int c = 0; c<grid[0].size(); c++){
                    // update the answer vector at index c with the maximum length of a number in column c
                    ans[c] = max(ans[c], (int) to_string(grid[r][c]).length());
                }
            }

            // return the answer vector
            return ans;
        }
    };
