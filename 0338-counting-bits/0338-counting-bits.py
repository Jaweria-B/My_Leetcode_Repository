class Solution:
    def countBits(self, n: int) -> List[int]:
        t = [0] * (n+1)
        for i in range(1, n+1):
            t[i] = t[i >> 1] + (i & 1)
        return t            