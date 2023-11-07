class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def calculate(a):
            s = 0
            for i in range(len(a)):
                if(i-1 >= 0 and a[i-1] == 10) or (i-2 >= 0 and a[i-2] == 10):
                    s += (a[i]*2)
                else:
                    s += a[i]
            return s   

        score1 = calculate(player1)
        score2 = calculate(player2)
        
        if score1 > score2:
            return 1
        
        elif score1 < score2:
            return 2
        
        return 0