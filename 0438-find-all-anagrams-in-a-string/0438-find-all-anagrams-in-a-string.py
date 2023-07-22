class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        sort_p = sorted(p)
        
        ans = []
        
        for i in range(len(s)-k+1):
            sort_win_substr = sorted(s[i:i+k])
            
            if sort_win_substr == sort_p:
                ans.append(i)
        return ans