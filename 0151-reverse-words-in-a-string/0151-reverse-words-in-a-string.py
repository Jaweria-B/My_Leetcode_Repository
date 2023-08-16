class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        flag = False
        ans = ""
        
        for i in range(n-1, -1, -1):
            if s[i] == " " and flag == False:
                s = s[:i]
                continue
            if s[i] != " ":
                flag = True
            
            if s[i] == " " and flag:
                ans += s[i+1 : len(s)] + " "         
                s = s[0 : i]
                
                if ans[-2] == " ":
                    ans = ans[:len(ans)-1]
        if s:
            ans += s
        return ans[:len(ans) -1] if ans[-1] == " " else ans