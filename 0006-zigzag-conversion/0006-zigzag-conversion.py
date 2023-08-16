class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ""
        unit = numRows *2 - 2
        
        if numRows == 1:
            return s
        
        for r in range(numRows):
            for n in range(len(s)):
                if r == 0 or r == numRows - 1:
                    if unit * n + r < len(s):
                        res += s[unit * n + r]
                else:
                    if unit * n + r < len(s):
                        res += s[unit * n + r]
                    if unit * n + unit - r < len(s):
                        res += s[unit * n + unit - r]
        return res