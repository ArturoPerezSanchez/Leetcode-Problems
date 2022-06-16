# https://leetcode.com/problems/logger-rate-limiter

class Logger:

    def __init__(self):
        self.d = {}

    def shouldPrintMessage(self, t: int, message: str) -> bool:
        if(message not in self.d):
            self.d[message] = t+10
            return True
        res = self.d[message]<=t
        if(res): self.d[message] = t+10
        return res
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)