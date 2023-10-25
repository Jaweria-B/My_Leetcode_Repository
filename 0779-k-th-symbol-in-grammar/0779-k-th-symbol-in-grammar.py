class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        def depthFirstSearch(n: int, k: int, rootVal: int) -> int:
            
            if n == 1:
                return rootVal
        
            totalNodes = 2 ** (n - 1)

            # Target node is in right half ?
            
            if k > (totalNodes / 2):
                
                nextRootVal = 1 if rootVal == 0 else 0
                return depthFirstSearch(n - 1, k - (totalNodes / 2), nextRootVal)
            
            # Target node is in left half ?
            
            else:
                
                nextRootVal = 0 if rootVal == 0 else 1
                return depthFirstSearch(n - 1, k, nextRootVal)
            
        return depthFirstSearch(n, k, 0)