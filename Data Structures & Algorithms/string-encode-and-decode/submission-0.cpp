class Solution {
public:

    string encode(vector<string>& strs) {
        string s = "";
        int n = strs.size();
        for(int i = 0; i<n; i++){
            s += to_string(strs[i].length());
            s += '#';
            s += strs[i];
        }
        return s;
    }

    vector<string> decode(string s) {
        vector<string> ss;
        int n = s.size();
        int i = 0;
        while(i < n){
            int pos = s.find('#', i);
            int len = stoi(s.substr(i, pos - i));
            i = pos + 1;
            ss.push_back(s.substr(i, len));
            i += len;
        }
        return ss;
    }
};