class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if( nums.size()== 0) return 0;
        unordered_set<int> st(nums.begin(), nums.end());
        int lu = 1;
        int n = nums.size();
        for(int i = 0; i<n; i++){
            int curr = nums[i];
            int lt = 1;
            while(st.find(curr-1) != st.end()){
                lt++;
                curr--;
            }
            if(lt>lu) lu = lt;
        }
        return lu;
    }
};
