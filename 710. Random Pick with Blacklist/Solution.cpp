// https://leetcode.com/problems/random-pick-with-blacklist

class Solution {
    vector<int> v;
    std::random_device rd;
    int mod;
public:
    Solution(int N, vector<int> blacklist) {
        mod = N - blacklist.size();
        sort(blacklist.begin(), blacklist.end());
        v = blacklist;
        v.push_back(N);
        for (int i = 0; i < v.size(); i++) v[i] -= i;
    }
    
    int pick() {
        int index = rd() % mod;
        auto it = upper_bound(v.begin(), v.end(), index);
        return index + (it - v.begin());
    }
};