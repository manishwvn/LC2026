# Last updated: 8/20/2026, 2:13:52 AM
class MovingAverage:

    def __init__(self, size: int):
        self.nums = deque()
        self.size = size
        self.sum_ = 0
        self.count = 0
        
    def next(self, val: int) -> float:
        self.nums.append(val)
        self.count += 1

        tail = 0
        if self.count > self.size:
            tail = self.nums.popleft()

        self.sum_ += val - tail 
        div = min(self.count, self.size)

        return self.sum_ / div

        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)