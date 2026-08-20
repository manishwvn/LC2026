# Last updated: 8/20/2026, 2:07:39 AM
class FreqStack:

    def __init__(self):
        self.counts = {}
        self.stacks = {}
        self.max_count = 0
        

    def push(self, val: int) -> None:
        val_count = 1 + self.counts.get(val, 0)
        self.counts[val] = val_count
        
        if val_count > self.max_count:
            self.max_count = val_count
            self.stacks[val_count] = []
            
        self.stacks[val_count].append(val)

    def pop(self) -> int:
        res = self.stacks[self.max_count].pop()
        self.counts[res] -= 1
        
        if not self.stacks[self.max_count]:
            self.max_count -= 1
            
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()