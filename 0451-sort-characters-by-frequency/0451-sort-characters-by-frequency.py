class Solution:
    def frequencySort(self, s: str) -> str:
        count = defaultdict(int)
        
        for ch in s:
            count[ch] += 1
        
        count = sorted(count.items(), key=lambda x:x[1], reverse = True)
        
        ans = ""
        for key, value in count:
            ans += key * value
        
        return ans
            