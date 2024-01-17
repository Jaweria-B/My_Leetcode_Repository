class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurence = defaultdict(int)
        
        for i in arr:
            occurence[i] += 1
            
        return len(set(occurence.values())) == len(occurence)