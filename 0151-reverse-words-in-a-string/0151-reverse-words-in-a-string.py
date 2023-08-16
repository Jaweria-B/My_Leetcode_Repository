class Solution:
    def reverseWords(self, s: str) -> str:
        trimmed_s = s.split()
        answer = ""
        
        for i in range(len(trimmed_s)-1, -1, -1):
            if i == 0:
                answer += trimmed_s[i]
            else:
                answer += trimmed_s[i] + " "
        
        return answer
        