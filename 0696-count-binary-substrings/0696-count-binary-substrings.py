class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        left = 0
        right = 0
        ans = 0
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                prev_char = s[i-1]
                curr_char = s[i]
                left = i-1
                right = i
                while left >= 0 and right < len(s) and s[left] == prev_char and s[right] == curr_char:
                    if s[left] != s[right]:
                        left -= 1
                        right += 1
                        ans += 1
                    else:
                        break
                        
        return ans
    