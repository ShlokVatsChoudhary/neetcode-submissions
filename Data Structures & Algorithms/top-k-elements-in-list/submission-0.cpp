class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> mp;
        vector<int> v;
        for(int x : nums){
            mp[x]++;
        }
        int maxv = 0;
        int maxk = 0;
        while(k>0){
        for(const auto& [key,value] : mp){
            if(value>maxv){
                maxk = key;
                maxv = value;
            }
        }
        v.push_back(maxk);
        mp.erase(maxk);
        maxv = 0;
        maxk = 0;
        k--;
        }
        return v;
    }
};
