class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def checkIfCanEqual(word, query):
            toCorrect = 0
            for j in range(len(word)):
                if word[j] != query[j]:
                    toCorrect += 1
            
            return toCorrect
        
        ans = []
        for query in queries:
            if query in dictionary:
                ans.append(query)
            
            else:
                for j in range(len(dictionary)):
                    c = checkIfCanEqual(dictionary[j], query)
                    if c <= 2:
                        ans.append(query)
                        break
                    else:
                        continue
        return ans