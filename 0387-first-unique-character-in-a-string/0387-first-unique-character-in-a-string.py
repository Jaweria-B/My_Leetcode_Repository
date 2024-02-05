class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(int)
        
        for c in s:
            count[c] += 1
        
        for ind, ch in enumerate(s):
            if count[ch] == 1:
                return ind
            
        return -1