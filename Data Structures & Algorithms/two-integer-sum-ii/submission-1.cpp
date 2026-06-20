class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int l = 0;
        int n = nums.size();
        vector<int> v;
        int r = n - 1;
        while(l<r){
            int curr = nums[l]+nums[r];
            if(curr == target){
                v.push_back(l+1);
                v.push_back(r+1);
                break;
            }
            if(curr<target){
                l++;
            }
            if(curr>target){
                r--;
            }
        }
        return v;
    }
};
