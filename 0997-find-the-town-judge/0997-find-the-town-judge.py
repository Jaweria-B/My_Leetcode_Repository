class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        delta = defaultdict(int)
        
        for p1, p2 in trust:
            delta[p1] -= 1
            delta[p2] += 1
        
        for i in range(1, n + 1):
            if delta[i] == n - 1:
                return i
            
        return -1 