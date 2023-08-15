class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        count = 0
        
        for i in range(n-1, -1, -1):
            if count == 0 and s[i] == " ":
                continue
            elif s[i] != " ":
                count += 1
            elif count != 0 and s[i] == " ":
                break
        
        return count
        