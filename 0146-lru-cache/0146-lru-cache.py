class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.m = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def deleteNode(self, p):
        p.prev.next = p.next
        p.next.prev = p.prev
    
    def addNode(self, newNode):
        temp = self.head.next
        self.head.next = newNode
        newNode.prev = self.head
        newNode.next = temp
        temp.prev = newNode
        
    def get(self, key: int) -> int:
        if key not in self.m:
            return -1
        
        p = self.m[key]
        self.deleteNode(p)
        self.addNode(p)
        self.m[key] = self.head.next
        
        return self.head.next.val
    
    def put(self, key: int, value: int) -> None:
        if key in self.m:
            c = self.m[key]
            self.deleteNode(c)
            c.val = value
            self.addNode(c)
            self.m[key] = self.head.next
        else:
            if len(self.m) == self.size:
                prev = self.tail.prev
                self.deleteNode(prev)
                l = Node(key, value)
                self.addNode(l)
                del self.m[prev.key]
                self.m[key] = self.head.next
            else:
                l = Node(key, value)
                self.addNode(l)
                self.m[key] = self.head.next
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)