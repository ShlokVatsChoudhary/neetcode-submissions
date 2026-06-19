#include <numeric>
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int left = 1;
        int n = nums.size();
        vector<int>nnn(n,1); 
        for(int i = 0; i<n; i++){
            nnn[i] = left;
            left *= nums[i];
        }
        left = 1;
        for(int i = n-1; i>=0; i--){
            nnn[i] *= left;
            left *= nums[i];
        }
        return nnn;
    }
};
