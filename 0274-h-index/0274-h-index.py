class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations.sort()
        n = len(citations)
        h = 0
        
        if n==1 and citations[0] == 0:
            return 0
        
        else:
            for i in range(n):
                if citations[i] < n-i:
                    h = citations[i]
                else:
                    h = max(h, n-i)
           
        return h