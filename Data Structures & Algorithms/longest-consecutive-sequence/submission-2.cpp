class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if( nums.size()== 0) return 0;
        unordered_set<int> st(nums.begin(), nums.end());
        int lu = 1;
        int n = nums.size();
        for(int i = 0; i<n; i++){
            int curr = nums[i];
            if(st.find(curr-1) == st.end()){
            int lt = 1;
            
            while(st.find(curr+1) != st.end()){
                lt++;
                curr++;
            }
            lu = max(lu,lt);
            }
        }
        return lu;
    }
};
