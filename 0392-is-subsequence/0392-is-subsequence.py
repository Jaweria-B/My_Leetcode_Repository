class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1 = 0
        p2 = 0

        if(len(s) == 0):
            return True
        
        if(len(s) != 0 and len(t) == 0):
            return False

        while(p1 <= len(s)-1 and p2 <= len(t)-1 ):
            if(s[p1] == t[p2]):
                p1 += 1
                p2 += 1
            else:
                p2 += 1
                if( p2>= len(t)):
                    break
            
        return p1 == len(s)