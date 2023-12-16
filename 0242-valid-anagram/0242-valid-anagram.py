class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = [0] * 26
        for ch in s:
            s_list[ord(ch) - ord('a')] += 1
            
        t_list = [0] * 26
        for ch in t:            
            t_list[ord(ch) - ord('a')] += 1
            

        
        return s_list == t_list
                