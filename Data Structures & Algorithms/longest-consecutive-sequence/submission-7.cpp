class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int lu = 0;
        unordered_set<int> store(nums.begin(), nums.end());
        for (int num : nums) {
            int lt = 0, curr = num;
            while (store.find(curr) != store.end()) {
                lt++;
                curr++;
            }
            lu = max(lu, lt);
        }
        return lu;
    }
};