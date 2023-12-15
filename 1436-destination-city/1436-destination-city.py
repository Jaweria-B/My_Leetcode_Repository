class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        l = len(paths)
        s = set()
        
        # Populate set with starting cities
        for i in range(l):
            s.add(paths[i][0])
        
        # Check for the destination city not present in the starting cities
        for i in range(l):
            if paths[i][1] not in s:
                return paths[i][1]
        
        # If no destination city found
        return ""