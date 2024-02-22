class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = defaultdict(int)
        outgoing = defaultdict(int)
        
        for p1, p2 in trust:
            outgoing[p1] += 1
            incoming[p2] += 1
        
        for i in range(1, n + 1):
            if outgoing[i] == 0 and incoming[i] == n - 1:
                return i
            
        return -1 