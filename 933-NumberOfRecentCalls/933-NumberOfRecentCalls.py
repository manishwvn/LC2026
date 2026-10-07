# Last updated: 10/7/2026, 3:03:24 PM
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