# Last updated: 8/20/2026, 2:15:27 AM
class MyStack:

    def __init__(self):
        self.inqueue, self.outqueue = deque(), deque()
        
    def push(self, x: int) -> None:
        self.inqueue.append(x)
        

    def pop(self) -> int:
        while len(self.inqueue) > 1:
            self.outqueue.append(self.inqueue.popleft())

        popped = self.inqueue.popleft()

        while self.outqueue:
            self.inqueue.append(self.outqueue.popleft())
        
        return popped
        

    def top(self) -> int:
        return self.inqueue[-1]
        

    def empty(self) -> bool:
        return not self.inqueue and not self.outqueue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()