class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits) == 1:
            return True
        
        i = 0
        while i < len(bits):            
            if bits[i] == 1:
                i += 2  
            else:
                i += 1
                
            if i == len(bits)-1:
                return True
        
        return False