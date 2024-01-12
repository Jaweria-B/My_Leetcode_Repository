class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        
        def countVowels(string):
            count = 0
            for ch in string:
                if ch in vowels:
                    count += 1

            return count
        
        half = len(s) // 2
        
        firstHalf = countVowels( s[: half])
        secondHalf = countVowels( s[half:])
        
        if firstHalf == secondHalf:
            return True
        else:
            return False
        
    