class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> st(nums.begin(), nums.end());
        int longest = 0;

        for (int num : nums) {
            // Only start from the beginning of a sequence
            if (st.find(num - 1) == st.end()) {
                int length = 1;
                int curr = num;

                while (st.find(curr + 1) != st.end()) {
                    curr++;
                    length++;
                }

                longest = max(longest, length);
            }
        }

        return longest;
    }
};