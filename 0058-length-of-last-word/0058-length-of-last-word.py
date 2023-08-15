class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        flag = False
        count = 0
        
        for i in range(n-1, -1, -1):
            
            if s[i] == " " and flag == True:
                break
            elif s[i] != " ":
                flag = True
                count += 1
        
        return count