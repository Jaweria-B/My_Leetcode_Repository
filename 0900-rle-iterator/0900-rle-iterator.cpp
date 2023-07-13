class RLEIterator {
    vector<int> data;
    int cur_idx = 0;
public:
    RLEIterator(vector<int>& encoding) {
        data = encoding;
    }
    
    int next(int n) {
        if(cur_idx >= data.size())  return -1;

        if(data[cur_idx] >= n){
            data[cur_idx] -= n;

            int val = data[cur_idx+1];
            while(cur_idx < data.size() && data[cur_idx] == 0)  cur_idx += 2;
            return val;
        }
        else{
            n -= data[cur_idx];
            cur_idx += 2;
            return next(n);
        }
    }
};

/**
 * Your RLEIterator object will be instantiated and called as such:
 * RLEIterator* obj = new RLEIterator(encoding);
 * int param_1 = obj->next(n);
 */