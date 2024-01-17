class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurence = defaultdict(int)
        
        for i in arr:
            occurence[i] += 1
            
        unique = set()
        
        for val in occurence.values():
            if val in unique:
                return False
            unique.add(val)
            
        return True