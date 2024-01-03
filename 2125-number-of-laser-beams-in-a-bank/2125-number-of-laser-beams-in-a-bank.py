class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        row_count = [0] * (len(bank) + 1)
        
        for i in range(len(bank)):
            for j in range(len(bank[0])):
                if bank[i][j] == '1':
                    row_count[i] += 1
        
        total = 0
        
        for r in range(len(row_count)):
            if r == len(row_count) - 1:
                continue
            else:
                pointer = r + 1
                while pointer  <  len(row_count) - 1 and row_count[pointer] == 0  :
                    pointer += 1
                total += row_count[r] * row_count[pointer]
        
        return total