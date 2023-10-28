class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        MOD = 10 ** 9 + 7
        
        countA = 1
        countE = 1
        countI = 1
        countO = 1
        countU = 1
        
        for i in range(1, n):
            
            nextCountA = countE
            nextCountE = (countA + countI) % MOD
            nextCountI = (countA + countE + countO + countU) % MOD
            nextCountO = (countI + countU) % MOD
            nextCountU = countA
            
            countA = nextCountA
            countE = nextCountE
            countI = nextCountI
            countO = nextCountO
            countU = nextCountU
            
        totalCount = (countA + countE + countI + countO + countU) % MOD
        
        return int(totalCount)