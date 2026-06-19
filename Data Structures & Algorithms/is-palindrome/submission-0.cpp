class Solution {
public:
    bool isPalindrome(string s) {
        string ss;
        for(char x: s){
            if(isalnum(x)){
                ss.push_back(tolower(x));
            }
        }
        int x = ss.size();
        for(int i = 0; i<x/2; i++){
            if(ss[i] != ss[x-i-1]){
                return false;
            }
        }
        return true;
    }
};
