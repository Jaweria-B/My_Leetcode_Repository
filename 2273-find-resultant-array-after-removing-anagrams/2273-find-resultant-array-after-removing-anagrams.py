class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        
        ans = [words[0]]
        
        for i in range(1, len(words)):
            dict1 = Counter(ans[-1])
            
            dict2 = Counter(words[i])
            
            if dict1 == dict2:
                continue
            else:
                ans.append(words[i])
        
        return ans