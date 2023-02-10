# https://leetcode.com/problems/simplify-path

class Solution {
public:
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

