class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left = 0;
        int n = heights.size();
        int right = n - 1;
        int vol = (right - left)*(min(heights[right],heights[left]));

        while(left<right){
            int tvol = (right - left)*(min(heights[right],heights[left]));
            if(heights[left]<=heights[right]) left++;
            else right--;
            vol = max(vol,tvol);
        }
        return vol;
    }
};
