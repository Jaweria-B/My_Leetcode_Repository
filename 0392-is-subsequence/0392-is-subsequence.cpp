class Solution {
public:
    bool isSubsequence(string s, string t) {
        int p1 = 0, p2 = 0;

        if(s.size() == 0)   return true;

        while(p1 <= s.size()-1){
            if(s[p1] == t[p2]){
                p1++;
                p2++;
            }
            else{
                p2++;
                if(p2>= t.size())   break;
            }
        }
        return p1 == s.size();
    }
};