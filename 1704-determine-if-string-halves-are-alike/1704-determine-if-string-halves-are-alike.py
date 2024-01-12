class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        
        half = len(s) // 2
        
        firstHalf = self.countVowels( s[: half], vowels)
        secondHalf = self.countVowels( s[half:], vowels)
        
        if firstHalf == secondHalf:
            return True
        else:
            return False
        
    def countVowels(self, string, vowels):
        count = 0
        for ch in string:
            if ch in vowels:
                count += 1
        
        return count