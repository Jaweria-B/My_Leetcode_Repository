class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True

        def backtrack(start, path):
            if start == n:
                result.append(path[:])
                return
            for end in range(start, n):
                if dp[start][end]:
                    backtrack(end + 1, path + [s[start:end+1]])

        result = []
        backtrack(0, [])
        return result