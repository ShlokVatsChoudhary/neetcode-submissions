class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()) return false;

        int arr1[26] = {};
        int n = s.size();
        for(char x : s){
            arr1[x - 'a']++;
        }
        for(char x : t){
        if(--arr1[x-'a'] < 0) return false;
    }
    return true;
    }
};
