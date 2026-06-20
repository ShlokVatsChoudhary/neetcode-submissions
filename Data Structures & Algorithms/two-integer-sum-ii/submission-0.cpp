class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int l = 0;
        int n = nums.size();
        vector<int> v;
        int r = n - 1;
        while(l<r){
            if(nums[l]+nums[r]== target){
                v.push_back(l+1);
                v.push_back(r+1);
                break;
            }
            if(nums[l]+nums[r]<target){
                l++;
            }
            if(nums[l]+nums[r]>target){
                r--;
            }
        }
        return v;
    }
};
