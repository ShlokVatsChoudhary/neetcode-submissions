class Solution {
public:
    vector<int> stringtoArray(std::string s) {
    std::vector<int> freq(26, 0); 
    for (char x : s) {
        freq[x - 'a']++;
    }
    return freq;
    }
    vector<vector<string>> groupAnagrams(vector<string>& str) {
        vector<vector<string>> kkk;
        map<vector<int>,vector<string>> mp;
        int n = str.size();
        for(string x : str){
            vector<int> arr1 = stringtoArray(x);
            mp[arr1].push_back(x);
        }
        for(const auto& [key,values]: mp){
            kkk.push_back(values);
        }
        return kkk;
    }
};
