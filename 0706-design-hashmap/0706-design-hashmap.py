class MyHashMap:

    def __init__(self):
        self.dic = {}

    def put(self, key: int, value: int) -> None:
        self.dic[key] = value

    def get(self, key: int) -> int:
        if key in self.dic:
            return self.dic[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.dic:
            self.dic.pop(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)