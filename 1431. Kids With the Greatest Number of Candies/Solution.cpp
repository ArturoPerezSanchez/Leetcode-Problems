// https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
class Solution {
public:
    /*
    Time complexity: The code performs a single pass through the input list of candies to find the maximum value, which takes O(n) time.
                     Then, it performs another pass through the same list to generate the output list of Boolean values, which also takes O(n) time.
                     Therefore, the overall time complexity of the code is O(n).

    Space complexity: The code creates a single list of Boolean values, which has the same length as the input list of candies.
                      Therefore, the space complexity of the code is O(n).
    */
	vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
		// create a boolean vector, the same size as candies vector to store the results
		vector<bool> ans(candies.size());
		
		// initialize a variable to store the biggest number of candies
		int biggest = 0;

		// loop through the candies vector and update the biggest variable to store the highest number of candies
		int i;
		for (i = 0; i < candies.size(); i++){
			if(candies[i] > biggest){
				biggest = candies[i];
			}
		}

		// subtract extraCandies from the biggest variable to get the threshold value
		biggest -= extraCandies;

		// loop through the candies vector again and set the corresponding index in the boolean vector to true if that child has enough candies to match or exceed the threshold value
		for (i = 0; i < candies.size(); i++){
			if(candies[i] >= biggest){
				ans[i] = true;
			}
		}

		// return the boolean vector
		return ans;
	}
};