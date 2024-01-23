class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        
        row = {
            'a': 0,
            'b': 1,
            'c': 2,
            'd': 3,
            'e': 4,
            'f': 5,
            'g': 6,
            'h': 7
        }
        
        x = row[coordinates[0]]
        y = int(coordinates[1])
        
        if (x == y) or (x % 2 == 0 and y % 2 == 0 ) or ((x + y) % 2 == 0):
            return True
        else:
            return False