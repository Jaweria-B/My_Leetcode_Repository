class Solution:
    def sortVowels(self, s: str) -> str:
        
        def isVowel(c):
            return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U'
        
        temp = []
        
        for c in s:
            if isVowel(c):
                temp += (c)
        
        temp.sort()
        
        ans = ""
        
        j = 0
        
        for ch in range(len(s)):
            
            if isVowel(s[ch]):
                print(temp[j])
                ans += temp[j]
                j += 1
            else:
                ans += s[ch]
                
        return ans