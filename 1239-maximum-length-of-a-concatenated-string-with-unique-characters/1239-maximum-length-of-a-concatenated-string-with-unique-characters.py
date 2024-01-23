class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        charSet = set()
        
        def overLap(charSet, string):
            c = Counter(charSet) + Counter(string)
            return max(c.values()) > 1
        
        def backtracking(i):
            if i == len(arr):
                return len(charSet)
            
            res = 0
            
            if not overLap(charSet, arr[i]):
                for ch in arr[i]:
                    charSet.add(ch)
                res =  backtracking(i + 1)
                
                for ch in arr[i]:
                    charSet.remove(ch)
                
            return max(res, backtracking(i + 1))
            
        return backtracking(0)