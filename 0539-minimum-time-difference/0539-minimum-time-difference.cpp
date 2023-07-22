class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {
     vector<int> data;
        int time_24h = 24*60;

        for(string time:timePoints){
            int time_min = stoi(time.substr(0, 2))*60+ stoi(time.substr(3, 2));
            data.push_back(time_min);
        }
        sort(data.begin(), data.end());

        int minDiff = INT_MAX;

        int prev = data[data.size()-1];
        for(int i=0; i<data.size(); i++){
            int diff = abs(data[i]- prev);
            minDiff = min(minDiff, min(diff, abs(time_24h - diff)));
            prev = data[i];
        }
        return minDiff;   
    }
};