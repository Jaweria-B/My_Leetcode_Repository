class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurence = defaultdict(int)
        
        for i in arr:
            occurence[i] += 1
            
        if len(set(occurence.values())) == len(occurence):
            return True
        
        return False