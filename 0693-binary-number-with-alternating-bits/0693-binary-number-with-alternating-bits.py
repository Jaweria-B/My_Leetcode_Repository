class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary = bin(n)[2: ]
        
        firstEle = binary[0]
        
        for i in range(1, len(binary)):
            if binary[i] != firstEle:
                firstEle = binary[i]
            else:
                return False
        
        return True