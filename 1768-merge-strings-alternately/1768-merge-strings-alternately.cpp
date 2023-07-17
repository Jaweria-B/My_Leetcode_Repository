class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string res = "";
        int p1 = 0, p2 = 0;

        while(p1<word1.size() && p2<word2.size()){
            res = res + word1[p1] + word2[p2];
            p1++;
            p2++;
        }

        return p1 == word1.size()? res+word2.substr(p2, word2.size()-p2): res+word1.substr(p1, word1.size()-p1);
        
    }
};