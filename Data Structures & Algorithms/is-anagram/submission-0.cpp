class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()) return false;

        int arr1[26] = {};
        int arr2[26] = {};
        int n = s.size();
        for(int i = 0; i<n; i++){
            arr1[s[i] - 'a']++;
            arr2[t[i] - 'a']++;
        }
        for(int i = 0; i < 26; i++){
        if(arr1[i] != arr2[i]) return false;
    }
    return true;
    }
};
