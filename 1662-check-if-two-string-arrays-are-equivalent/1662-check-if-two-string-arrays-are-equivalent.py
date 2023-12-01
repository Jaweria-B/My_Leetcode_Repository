class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        def makeAString(word):
            string = ""
            for w in word:
                string += w
            return string
        
        return makeAString(word1) == makeAString(word2)
            