class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoded = encoding[:]
        

    def next(self, n: int) -> int:
        
        count = 0
        
        while count < n:
            if self.encoded:
                no_of_times = self.encoded.pop(0)
                element = self.encoded.pop(0)
                
                count += no_of_times
            else:
                return -1
        
        if count > n:
            self.encoded.insert(0, element)
            self.encoded.insert(0, count-n)
        
        return element
# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)