class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        result = ''
        lastSpaceIndex = -1
        
        for strIndex in range(n):
            if strIndex == n-1 or s[strIndex] == ' ':
                reverseStrIndex = strIndex if strIndex == n-1 else strIndex-1
                
                while reverseStrIndex > lastSpaceIndex:
                    result += s[reverseStrIndex]
                    reverseStrIndex -= 1
                    
                if strIndex != n-1:
                    result += ' '
                
                lastSpaceIndex = strIndex
                
        
        return result