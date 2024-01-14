class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        wrd1_frq = Counter(word1)
        wrd2_frq = Counter(word2)
        
        keys_match = set(wrd1_frq.keys()) == set(wrd2_frq.keys())
        
        return sorted(wrd1_frq.values()) == sorted(wrd2_frq.values()) and keys_match