class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)
        for word in strs: 
           sorted_word = ''.join(sorted(word))
           anagram_groups[sorted_word].append(word)  
        return list(anagram_groups.values())
        