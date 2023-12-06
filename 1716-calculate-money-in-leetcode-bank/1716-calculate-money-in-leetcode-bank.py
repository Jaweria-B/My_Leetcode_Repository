class Solution:
    def totalMoney(self, n: int) -> int:
        k = n // 7
        first_element = 28
        last_element = first_element + (k - 1) * 7
        
        arith_seq = k * ( first_element + last_element ) // 2
        
        monday = k + 1
        last_week_sum = 0
        
        for day in range(n % 7):
            last_week_sum += monday + day
            
        total_sum = arith_seq + last_week_sum
        
        return total_sum