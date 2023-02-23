// https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/

class Solution{
    /*
    Time complexity: O(m*n), The function loops through each element in the grid once, so the time complexity of this function is O(m*n),
                 where m is the number of rows in the grid and n is the number of columns in the grid.


    Space complexity: O(n), To keep track of the maximum length of integers in each column, the function uses a list of length equal to the number of columns in the grid.
    */
    // Solution using a custom function to get the length of the number instead of converting it to string
    public:
        vector<int> findColumnWidth(vector<vector<int>>& grid) {
            vector<int> ans(grid[0].size());

            // loop through each row and column in the input grid
            for (int r = 0; r<grid.size(); r ++){
                for (int c = 0; c<grid[0].size(); c++){
                     // update the answer vector at index c with the maximum length of a number in column c
                ans[c] = max(ans[c], len(grid[r][c]));
                }
            }
            return ans;
        }

        // Auxiliar function to get the length of a number, the function counts the necesary divisions by 10
        // necesary until the number length is only 1 digit, then add 1 if the number is negative
        int len(int num){
            int counter = 1;
            if(num<0){
                num = -num;
                counter++;
            }
            while (num>9){
                num /= 10;
                counter++;
            }

        return counter;
        }
    };
