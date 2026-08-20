# Last updated: 8/20/2026, 2:13:42 AM
class Logger:

    def __init__(self):
        self.logs = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.logs:
            self.logs[message] = timestamp
            return True
        
        elif timestamp - self.logs[message] >= 10:
            self.logs[message] = timestamp
            return True
        
        else:
            return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)