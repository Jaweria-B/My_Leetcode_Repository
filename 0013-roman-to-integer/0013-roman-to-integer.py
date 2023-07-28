class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_disc = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D":500,
            "M": 1000
        }
        
        ans = 0
        for i in range(len(s)):
            if i+1 < len(s) and roman_disc[s[i]] < roman_disc[s[i+1]]:
                ans -= roman_disc[s[i]]
            else:
                ans += roman_disc[s[i]]
                
        return ans