class Solution {
public:
    int compress(vector<char>& chars) {
        int j = 0;

        if(chars.size() == 1)   return 1;


        int count;
        char cur_char;

        bool flag = false;

        for(int i=0; i<chars.size()-1; i++){

            count = 1;
            cur_char = chars[i];
            
            while(i<chars.size()-1 && chars[i] == chars[i+1]) {
                count++;
                i++;
            }
            if(i+1 == chars.size()-1 && chars[i] != chars[i+1]) flag = true;

            if(count == 1){
                chars[j] = cur_char;
                j++;
                continue;
            }
            
            chars[j] = cur_char;
            j++;

            string count_str = to_string(count);

            for(int k=0; k<count_str.size(); k++){
                chars[j++] = count_str[k];
            }
        }
        if(flag) chars[j++] = chars[chars.size()-1];

        return j;
    }
};