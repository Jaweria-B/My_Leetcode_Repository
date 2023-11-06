class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        
        count = {}
        res = 0
        for d in dominoes:
            ans = min(d[0], d[1]) * 10 + max(d[0], d[1])
            if ans not in count:
                count[ans] = 1
            else:
                res += count[ans]
                count[ans] += 1
                
        return res