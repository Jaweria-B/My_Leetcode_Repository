class Solution {
public:
    vector<int> diffWaysToCompute(string input) {
        vector<int> res;  // equal to this { } symbol functionality
        for(int i=0; i<input.length(); i++){
            if(input[i]=='+'||input[i]=='-'||input[i]=='*'){
                vector<int> left = diffWaysToCompute(input.substr(0,i));    //divide to two parts 
                vector<int> right = diffWaysToCompute(input.substr(i+1));
                for(int j=0; j<left.size(); j++){
                    for(int k=0; k<right.size(); k++){
                        if(input[i] == '+'){
                            res.push_back(left[j]+right[k]);
                        }
                        else if(input[i] == '-'){
                            res.push_back(left[j]-right[k]);
                        }
                        else{
                            res.push_back(left[j]*right[k]);
                        }
                    }
                }
            }
        }
        if(res.empty()){  //if input only has one number character ex. f(5)
            res.push_back(stoi(input));
        }
        return res;
    }
};