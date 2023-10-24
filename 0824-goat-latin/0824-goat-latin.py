class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        splitted = sentence.split(" ")
        
        ans = ""
        
        c = 1
        for w in splitted:
            temp = ""
            if w[0] in "aeiouAEIOU":
                temp = w + "ma"
                
            elif w[0] not in "aeiouAEIOU":
                temp = w[1:] + w[0] + "ma"
            
            temp = temp + "a"*c + " "
            c += 1
            ans += temp
        
        return ans[0:-1]