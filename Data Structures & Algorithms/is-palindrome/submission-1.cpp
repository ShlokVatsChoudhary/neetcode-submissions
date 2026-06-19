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
        int l = x - 1;
        for(int i = 0; i<x/2; i++){
            if(ss[i] != ss[l]){
                return false;
            }
            l--;
        }
        return true;
    }
};
