class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        columns = len(board[0])

        def find(board, word, i, j):
            if len(word) == 0: 
                return True
            
            if i<0 or i >= rows or j<0 or j >= columns or board[i][j] != word[0] or board[i][j]==' ': 
                return False
            
            c = board[i][j]
            board[i][j] = ' '
            word = word[1:]
            up = find(board, word, i-1, j)
            down = find(board, word, i+1, j)
            left = find(board, word, i, j-1)
            right = find(board, word, i, j+1)
            res = up or down or left or right
            board[i][j] =c
            return res
        
        for r in range(rows):
            for c in range(columns):
                if (board[r][c] == word[0]) and find(board, word, r,c):
                    return True
                
        return False