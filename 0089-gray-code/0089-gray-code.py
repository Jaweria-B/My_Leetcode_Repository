class Solution:
    def grayCode(self, n: int) -> List[int]:
        codes = [0]
        offset = 1
        for i in range(n):
            for j in range(len(codes)-1, -1, -1):
                codes.append(codes[j]+offset)
            offset = offset << 1
        return codes
    
        