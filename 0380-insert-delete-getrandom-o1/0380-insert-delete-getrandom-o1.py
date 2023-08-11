class RandomizedSet:

    def __init__(self):
        
        self.toIndex = {}
        self.nums = collections.deque() 

    def insert(self, val: int) -> bool:
        
        if val in self.toIndex:
            return False
        else:
            self.nums.append(val)
            self.toIndex[val] = len(self.nums) - 1
            return True
        

    def remove(self, val: int) -> bool:
        
        if val not in self.toIndex:
            return False
        else:
            oldIndex , numAtEnd = self.toIndex[val] , self.nums[-1]
            self.nums[oldIndex], self.nums[-1] = self.nums[-1] , self.nums[oldIndex]
            self.toIndex[numAtEnd] = oldIndex
            
            self.nums.pop()
            del self.toIndex[val]
            
            return True

    def getRandom(self) -> int:
        
        n = len(self.nums)
        
        randInd = random.randrange(0, n)
        
        return self.nums[randInd]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()