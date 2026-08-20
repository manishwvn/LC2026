# Last updated: 8/20/2026, 2:07:22 AM
class RecentCounter:

    def __init__(self):
        self.queue = deque()
        

    def ping(self, t: int) -> int:
        
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()
            
        self.queue.append(t)
            
        return len(self.queue)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)