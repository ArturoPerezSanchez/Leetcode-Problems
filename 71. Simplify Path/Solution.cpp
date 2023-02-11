# https://leetcode.com/problems/simplify-path

class Solution {
public:
    /*
        Time complexity: O(n), where n is the length of the input path string. This is because the code iterates over each character in the input string exactly
                               once to extract the individual path segments, and then loops over each segment in the simplified path to construct the final string.

        Space complexity: O(n), where n is the length of the input path string. This is because the code creates a vector of strings to store the intermediate path segments 
                                which could potentially be as large as the input string itself in the case where every character represents a new directory.
                                The space required for other variables like the stringstream, segment, and res is at most equal to n so space complexity can still be described as O(n).
    */
    string simplifyPath(string path) {

        // Initialize a stringstream object with the input string.
        stringstream pathstream(path);

        // String variable to store the current segment of the path being processed.
        string segment;

        // Vector of strings to store the simplified path segments.
        vector<string> l;

        // String variable to store the final simplified path.
        string res = "";

        // Loop through each segment of the input path using the getline function.
        while(getline(pathstream, segment, '/')) {

            // Ignore empty and current directory segments.
            if(segment != "" && segment != ".") {

                // if the segment its for parent directory, remove the last element from the simplified path vector.
                if(segment == "..") {
                    if (l.size() > 0) {
                        l.pop_back();
                    }
                } else {
                    // Otherwise add the segment to the vector
                    l.push_back(segment);
                }
            }
        }

        // Construct the final simplified path string by joining the simplified path segments with forward slashes.
        for(int i = 0; i < l.size(); i++) {
            res += '/' + l[i];
        }

        // If the final simplified path is empty, return the root directory.
        if (res == ""){
            return "/";
        }

        // Return the final simplified path string.
        return res;
    }
};

