class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        l = 0
        r = len(tokens)-1
        ans = 0
        while l <= r:
            if tokens[l] <= power:
                score += 1
                power -= tokens[l]
                ans = max(ans, score)
                l += 1
                
            elif score > 0:
                power += tokens[r]
                r -= 1
                score -= 1
            
            else:
                return ans
        
        return ans