class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        length = len(words)
        
        chars = [0] * 26
        
        for word in words:
            for ch in word:
                chars[ord(ch) - ord('a')] +=  1
        
    
        for char in chars:
            if char % length != 0:
                return False
        
        return True
                