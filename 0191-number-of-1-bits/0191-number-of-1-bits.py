class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        m = str(bin(n)[2:])
        i = 0
        
        while i < len(m):
            if m[i] == '1':
                count += 1
            i += 1
                    
        return count