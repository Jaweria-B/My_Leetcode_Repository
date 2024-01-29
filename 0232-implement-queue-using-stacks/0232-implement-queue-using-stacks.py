class MyQueue:

    def __init__(self):
        self.stack = []
        # self.start = 0
        

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        top = self.stack.pop(0)
        return top
        

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        if not self.stack:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()