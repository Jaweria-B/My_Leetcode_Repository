class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        for i in range(len(s)):
            res += self.countPalindrome(s, i, i)
            res += self.countPalindrome(s, i + 1, i)
        return res
    
    def countPalindrome(self, s, r , l):
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        return count