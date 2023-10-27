class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        for ch in s:
            if ch in dic:
                dic[ch] += 1
            else:
                dic[ch] = 1
        
        ans = 0
        size = len(dic)
        for key, val in dic.items():
            if val%2 == 0:
                ans += val
                size -= 1
            else:
                ans += val-(val%2)
                dic[key] = val%2
                
        if size > 0:
            return ans + 1
        
        return ans