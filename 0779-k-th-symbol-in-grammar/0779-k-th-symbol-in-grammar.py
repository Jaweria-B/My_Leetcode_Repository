class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        curr, l, r = 0, 1, 2 ** (n - 1)

        for __ in range(n - 1):
            m = l + (r - l) // 2

            if m >= k:
                r = m
            elif m < k:
                l = m + 1
                curr = 0 if curr == 1 else 1
            
        return curr